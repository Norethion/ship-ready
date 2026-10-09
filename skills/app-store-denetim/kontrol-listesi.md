# App Store incelemesi

<!-- sira: 2 -->
<!-- liste: app-store -->
<!-- grup: Kontrol listeleri -->
<!-- ikon: phone -->

En sık 27 red sebebi ve her biri için ne yapılacağı.
Apple uygulamayı reddederken çoğu zaman sadece bir kural numarası ve iki cümle yazar; hangi ekranda neyin eksik olduğunu söylemez.
Bu sebeplerin çoğu kod hatası değil; eksik anlatılan, unutulan ya da yanlış girilen ayarlar.
Liste [bu videodan](https://www.instagram.com/reel/DctdIykgb9C/) ve aynı hesabın 24 maddelik ikinci listesinden alındı; kural numaraları 25.09.2026'da [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/) sayfasından doğrulandı.

## Ödeme ve abonelik

| # | Red sebebi | Ne yapmalı | Kural |
|---|---|---|---|
| 1 <!-- id: as-paywall-linkleri --> | Satın alma ekranında (paywall) link yok | Abonelik ekranına Kullanım Koşulları (EULA) ve Gizlilik Politikası linklerini koy; ayrıca App Store Connect'teki uygulama açıklamasına da ekle. | 3.1.2 |
| 2 <!-- id: as-fiyat-bilgisi --> | Fiyat yazmıyor | Kullanıcı abone olmadan önce ne alacağını, fiyatı, süreyi ve deneme bitince ne kadar ödeyeceğini açıkça görsün; "Premium'a geç" tek başına yetmez. | 3.1.2(a), 3.1.2(c) |
| 3 <!-- id: as-geri-yukleme --> | Satın almayı geri yükleme (restore) yok | Geri yüklenebilen satın almalar için "Satın almaları geri yükle" düğmesi olsun. | 3.1.1 |
| 4 <!-- id: as-dis-odeme-linki --> | Dış ödeme linki | Dijital ürün ve abonelikleri uygulama dışında satın aldıran düğme ya da link koyma. ABD mağazasında bu yasak uygulanmıyor; diğer ülkelerde reddedilir. | 3.1.1(a) |

## Gizlilik ve izinler

| # | Red sebebi | Ne yapmalı | Kural |
|---|---|---|---|
| 5 <!-- id: as-hesap-silme --> | Hesap silme yok | Uygulamada hesap açılabiliyorsa hesap silme de uygulamanın içinden yapılabilmeli; sadece e-posta ile talep yetmez. | 5.1.1(v) |
| 6 <!-- id: as-izin-gerekcesi --> | İzin gerekçesi yok | Kamera, konum, rehber gibi izin isteklerinde verinin neden ve nasıl kullanılacağını açıkça yaz; "Kamera erişimi gerekli" yetmez. | 5.1.1(ii) |
| 7 <!-- id: as-takip-izni --> | Takip izni yok | Kullanıcıyı başka uygulama ve sitelerde takip ediyorsan (reklam kimliği, bazı analitik SDK'ları) App Tracking Transparency izni iste. | 5.1.2(i) |
| 8 <!-- id: as-ucuncu-taraf-ai --> | Veri AI servisine izinsiz gidiyor | Kullanıcının metni, fotoğrafı ya da sesi OpenAI, Anthropic, Gemini gibi bir AI servisine gidiyorsa ilk gönderimden önce hangi verinin hangi sağlayıcıya gittiğini açıkça söyleyip açık izin al; aynı bilgiyi gizlilik politikasına da yaz. Kural AI ile üretilen içeriği etiketlemeyi değil, kişisel verinin üçüncü taraf AI ile paylaşılmasını kapsar (13.11.2025'te eklendi). | 5.1.2(i) |
| 9 <!-- id: as-gizlilik-etiketi --> | Gizlilik etiketi yanlış | App Store Connect'teki gizlilik bilgileri, uygulamanın ve eklediğin SDK'ların (analitik, reklam, çökme raporu) gerçekte topladığı veriyle birebir aynı olsun. | 2.3, 5.1.1(i) |
| 10 <!-- id: as-gizlilik-politikasi-linki --> | Gizlilik politikası linki yok | Gizlilik politikası linkini hem App Store Connect'teki alana hem de uygulamanın içinde kolay bulunur bir yere koy; sadece satın alma ekranında olması yetmez. | 5.1.1(i) |
| 11 <!-- id: as-esdeger-giris-secenegi --> | Eşdeğer giriş seçeneği yok | Google, Facebook gibi bir hesapla giriş varsa yanında veriyi ad ve e-postayla sınırlayan, e-postayı gizlemeye izin veren ve reklam için izlemeyen bir giriş seçeneği daha sun; Apple ile Giriş bu şartları karşılar. Sadece kendi e-posta ve şifre girişin varsa gerekmez. | 4.8 |

## İnceleme hazırlığı

| # | Red sebebi | Ne yapmalı | Kural |
|---|---|---|---|
| 12 <!-- id: as-yer-tutucu-icerik --> | Yer tutucu içerik | "Lorem ipsum", boş ekran, çalışmayan link ya da "yakında" sayfası bırakma; gönderilen sürüm son sürüm olmalı. | 2.1(a) |
| 13 <!-- id: as-demo-hesap --> | Demo hesap yok | Giriş gerektiren her şey için çalışan ve inceleme sürerken süresi dolmayacak bir demo hesap (ya da tam demo modu) ve gerekiyorsa örnek QR kodu gibi ek bilgileri inceleme notlarına yaz. | 2.1(a) |
| 14 <!-- id: as-gizli-ozellik --> | Gizli özellik | Gizli, kapalı bekleyen ya da belgelenmemiş özellik bırakma; yeni özellikleri inceleme notlarında ayrıntılı anlat ve inceleme ekibinin her özelliğe (ör. satın alma ekranına) nasıl ulaşacağını adım adım yaz, genel açıklama reddedilir. | 2.3.1(a) |
| 15 <!-- id: as-ekran-goruntuleri --> | Ekran görüntüsü yanlış | Ekran görüntüleri uygulamanın kullanımını göstermeli; sadece logo, giriş ya da açılış ekranı olmaz. | 2.3.3 |
| 16 <!-- id: as-cokme --> | Çöküyor | Göndermeden önce gerçek cihazda test et; çöken ya da belirgin hatası olan sürüm reddedilir. | 2.1(a) |
| 17 <!-- id: as-destek-linki --> | Destek linki çalışmıyor | App Store Connect'teki destek linki (Support URL) açılmalı ve sana ulaşmanın kolay bir yolunu göstermeli; boş ya da hata veren sayfa bırakma. | 1.5 |
| 18 <!-- id: as-yas-derecelendirmesi --> | Yaş sınırı yanlış | App Store Connect'teki yaş derecelendirmesi sorularını dürüst cevapla; kullanıcı içeriği, sohbet, kumar ya da yetişkin içerik varsa belirt. | 2.3.6 |

## İçerik ve işlevsellik

| # | Red sebebi | Ne yapmalı | Kural |
|---|---|---|---|
| 19 <!-- id: as-web-gorunumu --> | Sadece web görünümü | Uygulama, paketlenmiş bir web sitesinden fazlası olmalı: uygulamaya özgü özellik, içerik ve arayüz. | 4.2 |
| 20 <!-- id: as-minimum-islevsellik --> | Minimum işlevsellik | Sadece reklam, link koleksiyonu ya da çok basit tek işlev olan uygulamalar reddedilir. | 4.2, 4.2.2 |
| 21 <!-- id: as-cocuk-kategorisi --> | Çocuk kategorisi | Çocuk kategorisindeysen dışarıya link, satın alma ve reklam ebeveyn kilidinin arkasında olmalı; kişisel ve cihaz verisi üçüncü taraflara gitmemeli. | 1.3 |
| 22 <!-- id: as-kullanici-icerigi --> | Kullanıcı içeriği | Kullanıcılar içerik paylaşabiliyorsa uygunsuz içeriği filtreleme, şikâyet etme, kullanıcı engelleme ve iletişim bilgisi şart. | 1.2 |
| 23 <!-- id: as-baskasinin-markasi --> | Başkasının markası | Başka markanın adını, logosunu ya da telifli içeriğini izinsiz kullanma; başka uygulamanın ikonunu ya da adını taklit etme. Açıklamada ve ekran görüntülerinde Android gibi başka platformların adı ya da görseli de geçmesin. | 5.2.1, 4.1(c), 2.3.10 |
| 24 <!-- id: as-saglik-iddiasi --> | Sağlık iddiası | Sağlıkla ilgili ölçüm ya da etki iddiasının verisini ve yöntemini göster; doğrulanamayan iddia ("stresi tedavi eder") reddedilir. | 1.4.1 |
| 25 <!-- id: as-sablon-uygulama --> | Şablon uygulama | Hazır şablonla ya da uygulama üretme servisiyle yapılıp başkası adına gönderilen uygulama reddedilir; içerik sahibi kendi hesabından göndermeli ve uygulama özgün olmalı. | 4.2.6 |
| 26 <!-- id: as-olmayan-ozellik-vaadi --> | Olmayan özellik vaadi | Açıklama, ekran görüntüleri ve önizleme videosu uygulamanın gerçekte yaptığını göstermeli; olmayan özelliği ya da yanlış fiyatı vaat etme. | 2.3, 2.3.1(a) |

## Reddedilince

| # | Red sebebi | Ne yapmalı | Kural |
|---|---|---|---|
| 27 <!-- id: as-red-cevabi --> | Cevap yazmıyorsun | Sessizce yeni sürüm göndermek yerine App Store Connect'te uygulamanın App Review bölümünden inceleme ekibine yaz; neyin eksik olduğunu sor ya da neden kurala uyduğunu açıkla. | App Review |

- **Önce yaz:** Ret mesajına App Store Connect'ten cevap vermek çoğu zaman yeni sürüm göndermekten hızlı sonuç verir.
- **İtiraz:** Uygulamanın yanlış anlaşıldığını düşünüyorsan [App Review Board'a itiraz](https://developer.apple.com/contact/app-store/?topic=appeal) edebilirsin. Her ret için tek itiraz hakkı var; önce ekibin istediği ek bilgileri ver.
- **Görüşme:** Apple, App Review ile 30 dakikalık Webex görüşmesi randevusu da veriyor ([App Review](https://developer.apple.com/distribute/app-review/) sayfasında).
- **İlgili sekmeler:** Satın alma ekranı ve abonelik araçları [Gelir & analitik](gelir-analitik.md) sekmesinde; abonelik şartları ve hesap silme [yayın öncesi listesinin](yayin-oncesi-maddeler.md) 55. ve 104. maddelerinde.

## Göndermeden önce kontrol prompt'u

```
Bu iOS uygulamasını App Store incelemesine göndermeden önce şu 27 red sebebine göre kontrol et: satın alma ekranında Kullanım Koşulları ve Gizlilik Politikası linkleri, fiyat ve deneme süresi açıklaması, satın almaları geri yükleme düğmesi, dış ödeme linki, uygulama içinden hesap silme, izin gerekçesi metinleri, App Tracking Transparency, kişisel veri üçüncü taraf AI servisine gidiyorsa açıklama ve açık izin, gizlilik etiketinin SDK'larla uyumu, App Store Connect'te ve uygulama içinde gizlilik politikası linki, Google/Facebook girişinin yanında eşdeğer giriş seçeneği, yer tutucu içerik, demo hesap, gizli özellikler ve inceleme ekibinin özelliklere nasıl ulaşacağı, ekran görüntüleri, çökme, destek linki, yaş derecelendirmesi, web görünümünden ibaret olma, minimum işlevsellik, çocuk kategorisi kuralları, kullanıcı içeriği için filtreleme/şikâyet/engelleme, başkasının markası ve başka platform adları, sağlık iddiaları, şablon uygulama, açıklamadaki vaatlerin uygulamayla uyumu. Her madde için durumu (✅ ⚠️ ❌ ➖) ve ilgili dosyayı yaz, sonra inceleme notlarına yazılacak metni ve demo hesap bilgisi taslağını hazırla.
```
