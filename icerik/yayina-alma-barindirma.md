# Yayına alma & barındırma

<!-- sira: 6 -->
<!-- grup: Rehberler -->
<!-- ikon: server -->

<!-- yan-yana -->

Projeyi yayına alırken kullanılan servisler ve yayın öncesi listesinde bunlarla çözülen maddeler.
Ücretler 25.09.2026'da sitelerinden alındı.

## Servisler

| Servis | Tür | Ne işe yarar | Ne zaman | Ücret |
|---|---|---|---|---|
| [Coolify](https://coolify.io) | Kendi sunucunda PaaS | Vercel, Heroku, Netlify ve Railway'e açık kaynak alternatif; kendi sunucuna (VPS, Raspberry Pi, bulut) kurulur. Git'e push edince uygulamayı yayına alır, 300'den fazla hazır servisi (veritabanları dahil) tek tıkla kurar, Let's Encrypt SSL sertifikasını otomatik alır, veritabanı yedeklerini S3 uyumlu depoya gönderir. | Backend, veritabanı ya da Docker gerektiren projeler | Kendi sunucunda ücretsiz ve açık kaynak; yönetilen Coolify Cloud ücretli |
| [Dokploy](https://github.com/Dokploy/dokploy) | Kendi sunucunda PaaS | Coolify'a benzer açık kaynak alternatif: uygulama ve veritabanı yayına alma, Docker Compose, otomatik yedek, Traefik ile yönlendirme ve kaynak izleme; tek komutla kurulur. | Coolify yerine; ikisinden birini seç | Kendi sunucunda ücretsiz (çekirdek Apache-2.0; SSO ve roller gibi kurumsal özellikler ticari lisans ister); Dokploy Cloud ücretli |
| [fastlane](https://github.com/fastlane/fastlane) | Mobil yayın otomasyonu | iOS ve Android'de ekran görüntüsü üretme, imzalama (provisioning profile) ve App Store ya da Google Play'e yükleme işlerini tek komuta bağlar; proje içindeki Fastfile ile tanımlanır. | Mobil uygulamayı sık yayınlıyorsan | Ücretsiz, MIT; anonim kullanım verisi gönderir, `opt_out_usage` ile kapatılır |
| [Prometheus](https://github.com/prometheus/prometheus) ve [Grafana](https://github.com/grafana/grafana) | İzleme ve alarm | Prometheus sunucudan ve uygulamadan metrik toplar, Grafana bunları panolarda gösterir ve eşik aşılınca Slack gibi kanallara alarm gönderir. | Kendi sunucunda çalışan uygulamalar | Kendi sunucunda ücretsiz; Prometheus Apache-2.0, Grafana AGPL-3.0 |
| [Cloudflare](https://www.cloudflare.com) | DNS, CDN ve güvenlik | Alan adının DNS'i; trafiği önbelleğe alan ve saldırılara karşı koruyan proxy, ücretsiz SSL, DDoS koruması, güvenlik ve rate limiting kuralları. | Her projenin önünde | Ücretsiz planda SSL, CDN ve DDoS koruması var |
| [Cloudflare Workers ve Pages](https://workers.cloudflare.com) | Site ve sunucusuz barındırma | Statik siteleri ve küçük API'leri barındırır; Git'e push edince yayına alır. Webhook alıcıları ve yönlendirmeler için de uygun. | Tanıtım siteleri, hafif backend işleri | Ücretsiz planda günde 100.000 istek; statik dosya istekleri ücretsiz ve sınırsız |
| [Cloudflare R2](https://www.cloudflare.com/developer-platform/products/r2/) | Dosya depolama | S3 uyumlu depolama; dışarı veri çıkışı (egress) ücretsiz. | Kullanıcı dosyaları, görseller, yedekler | Ayda 10 GB, 1 milyon yazma ve 10 milyon okuma işlemine kadar ücretsiz |
| [Cloudflare Tunnel](https://www.cloudflare.com/products/tunnel/) | Güvenli erişim | Sunucuda port açmadan uygulamayı internete ya da sadece ekibe açar. | Ev ya da ofis sunucusu, iç araçlar, staging | Ücretsiz |
| [Cloudflare Turnstile](https://www.cloudflare.com/products/turnstile/) | Bot koruması | CAPTCHA yerine görünmez doğrulama; giriş, kayıt ve iletişim formlarını botlardan korur. | Herkese açık formlar | Ücretsiz |

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
