# ship-ready

[English](README.md) · **Türkçe**

ship-ready, AI ile geliştirilen kişisel projeleri yayına hazırlamak için Türkçe kontrol listeleri, rehberler ve bir GitHub repo kataloğu sunar.
Herkese açık bir Astro Starlight sitesi ve proje denetim raporları için ayrı bir yerel sayfa sağlar.

## İçerik

- Kalıcı madde kimlikleri olan yayın öncesi, App Store, Google Play ve paywall kontrol listeleri.
- AI geliştirme, UI/UX, analitik ve barındırma rehberleri ile doğrulanmış GitHub repolarından oluşan bir katalog.
- Denetim raporları ve çevrimdışı arama içeren yerel sayfa ile içerik ve raporları kodlama ajanlarına açan bir Python MCP sunucusu.
- Denetim raporlarını ve diğer yerel verileri içermeyen herkese açık site derlemesi.

## Teknoloji ve yerel kullanım

İçerik ve katalog Markdown ile JSON kullanır; üretim araçları ve MCP sunucusu Python standart kütüphanesini kullanır.
Site, Node.js ve npm ile Astro ve Starlight kullanır.
Komut içinde `site/` klasörüne geçilmediği sürece bu komutları depo kökünden çalıştırın:

| İş | Komut |
|---|---|
| Site bağımlılıklarını kur | `cd site; npm ci` |
| Geliştirme sunucusunu başlat | `cd site; npm run dev` |
| Herkese açık siteyi `site/dist/` altında derle | `cd site; npm run build` |
| Herkese açık derlemeyi önizle | `cd site; npm run preview` |
| İçeriği yeniden üret ve yerel sayfayı `sayfa/` altında derle | `python uygulama/guncelle.py` |
| Madde kimliklerini, atıfları ve raporları doğrula | `python uygulama/katalog.py dogrula` |
| GitHub verilerini güncelle ve içerik bağlantılarını denetle | `python uygulama/guncelle.py --github` |

Yerel sayfayı derlemeden önce site bağımlılıklarını kurun.
Yerel sayfayı ürettikten sonra kökteki `index.html` dosyasını açarak `sayfa/` klasörüne gidin.

## Proje yapısı

| Yol | İçerik |
|---|---|
| `icerik/` | Kaynak kontrol listeleri ve rehberler. |
| `veri/` | Repo kataloğu, bağlantı kontrolü sonuçları ve yerel denetim raporları. |
| `uygulama/` | Katalog ayrıştırıcısı, site üreticisi, güncelleme komutu ve MCP sunucusu. |
| `site/` | Astro Starlight sitesi, bileşenler, stiller ve canlı rehber örnekleri. |
| `skills/` | Yayın öncesi, App Store ve Google Play denetim skill'leri. |
| `docs/proje-referansi.md` | İçerik biçimleri, katalog verileri, raporlar ve site davranışı için ayrıntılı referans. |

## Yayın ve belgeler

`site/dist/` herkese açık derlemenin çıktısıdır; bu depoda onun için canlı yayın tanımlı değildir.
Denetim raporları yalnızca yerel sayfada ve MCP arayüzünde görünür.
Üretim kuralları ve site davranışı için [proje referansına](docs/proje-referansi.md), genel yayına alma ve barındırma bilgileri için [barındırma rehberine](icerik/yayina-alma-barindirma.md) bakın.
