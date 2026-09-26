// Sitenin iki araması (yerel sayfadaki arama penceresi ve repo kataloğunun arama kutusu) aynı eşleştirmeyi kullanır:
// Türkçe büyük/küçük harf ve şapka, nokta farkı yok sayılır, "ve, için, nasıl" gibi dolgu kelimeleri atılır,
// ekli kelimeler kökünden eşleşir ("animasyonları" → "animasyon").

export const katla = (s: string) =>
	s.toLocaleLowerCase('tr').normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/ı/g, 'i');

const DOLGU = new Set(
	've ile icin bir bu su ne nasil neden hangi hangisi mi mu da de ki gibi olan olarak var en cok daha her bana beni benim ben lazim istiyorum yapmak yapan yapmaliyim yapmali olmali olsun nedir and or the for to of with how what'.split(
		' ',
	),
);

/** Sorgunun aranacak kelimeleri: katlanmış, dolgu kelimeleri ve tek harfler atılmış. */
export function terimler(sorgu: string): string[] {
	return katla(sorgu)
		.split(/[^\p{L}\p{N}]+/u)
		.filter((t) => t.length > 1 && !DOLGU.has(t));
}

/** Terimin metinde eşleşen kısmı: terimin tamamı ya da en uzun kökü (en az 4 harf ve terimin %60'ı); eşleşmezse boş.
 * İki harfli kelimeler ("az", "ai") başka kelimelerin içinde her yerde geçtiği için sadece tam kelime olarak eşleşir. */
export function eslesenParca(terim: string, metin: string): string {
	if (terim.length < 3) return new RegExp(`(^|[^\\p{L}\\p{N}])${terim}([^\\p{L}\\p{N}]|$)`, 'u').test(metin) ? terim : '';
	if (metin.includes(terim)) return terim;
	for (let n = terim.length - 1; n >= Math.max(4, Math.ceil(terim.length * 0.6)); n--) {
		const kok = terim.slice(0, n);
		if (metin.includes(kok)) return kok;
	}
	return '';
}

/** Eşleşmenin ağırlığı: tam 1, kökten 0,7, yok 0. */
export function eslesme(terim: string, metin: string): number {
	const p = eslesenParca(terim, metin);
	return p === terim ? 1 : p ? 0.7 : 0;
}
