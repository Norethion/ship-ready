// Yerel sayfayı (SHIP_YEREL=1 derlemesi) sunucusuz açılır hale getiren Astro eklentisi. Derleme bitince her sayfada:
//  - site içi adresler göreli olur, klasör adresleri index.html'e gider (dosyadan açılınca tarayıcı klasörü sayfa saymaz),
//  - modül betikleri esbuild ile tek bir satır içi betikte toplanır (tarayıcılar file:// altında dış modül dosyası yüklemez),
// ve arama dizini (src/yerel/arama.json) arama.js olarak yazılır.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { build } from 'esbuild';

const MODUL = /<script type="module"(?: src="([^"]+)")?>([\s\S]*?)<\/script>/g;

function sayfalar(klasor) {
	return fs.readdirSync(klasor, { withFileTypes: true }).flatMap((d) => {
		const p = path.join(klasor, d.name);
		return d.isDirectory() ? sayfalar(p) : d.name.endsWith('.html') ? [p] : [];
	});
}

function goreli(onek, yol) {
	const i = yol.search(/[?#]/);
	const p = i < 0 ? yol : yol.slice(0, i);
	const kalan = i < 0 ? '' : yol.slice(i);
	const hedef = p === '' || p.endsWith('/') ? `${p}index.html` : path.posix.extname(p) ? p : `${p}/index.html`;
	return onek + hedef + kalan;
}

async function paketle(girdiler, kok, astro, sira) {
	const gecici = [];
	const satirlar = girdiler.map((g, i) => {
		let dosya = path.join(kok, (g.src ?? '').replace(/^\//, ''));
		if (!g.src) {
			dosya = path.join(astro, `__satir-${sira}-${i}.js`);
			fs.writeFileSync(dosya, g.kod.replace(/(["'])\/_astro\//g, '$1./'));
			gecici.push(dosya);
		}
		return `import ${JSON.stringify(dosya.replaceAll('\\', '/'))};`;
	});
	try {
		const sonuc = await build({
			stdin: { contents: satirlar.join('\n'), resolveDir: astro, loader: 'js' },
			bundle: true,
			format: 'esm',
			minify: true,
			target: 'es2022',
			write: false,
			logLevel: 'silent',
		});
		return sonuc.outputFiles[0].text.replace(/<\/script/gi, '<\\/script');
	} finally {
		gecici.forEach((f) => fs.rmSync(f));
	}
}

export default function yerelDerleme() {
	return {
		name: 'ship-yerel-derleme',
		hooks: {
			'astro:build:done': async ({ dir, logger }) => {
				const kok = fileURLToPath(dir);
				const astro = path.join(kok, '_astro');
				const dizin = fs.readFileSync(new URL('./src/yerel/arama.json', import.meta.url), 'utf-8').trim();
				fs.writeFileSync(path.join(kok, 'arama.js'), `window.SHIP_ARAMA = ${dizin};\n`);
				const paketler = new Map();
				const liste = sayfalar(kok);
				for (const dosya of liste) {
					let html = fs.readFileSync(dosya, 'utf-8');
					const girdiler = [];
					html = html.replace(MODUL, (_, src, kod) => {
						girdiler.push(src ? { src } : { kod });
						return '';
					});
					const derinlik = path.relative(kok, path.dirname(dosya)).split(path.sep).filter(Boolean).length;
					const onek = '../'.repeat(derinlik);
					html = html.replace(/(\s(?:href|src))="\/(?!\/)([^"]*)"/g, (_, ad, yol) => `${ad}="${goreli(onek, yol)}"`);
					if (girdiler.length) {
						const anahtar = JSON.stringify(girdiler);
						if (!paketler.has(anahtar)) paketler.set(anahtar, await paketle(girdiler, kok, astro, paketler.size));
						html = html.replace('</body>', () => `<script type="module">${paketler.get(anahtar)}</script></body>`);
					}
					fs.writeFileSync(dosya, html);
				}
				// Betiklerin hepsi sayfaların içine alındı.
				for (const f of fs.readdirSync(astro)) if (f.endsWith('.js')) fs.rmSync(path.join(astro, f));
				logger.info(`${liste.length} sayfa dosyadan açılacak şekilde hazırlandı`);
			},
		},
	};
}
