// @ts-check
// ship-ready sitesi. İçerik ve kenar menü uygulama/site_uret.py ile icerik/ ve veri/ klasörlerinden üretilir;
// src/content/docs/, src/data/ ve src/yerel/ altındakiler elle düzenlenmez.
// İki derlemesi var: npm run build herkese açık siteyi dist/'e derler; SHIP_YEREL=1 (python uygulama/guncelle.py yapar)
// raporlu yerel sayfayı ship-ready/sayfa/'ya derler, o da sunucusuz, çift tıklamayla açılır (yerel-derleme.mjs).
import fs from 'node:fs';
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import yerelDerleme from './yerel-derleme.mjs';

const YEREL = process.env.SHIP_YEREL === '1';
const sidebar = JSON.parse(fs.readFileSync(new URL(YEREL ? './src/yerel/sidebar.json' : './src/data/sidebar.json', import.meta.url), 'utf-8'));

export default defineConfig({
	outDir: YEREL ? '../sayfa' : './dist',
	integrations: [
		starlight({
			title: 'ship-ready',
			description:
				'AI ile kişisel proje geliştirip yayına çıkarırken başvurulan Türkçe kontrol listeleri, rehberler ve doğrulanmış araçlar.',
			locales: { root: { label: 'Türkçe', lang: 'tr' } },
			sidebar,
			components: {
				Sidebar: './src/components/KenarMenu.astro',
				SiteTitle: './src/components/SiteBasligi.astro',
				ThemeSelect: './src/components/TemaSecici.astro',
				TableOfContents: './src/components/SayfaIcerigi.astro',
				// Pagefind sunucusuz çalışmaz; yerel sayfada çevrimdışı arama kullanılır.
				...(YEREL ? { Search: './src/components/YerelArama.astro' } : {}),
			},
			pagefind: !YEREL,
			customCss: ['./src/styles/ship.css'],
			tableOfContents: { minHeadingLevel: 2, maxHeadingLevel: 2 },
		}),
		...(YEREL ? [yerelDerleme()] : []),
	],
});
