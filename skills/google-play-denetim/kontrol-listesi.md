# Google Play incelemesi

<!-- sira: 3 -->
<!-- liste: google-play -->
<!-- grup: Kontrol listeleri -->
<!-- ikon: play -->

Google Play'in uygulamayı reddetmesine ya da kaldırmasına en sık yol açan 24 madde ve her biri için ne yapılacağı.
Çoğu kod hatası değil; Play Console'daki formların eksik ya da gerçekle uyumsuz doldurulması.
Maddeler 25.09.2026'da Google Play politika merkezinden ve Play Console Yardım sayfalarından doğrulandı; tarih ve API seviyeleri her yıl değişir.

## Veri ve gizlilik

| # | Red sebebi | Ne yapmalı | Politika |
|---|---|---|---|
| 1 <!-- id: gp-veri-guvenligi-formu --> | Veri güvenliği formu uyumsuz | Play Console'daki Veri güvenliği (Data safety) formunu uygulamanın ve eklediğin SDK'ların gerçekte topladığı ve paylaştığı veriyle, gizlilik politikanla tutarlı doldur. Hiç veri toplamasan da formu doldurman gerekir; uyumsuzluk güncellemelerin engellenmesine ya da kaldırmaya yol açar. | [Data safety](https://support.google.com/googleplay/android-developer/answer/10787469) |
| 2 <!-- id: gp-gizlilik-politikasi --> | Gizlilik politikası yok | Veri toplamasa bile her uygulama Play Console'daki alana ve uygulamanın içine gizlilik politikası linki koymalı. Sayfa herkese açık olmalı, PDF olmamalı; geliştirici adını, iletişim bilgisini, verinin ne kadar saklanıp nasıl silindiğini içermeli. | [User Data](https://support.google.com/googleplay/android-developer/answer/10144311) |
| 3 <!-- id: gp-belirgin-aciklama-onay --> | Belirgin açıklama ve onay yok | Kullanıcının beklemeyeceği veri kullanımında (ör. arka planda toplama) izin isteğinden hemen önce uygulama içinde açıklama göster ve kullanıcı bir düğmeyle onaylasın; geri tuşu ya da kendiliğinden kapanan mesaj onay sayılmaz. | [User Data](https://support.google.com/googleplay/android-developer/answer/10144311) |
| 4 <!-- id: gp-hesap-silme --> | Hesap silme yok | Uygulamada hesap açılabiliyorsa hem uygulama içinden hesap ve veri silme yolu, hem de silme talebi için bir web sayfası olmalı (linki Veri güvenliği formundaki alana). Hesabı dondurmak ya da pasifleştirmek silme sayılmaz. | [Hesap silme](https://support.google.com/googleplay/android-developer/answer/13327111) |

## İzinler

| # | Red sebebi | Ne yapmalı | Politika |
|---|---|---|---|
| 5 <!-- id: gp-hassas-izin-beyani --> | Hassas izin beyanı yok | SMS ve arama kaydı, tüm dosyalara erişim (`MANAGE_EXTERNAL_STORAGE`), yüklü uygulamaları görme (`QUERY_ALL_PACKAGES`), erişilebilirlik API'si, fotoğraf ve video (`READ_MEDIA_*`) izinlerini sadece ana işlev gerçekten gerektiriyorsa iste ve Play Console'da beyan formunu doldur. Fotoğraf için mümkünse sistemin fotoğraf seçicisini kullan. | [Hassas izinler](https://support.google.com/googleplay/android-developer/answer/16558241) |
| 6 <!-- id: gp-arka-plan-konum --> | Arka planda konum | Arka planda konum sadece ana işlev için olabilir, reklam ya da analitik için asla. Beyan formu, video gösterimi, uygulama içi açıklama ve gizlilik politikası ister. | [Konum izinleri](https://support.google.com/googleplay/android-developer/answer/9799150) |
| 7 <!-- id: gp-on-plan-servisi --> | Ön plan servisi beyanı yok | Android 14 ve üstünü hedefliyorsan her ön plan servisi türünü App content sayfasında açıklama, kullanıcıya etkisi ve video linkiyle beyan et. Tam ekran bildirim (`USE_FULL_SCREEN_INTENT`) ve kesin alarm (`USE_EXACT_ALARM`, sadece alarm, zamanlayıcı ve takvim uygulamaları) da beyan ister. | [Ön plan servisleri](https://support.google.com/googleplay/android-developer/answer/13392821) |

## Teknik gereksinimler

| # | Red sebebi | Ne yapmalı | Politika |
|---|---|---|---|
| 8 <!-- id: gp-hedef-api-seviyesi --> | Hedef API seviyesi düşük | 31 Ağustos 2026'dan itibaren yeni uygulamalar ve güncellemeler telefon ve tablette Android 16'yı (API 36) hedeflemeli. Mevcut uygulamalar en az API 35 olmalı, yoksa yeni Android sürümlerindeki yeni kullanıcılardan gizlenir. 1 Kasım 2026'ya kadar uzatma istenebilir. | [Hedef API](https://support.google.com/googleplay/android-developer/answer/11926878) |
| 9 <!-- id: gp-16kb-sayfa --> | 16 KB sayfa boyutu desteği yok | Android 15 ve üstünü hedefleyen, native kod (NDK ya da native kütüphane içeren bir SDK) kullanan uygulamalar 64 bit cihazlarda 16 KB bellek sayfasını desteklemeli. Sadece Java/Kotlin uygulamalar zaten uyumlu. 1 Şubat 2027'den itibaren desteklemeyen güncellemeler yayınlanamaz. | [16 KB sayfa](https://developer.android.com/guide/practices/page-sizes) |
| 10 <!-- id: gp-app-bundle-64bit --> | App Bundle ya da 64 bit yok | Yeni uygulamalar Android App Bundle (AAB) olarak yüklenmeli; native kod içeren uygulamalar 64 bit sürüm de içermeli. | [App Bundle](https://developer.android.com/guide/app-bundle) |
| 11 <!-- id: gp-paket-kaydi --> | Paket adı kayıtlı değil | Android geliştirici doğrulaması kapsamında 30 Eylül 2026'dan itibaren kayıtlı olmayan Play paketleri kaldırılır. Play uygulamaların çoğunu kendisi kaydediyor; Play Console ana sayfasında kaydedilmemiş uygulama uyarısı olup olmadığına bak. | [Geliştirici doğrulaması](https://developer.android.com/developer-verification) |
| 12 <!-- id: gp-cokme --> | Çöküyor ya da çalışmıyor | Çöken, donan, yüklenmeyen ya da açılmayan uygulamalar reddedilir. Android vitals'da çökme oranını %1,09'un, ANR oranını %0,47'nin altında tut. | [İşlevsellik](https://support.google.com/googleplay/android-developer/answer/9898783) |

## Ödeme ve abonelik

| # | Red sebebi | Ne yapmalı | Politika |
|---|---|---|---|
| 13 <!-- id: gp-play-faturalandirma --> | Play Faturalandırma dışında ödeme | Dijital ürün ve abonelikleri Google Play Faturalandırma ile sat; uygulama içinde başka ödeme yöntemine yönlendiren link ya da düğme koyma. ABD'de Ekim 2025'ten beri bu zorunluluk yok; AB, Birleşik Krallık, Japonya gibi bazı ülkelerde kayıt olarak alternatif faturalandırma kullanılabiliyor. Türkiye bu ülke listelerinde yok. Fiziksel ürün ve hizmetler Play Faturalandırma kullanmaz. | [Ödemeler](https://support.google.com/googleplay/android-developer/answer/9858738) |
| 14 <!-- id: gp-abonelik-sartlari --> | Abonelik şartları belirsiz | Fiyatı, fatura dönemini, otomatik yenilemeyi, denemenin ne zaman ve kaça dönüşeceğini ve nasıl iptal edileceğini açıkça göster. Yıllık planda aylık fiyatı öne çıkarma, kapatma düğmesi görünür olsun, uygulamada kolay bir iptal yolu (ör. Play abonelik merkezine link) bulunsun. | [Abonelikler](https://support.google.com/googleplay/android-developer/answer/9900533) |

## Mağaza sayfası ve içerik

| # | Red sebebi | Ne yapmalı | Politika |
|---|---|---|---|
| 15 <!-- id: gp-yaniltici-magaza-bilgisi --> | Yanıltıcı mağaza bilgisi | Başlık en fazla 30 karakter olsun; başlıkta, ikonda ve geliştirici adında emoji, tamamı büyük harf, "#1", "En iyi", fiyat ya da promosyon olmasın. Alakasız anahtar kelime ve kaynaksız yorum kullanma; ekran görüntüleri uygulamanın gerçek halini göstersin. | [Meta veri](https://support.google.com/googleplay/android-developer/answer/9898842) |
| 16 <!-- id: gp-icerik-derecelendirmesi --> | İçerik derecelendirmesi yok | IARC içerik derecelendirme anketini doldur, içerik değişince yeniden doldur; derecelendirmesiz uygulamaya izin verilmez. | [İçerik derecelendirme](https://support.google.com/googleplay/android-developer/answer/9898843) |
| 17 <!-- id: gp-hedef-kitle-cocuklar --> | Hedef kitle ve çocuklar | Hedef yaş gruplarını beyan et. Çocuklar da hedefteyse Aileler politikasına uy: çocuklardan cihaz kimliği (reklam kimliği, IMEI vb.) gönderme, sadece onaylı reklam SDK'larını kullan, ilgiye dayalı reklam gösterme. | [Hedef kitle](https://support.google.com/googleplay/android-developer/answer/9893335) |
| 18 <!-- id: gp-kullanici-icerigi --> | Kullanıcı içeriği | Kullanıcı paylaşım yapabiliyorsa önce kullanım koşullarını kabul etsin; sürekli moderasyon, içerik ve kullanıcı şikâyeti ile engelleme olsun. Sohbet, sosyal ve flört uygulamaları çocuk güvenliği standartlarını yayınlamalı. | [Kullanıcı içeriği](https://support.google.com/googleplay/android-developer/answer/9876937) |
| 19 <!-- id: gp-taklit-fikri-mulkiyet --> | Taklit ve fikri mülkiyet | Başka bir marka ya da kurumla olmayan bir ilişkiyi ima etme, izinsiz marka ve telifli içerik kullanma. İzinle kullanıyorsan göndermeden önce Google Play'e bildir. | [Taklit](https://support.google.com/googleplay/android-developer/answer/9888374) |
| 20 <!-- id: gp-web-gorunumu --> | Sadece web görünümü, sınırlı işlev | Sahibinin izni olmadan bir sitenin web görünümünden ibaret, statik metin ya da PDF gösteren veya başka bir uygulamanın kopyası olan uygulamalar reddedilir. | [Spam ve minimum işlev](https://support.google.com/googleplay/android-developer/answer/9899034) |
| 21 <!-- id: gp-reklam-kurallari --> | Reklam kuralları | Reklam sistem ya da uygulama arayüzünü taklit etmesin; uygulama dışında, açılışta, çıkışta ya da beklenmedik anda tam ekran reklam gösterme; geçiş reklamı en geç 15 saniyede kapatılabilsin. "Reklam içerir" beyanı doğru olsun; SDK'ların uyumundan sen sorumlusun. | [Reklamlar](https://support.google.com/googleplay/android-developer/answer/9857753) |
| 22 <!-- id: gp-saglik-finans-beyanlari --> | Sağlık ve finans beyanları | Bu özellikler olmasa bile Sağlık uygulamaları ve Finansal özellikler beyan formlarını doldur. Tıbbi cihaz olmayan sağlık uygulaması bunu açıklamasında belirtmeli; sağlık ve finans uygulamaları Kuruluş hesabı ister. | [Sağlık](https://support.google.com/googleplay/android-developer/answer/16679511) |

## İnceleme hazırlığı

| # | Red sebebi | Ne yapmalı | Politika |
|---|---|---|---|
| 23 <!-- id: gp-giris-bilgisi --> | Giriş bilgisi yok | Uygulama giriş gerektiriyorsa App content > Giriş bilgileri (Sign-in details) bölümüne çalışan bir demo hesap ve gerekiyorsa tek kullanımlık şifre, QR kodu gibi talimatları yaz; eski bilgi verme. | [Play Console gereksinimleri](https://support.google.com/googleplay/android-developer/answer/10788890) |
| 24 <!-- id: gp-kapali-test --> | Kapalı test şartı | 13 Kasım 2023'ten sonra açılan kişisel geliştirici hesapları üretime çıkmadan önce en az 12 test kullanıcısıyla kesintisiz 14 günlük kapalı test yapmalı. Kuruluş hesabı D-U-N-S numarası ister; alınması 30 güne kadar sürebilir. | [Test şartı](https://support.google.com/googleplay/android-developer/answer/14151465) |

## Reddedilince

- **Nerede:** Play Console'da uygulamanın Politika durumu (Policy status) sayfasında sebebi gör ve "Appeal" ile itiraz et ([yardım sayfası](https://support.google.com/googleplay/android-developer/answer/9842754)).
- **Tek itiraz:** Her kaldırma, askıya alma ya da yaptırım için tek itiraz hakkın var; itirazlar İngilizce yazılmalı (Çince, Japonca ve Korece de kabul ediliyor).
- **Yeniden gönderme:** Sorunu düzelt ve uyumsuz sürümleri tüm test ve yayın kanallarında devre dışı bırak; eski sürüm bir kanalda kalırsa ret sürer.
- **Hesaba etkisi:** Ret hesabın durumunu etkilemez ama askıya alma bir ihlal (strike) sayılır.
- **Süre:** İnceleme normalde 7 güne kadar sürebilir.
- **İlgili sekmeler:** Abonelik ve ödeme araçları [Gelir & analitik](gelir-analitik.md) sekmesinde; hesap silme ve abonelik şartları [yayın öncesi listesinin](yayin-oncesi-maddeler.md) 51. ve 88. maddelerinde.

## Yakında gelecekler

| Tarih | Değişiklik |
|---|---|
| 27 Ocak 2027 | Arama kaydı (`READ_CALL_LOG`) telefonla hesap doğrulaması için gerekçe olmaktan çıkıyor; Android 17'yi hedefleyen uygulamalar kişilere erişimi sadece kişi seçici yetmiyorsa isteyebilecek; coğrafi çit (geofencing) ön plan servisi gerekçesi olmaktan çıkıyor. |
| 1 Şubat 2027 | 16 KB sayfa boyutunu desteklemeyen güncellemeler yayınlanamayacak. |
| Nisan 2027 | Giriş özelliği olan uygulamalar yeni cihazda girişi Restore Credentials API ile kendiliğinden geri yüklemeli. |

## Göndermeden önce kontrol prompt'u

```
Bu Android uygulamasını Google Play incelemesine göndermeden önce şu maddelere göre kontrol et: Veri güvenliği formunun uygulama ve SDK'larla uyumu, uygulama içinde ve Play Console'da gizlilik politikası, beklenmedik veri kullanımı için belirgin açıklama ve onay, uygulama içi hesap silme ve silme web sayfası, hassas izinler ve beyan formları, arka planda konum, ön plan servisi türleri, hedef API seviyesi (API 36), native kod varsa 16 KB sayfa boyutu desteği, App Bundle ve 64 bit, çökme ve ANR riskleri, dijital satışlarda Play Faturalandırma, abonelik ekranındaki şartlar ve iptal yolu, mağaza başlığı ve açıklaması, içerik derecelendirmesi, hedef kitle ve çocuklar, kullanıcı içeriği için moderasyon, marka kullanımı, web görünümünden ibaret olma, reklam kuralları, sağlık ve finans beyanları. Her madde için durumu (✅ ⚠️ ❌ ➖) ve ilgili dosyayı yaz; Play Console'da doldurulması gereken formları (Veri güvenliği, izin beyanları, giriş bilgileri) ayrıca listele.
```
