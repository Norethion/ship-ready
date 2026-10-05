# Yayına alma & barındırma

<!-- sira: 6 -->
<!-- grup: Rehberler -->
<!-- ikon: server -->

<!-- yan-yana -->

Projeyi yayına alırken kullanılan servisler ve yayın öncesi listesinde bunlarla çözülen maddeler.
Servisler tablosunun ücretleri 25.09.2026'da, mobil servislerin ücretsiz sınırları 05.10.2026'da sitelerinden alındı.

## Servisler

| Servis | Tür | Ne işe yarar | Ne zaman | Ücret |
|---|---|---|---|---|
| [Coolify](https://coolify.io) | Kendi sunucunda PaaS | Vercel, Heroku, Netlify ve Railway'e açık kaynak alternatif; kendi sunucuna (VPS, Raspberry Pi, bulut) kurulur. Git'e push edince uygulamayı yayına alır, 300'den fazla hazır servisi (veritabanları dahil) tek tıkla kurar, Let's Encrypt SSL sertifikasını otomatik alır, veritabanı yedeklerini S3 uyumlu depoya gönderir. | Backend, veritabanı ya da Docker gerektiren projeler | Kendi sunucunda ücretsiz ve açık kaynak; yönetilen Coolify Cloud ücretli |
| [Dokploy](https://github.com/Dokploy/dokploy) | Kendi sunucunda PaaS | Coolify'a benzer açık kaynak alternatif: uygulama ve veritabanı yayına alma, Docker Compose, otomatik yedek, Traefik ile yönlendirme ve kaynak izleme; tek komutla kurulur. | Coolify yerine; ikisinden birini seç | Kendi sunucunda ücretsiz (çekirdek Apache-2.0; SSO ve roller gibi kurumsal özellikler ticari lisans ister); Dokploy Cloud ücretli |
| [fastlane](https://github.com/fastlane/fastlane) | Mobil yayın otomasyonu | iOS ve Android'de ekran görüntüsü üretme, imzalama (provisioning profile) ve App Store ya da Google Play'e yükleme işlerini tek komuta bağlar; proje içindeki Fastfile ile tanımlanır. | Mobil uygulamayı sık yayınlıyorsan | Ücretsiz, MIT; anonim kullanım verisi gönderir, `opt_out_usage` ile kapatılır |
| [Prometheus](https://github.com/prometheus/prometheus) ve [Grafana](https://github.com/grafana/grafana) | İzleme ve alarm | Prometheus sunucudan ve uygulamadan metrik toplar, Grafana bunları panolarda gösterir ve eşik aşılınca Slack gibi kanallara alarm gönderir. | Kendi sunucunda çalışan uygulamalar | Kendi sunucunda ücretsiz; Prometheus Apache-2.0, Grafana AGPL-3.0 |
| [Cloudflare](https://www.cloudflare.com) | DNS, CDN ve güvenlik | Alan adının DNS'i; trafiği önbelleğe alan ve saldırılara karşı koruyan proxy, ücretsiz SSL, DDoS koruması, güvenlik ve rate limiting kuralları. | Her projenin önünde | Ücretsiz planda SSL, CDN ve DDoS koruması var |
| [Cloudflare Workers ve Pages](https://workers.cloudflare.com) | Site ve sunucusuz barındırma | Statik siteleri ve küçük API'leri barındırır; Git'e push edince yayına alır. Webhook alıcıları ve yönlendirmeler için de uygun. | Tanıtım siteleri, hafif backend işleri | Ücretsiz planda günde 100.000 istek; statik dosya istekleri ücretsiz ve sınırsız |
| [Vercel](https://vercel.com) | Site ve sunucusuz barındırma | Next.js ve diğer web projelerini Git'e push edince yayına alır, her PR için önizleme adresi verir; sunucusuz fonksiyonlar ve CDN dahil. | Next.js projeleri, tanıtım siteleri | Hobby planı ücretsiz ama sadece ticari olmayan kişisel kullanım için: ödeme alan, satış yapan, reklam ya da affiliate içeren site ücretli plan ister ([Vercel kullanım kuralları](https://vercel.com/docs/limits/fair-use-guidelines)) |
| [Cloudflare R2](https://www.cloudflare.com/developer-platform/products/r2/) | Dosya depolama | S3 uyumlu depolama; dışarı veri çıkışı (egress) ücretsiz. | Kullanıcı dosyaları, görseller, yedekler | Ayda 10 GB, 1 milyon yazma ve 10 milyon okuma işlemine kadar ücretsiz |
| [Cloudflare Tunnel](https://www.cloudflare.com/products/tunnel/) | Güvenli erişim | Sunucuda port açmadan uygulamayı internete ya da sadece ekibe açar. | Ev ya da ofis sunucusu, iç araçlar, staging | Ücretsiz |
| [Cloudflare Turnstile](https://www.cloudflare.com/products/turnstile/) | Bot koruması | CAPTCHA yerine görünmez doğrulama; giriş, kayıt ve iletişim formlarını botlardan korur. | Herkese açık formlar | Ücretsiz |

## Mobil uygulama servisleri

Mobil uygulamada sık kullanılan derleme, backend, bildirim ve e-posta servisleri; liste [bu videodan](https://www.instagram.com/reel/Dd6jhGxFbkV/) alındı, sınırlar servislerin kendi fiyat sayfalarından doğrulandı.
Ücretsiz sınırlar sık değişiyor; ücretli plana geçmeden önce sayfasına yeniden bak.

| Servis | Tür | Ne işe yarar | Ne zaman | Ücret |
|---|---|---|---|---|
| [Expo EAS](https://expo.dev/eas) | Mobil derleme | React Native uygulamasını bulutta iOS ve Android için derler (Mac gerekmez), mağazalara gönderir (EAS Submit), JavaScript değişikliklerini mağaza incelemesine girmeden kullanıcılara ulaştırır (EAS Update). | React Native ya da Expo projesi | Ücretsiz planda ayda 15 Android ve 15 iOS derlemesi (düşük öncelikli kuyruk), EAS Update ile 1.000 aylık aktif kullanıcı; kota bitince ücret çıkmaz, derleme ay başını bekler. Starter ayda 19 $ |
| [Codemagic](https://codemagic.io) | Mobil CI/CD | Flutter, React Native ve yerel iOS ya da Android projesini her push'ta derler, test eder, imzalar ve App Store Connect ile Google Play'e yükler; macOS makinesi onlarda. | Flutter projesi ya da Mac'in yoksa | Kişisel hesapta ayda 500 dakika macOS derlemesi ücretsiz (tek eşzamanlı derleme, derleme başına en çok 120 dakika); sonrası dakika başına 0,095 $'dan |
| [Supabase](https://supabase.com) | Backend (Postgres) | Postgres veritabanı, giriş, dosya depolama, gerçek zamanlı veri ve sunucusuz fonksiyonlar; veritabanına otomatik REST API açar. Her tabloda RLS açık olmalı ([yayın öncesi {{no:yo-en-az-yetki}}. madde](yayin-oncesi-maddeler.md)). | İlişkisel veri ve SQL isteyen projeler | Ücretsiz planda en çok 2 aktif proje, proje başına 500 MB veritabanı, 1 GB depolama ve 50.000 aylık aktif kullanıcı; yedek yok, 1 hafta kullanılmayan proje duraklatılır. Pro ayda 25 $ |
| [Firebase](https://firebase.google.com) | Backend (Google) | Firestore veritabanı, giriş (Authentication), bildirim (Cloud Messaging), uzaktan ayar (Remote Config), çökme raporu (Crashlytics) ve barındırma (Hosting) tek projede, hazır mobil SDK'larıyla. | Mobil uygulamada hızlı başlangıç | Spark planı ücretsiz: Firestore'da 1 GiB ve günde 50.000 okuma, 20.000 yazma; Authentication'da 50.000 aylık aktif kullanıcı (SMS ile giriş sadece ücretli Blaze planında); Cloud Messaging ve Crashlytics ücretsiz; Remote Config 1 Eylül 2026'dan beri günde 100.000 isteğe kadar ücretsiz; Hosting'de 10 GB depolama ve günde 360 MB aktarım |
| [OneSignal](https://onesignal.com) | Bildirim kampanyası | Push bildirimi, uygulama içi mesaj, e-posta ve SMS kampanyalarını panelden zamanlar, kullanıcı gruplarına göre gönderir, açılma oranını ölçer. | Pazarlama bildirimleri; işlem bildirimleri için Firebase Cloud Messaging yeter | Ücretsiz planda mobil push ve uygulama içi mesaj 1.000 aylık aktif kullanıcıya kadar (Ekim 2026'dan beri; aşılırsa 24 saat içinde yükseltilmezse mobil push durur) ve ayda 10.000 e-posta. Growth ayda 19 $'dan |
| [Resend](https://resend.com) | İşlem e-postası | Kayıt, şifre sıfırlama ve fatura e-postalarını API ile gönderir; şablonlar React ile yazılabilir, alan adı için gereken SPF ve DKIM kayıtlarını gösterir. | Uygulamanın kendi gönderdiği e-postalar ([yayın öncesi {{no:yo-eposta-alt-alan}}. madde](yayin-oncesi-maddeler.md)) | Ücretsiz planda ayda 3.000, günde 100 e-posta ve 3 alan adı. Pro ayda 20 $ (50.000 e-posta) |
| [Zoho Mail](https://www.zoho.com/mail/) | Alan adlı e-posta kutusu | `destek@alanadi.com` gibi gelen kutusu; mağaza sayfalarında istenen destek adresi için. | Mağaza destek ve iletişim adresi | Forever Free planı: 5 kullanıcı, tek alan adı, kullanıcı başına 5 GB; sadece web ve mobil uygulamadan erişilir, IMAP, POP ve yönlendirme yok. Ücretsiz plan her veri merkezinde sunulmuyor |
| [TestFlight](https://developer.apple.com/testflight/) | iOS beta testi | Uygulamanın test sürümünü mağazaya çıkmadan kullanıcılara dağıtır, geri bildirim ve çökme raporu toplar. | iOS'ta yayından önce | Ücretsiz ama Apple Developer Program üyeliği (yıllık 99 $) gerekir; iç testte 100, dış testte 10.000 kişi, bir derleme 90 gün test edilebilir; dış testteki ilk derleme Beta App Review'a girer |

## Yayın öncesi maddeleriyle bağlantısı

- **HTTPS ve HSTS ([{{no:yo-https-hsts}}. madde](yayin-oncesi-maddeler.md)):** Coolify SSL sertifikasını otomatik alır; Cloudflare'de "Always Use HTTPS" ve HSTS açılır.
- **Güvenlik başlıkları ([{{no:yo-guvenlik-basliklari}}. madde](yayin-oncesi-maddeler.md)):** Uygulamada ya da Cloudflare'in yanıt başlığı kurallarıyla eklenir.
- **Bot ve rate limit ([{{no:yo-hesap-kilitleme}}–{{no:yo-rate-limit-bot-korumasi}}. maddeler](yayin-oncesi-maddeler.md)):** Giriş ve kayıt formlarında Turnstile, API'de Cloudflare rate limiting kuralı.
- **Staging dışarıya kapalı ([{{no:yo-env-gecmisten-temizle}}. madde](yayin-oncesi-maddeler.md)):** Staging'i herkese açık alan adına koymak yerine Cloudflare Tunnel ile sadece ekibe aç.
- **Alt alan adları ve e-posta ([{{no:yo-alt-alan-adi}}–{{no:yo-eposta-alt-alan}}. maddeler](yayin-oncesi-maddeler.md)):** `app.` için CNAME, `mail.` ve `news.` için SPF, DKIM ve DMARC kayıtları Cloudflare DNS'e girilir.
- **Yedekleme ([{{no:yo-yedekleme}}. madde](yayin-oncesi-maddeler.md)):** Coolify veritabanı yedeklerini zamanlayıp R2 gibi S3 uyumlu bir depoya gönderir; geri yükleme testini ayrıca yap.
- **Bağımlılık denetimi ([{{no:yo-bagimlilik-denetimi}}. madde](yayin-oncesi-maddeler.md)):** [OSV-Scanner](https://github.com/google/osv-scanner) bağımlılıkları ve container imajlarını bilinen açıklara karşı tarar (kaynak kod gönderilmez); JS/TS projesinde [Knip](https://github.com/webpro-nl/knip) kullanılmayan paket ve dosyaları bulur.
- **Directory listing ve source map ([{{no:yo-directory-listing}} ve {{no:yo-source-map-kapali}}. maddeler](yayin-oncesi-maddeler.md)):** Barındırmada klasör listelemenin kapalı olduğunu ve `.map` dosyalarının yayına çıkmadığını kontrol et.
- **Kesintisiz güncelleme ve geri dönüş ([{{no:yo-kesintisiz-surum}}–{{no:yo-geriye-uyumlu-sema}}. maddeler](yayin-oncesi-maddeler.md)):** Coolify, sağlık kontrolü tanımlıysa yeni sürümü eskisiyle bir süre birlikte çalıştırarak günceller (rolling update); kesintisizliği garanti etmez, host'a port açılmışsa ya da Docker Compose kullanılıyorsa çalışmaz. Sorun çıkarsa Configuration > Rollback'ten sunucuda tutulan eski sürüme dönülür; ama bu veritabanı değişikliklerini geri almaz, şema değişiklikleri geriye uyumlu olmalı ([rolling update](https://coolify.io/docs/knowledge-base/rolling-updates), [rollback](https://coolify.io/docs/applications/deployments/rollbacks)).
