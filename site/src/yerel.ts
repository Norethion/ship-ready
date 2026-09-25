// Yerel sayfa: aynı sitenin SHIP_YEREL=1 ile derlenmiş hâli (python uygulama/guncelle.py derler, çıktı ship-ready/sayfa/).
// Raporlar, raporu ship-ready'ye kaydettiren denetim prompt'u ve çevrimdışı arama sadece bu derlemede vardır.
// Verisi src/yerel/ altındadır (uygulama/site_uret.py yazar); herkese açık derleme bu klasörü okumaz.
import fs from 'node:fs';
import path from 'node:path';

export const YEREL = process.env.SHIP_YEREL === '1';
/** ship-ready klasörü; derleme site/ klasöründe çalışır. */
export const KOK = path.resolve(process.cwd(), '..');

export type Sayilar = Record<'✅' | '⚠' | '❌' | '➖', number>;
export interface Degisim {
	id: string;
	once: string;
	simdi: string;
}
export interface Rapor {
	yol: string;
	tarih: string;
	sayilar: Sayilar;
	onceki: { yol: string; tarih: string; sayilar: Sayilar } | null;
	fark: { duzelen: Degisim[]; bozulan: Degisim[]; degisen: Degisim[]; yeni: string[] } | null;
	metin: string;
}
export interface RaporGrubu {
	proje: string;
	baslik: string;
	liste: string;
	liste_adi: string;
	raporlar: Rapor[];
}

export function raporVerisi(): RaporGrubu[] {
	if (!YEREL) return [];
	return JSON.parse(fs.readFileSync(path.join(process.cwd(), 'src', 'yerel', 'raporlar.json'), 'utf-8')).gruplar;
}

export const tarih = (d: string) => d.split('-').reverse().join('.');
