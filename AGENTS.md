# ship-ready

## Proje

ship-ready, kişisel projeleri AI ile geliştirirken yayına hazırlık için kullanılan Türkçe kontrol listeleri, rehberler ve repo kataloğudur.
Astro ile üretilen herkese açık derleme `site/dist/` altındadır; denetim raporları yalnızca yerel sayfada ve MCP arayüzünde görünür.
Herkese açık derlemenin canlı yayını bu depoda tanımlı değildir.

Teknoloji: Python standart kütüphanesi; Astro ve Starlight; Node.js ve npm; Markdown ve JSON.

## Dosya haritası

- `icerik/*.md`: kontrol listeleri ve rehberlerin kaynak metinleri.
- `veri/repolar.json`, `veri/linkler.json`, `veri/raporlar/`: katalog, link kontrolü ve kişisel denetim raporları.
- `uygulama/katalog.py`: içerik ve veri için tek ayrıştırma çekirdeği; `mcp_sunucu.py` ve `site_uret.py` bunu kullanır.
- `uygulama/guncelle.py`: kaynaklardan siteyi ve yerel sayfayı üretir, `AGENTS.md` dosyasını `CLAUDE.md` dosyasına kopyalar.
- `site/src/components/`, `site/src/styles/`, `site/src/pages/`: elle düzenlenen Astro arayüzü; `site/public/ornekler/`: rehber kartlarındaki canlı örnekler; `skills/`: denetim skill'leri.
- [Proje referansı](docs/proje-referansi.md): içerik biçimleri, katalog şeması, raporlar, URL'ler ve site davranışı.

## Komutlar

Komutları aksi belirtilmedikçe depo kökünden çalıştır.

| İş | Komut |
|---|---|
| Site bağımlılıklarını kur | `cd site; npm ci` |
| Geliştirme sunucusu | `cd site; npm run dev` |
| Herkese açık derleme | `cd site; npm run build` |
| Derlemeyi önizle | `cd site; npm run preview` |
| İçerik, rapor veya katalog değişikliğinden sonra yerel sayfayı üret | `python uygulama/guncelle.py` |
| Kimlik, atıf ve rapor doğrulaması | `python uygulama/katalog.py dogrula` |
| GitHub verilerini ve içerik linklerini denetle | `python uygulama/guncelle.py --github` |

`site/package.json` içinde lint, typecheck veya test komutu yoktur; bu depoda `.github/workflows` ve PR için tanımlı CI kontrolü de yoktur.
Veritabanı ve tarayıcı testi bulunmaz.

## Korunacak sınırlar

- `icerik/*.md`, `veri/*.json` ve `veri/raporlar/` kaynak veridir; üretilen dosyaları elle düzenleme ([üretim ayrıntıları](docs/proje-referansi.md)).
- Raporları ve diğer kişisel verileri herkese açık derlemeye sokma; yerel koşullandırma `site/src/yerel.ts` içindeki `YEREL` üzerinden yapılır ([yerel sayfa](docs/proje-referansi.md)).
- Madde kimlikleri kalıcıdır; numaralı atıflarda `{{no:kimlik}}` kullanılır ([içerik biçimi](docs/proje-referansi.md)).
- Yeni repoyu kaynağından doğrula; GitHub 404 kaydı gizli veya erişilemez de kılabilir, bu nedenle katalogdan çıkarmadan önce sahibinin onayını al ([katalog kuralları](docs/proje-referansi.md)).
- `AGENTS.md` kaynak dosyadır; `CLAUDE.md` ile bayt düzeyinde eşit tut ve `site/CLAUDE.md` bağlantısını koru ([üretim ayrıntıları](docs/proje-referansi.md)).

## Git akışı

`main` üzerinden kısa ömürlü dalda çalış, `main` dalına PR aç ve PR'ı kimseye atama; `test` dalı yoktur.
PR'ı sahibi normal merge commit ile birleştirir.
Commit mesajları ve PR metinleri (başlık, açıklama, yorumlar) Türkçe yazılır.
Commit ve push yalnızca sahibi istediğinde yapılır.
