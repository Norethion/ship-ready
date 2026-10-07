---
title: "Mobil uygulama: platform, maliyet, ölçüm ve büyüme"
description: "Mobil uygulamada mağaza incelemesi dışında kalan kararlar: platform seçimi, aylık maliyet, ölçülecek olaylar, kullanıcıda çökme sebepleri, satmayan ve…"
---

Mobil uygulamada mağaza incelemesi dışında kalan kararlar: platform seçimi, aylık maliyet, ölçülecek olaylar, kullanıcıda çökme sebepleri, satmayan ve kullanıcı tutamayan uygulamanın sebepleri, reklamsız ilk kullanıcılar ve reklam terimleri.
Listeler dijitalakcin ve kema_the_engineer hesaplarının gönderilerinden alındı (her bölümde bağlantısı var); mağaza kuralları ve araç sınırları 06.10.2026'da kendi belgelerinden doğrulandı.
Mağaza incelemesi için [App Store](/listeler/app-store/) ve [Google Play](/listeler/google-play/) listeleri, satın alma ekranı için [Paywall dönüşümü](/listeler/paywall/), servislerin ücretsiz sınırları için [Yayına alma & barındırma](/rehberler/yayina-alma-barindirma/) sekmesi.

## Platform seçimi

Swift, Kotlin, Flutter ve React Native arasında seçim için on soru; [bu videodan](https://www.instagram.com/reel/DeE2n-0Ec6c/) alındı.

| Kriter | Soru | Ne seçilir |
|---|---|---|
| Platform | Sadece iOS mu, sadece Android mi, ikisi birden mi? | Tek platformsa Swift (iOS) ya da Kotlin (Android); ikisi birdense Flutter ya da React Native ile tek kod. |
| Bildiğin dil | Hangi dili biliyorsun? | JavaScript ya da TypeScript biliyorsan React Native bir adım yakın; Flutter için Dart öğrenmek gerekir. |
| Tasarım | Uygulama her platformda birebir aynı mı görünsün? | Flutter arayüzü kendisi çizer, her yerde aynı görünür; React Native platformun kendi bileşenlerini kullanır, her platformda o platforma benzer. |
| Cihaz özellikleri | Ana ekran widget'ı, saat uygulaması ya da Live Activity gerekecek mi? | iOS'ta bunlar WidgetKit ve SwiftUI ile yazılır; Flutter'da bu kısım ayrıca Swift ya da Kotlin ile yazılır, Expo'da `expo-widgets` ile yerel kod yazmadan iOS widget'ı ve Live Activity yapılabiliyor. |
| Performans | Ağır grafik ya da oyun mu? | Yerel kod ya da Unity gibi bir oyun motoru. |
| Web | Web sürümü de lazım mı? | Flutter'ın ve Expo'nun (React Native) web desteği var ama sınırlı; web asıl ürünse ayrı bir web uygulaması düşün. |
| Hızlı güncelleme | Mağaza incelemesini beklemeden düzeltme göndermen gerekecek mi? | React Native'de EAS Update, Flutter'da Shorebird; ikisi de JavaScript ya da Dart kodunu günceller, yerel kod ve izin değişikliği yeni sürüm ister. Apple'ın kuralına göre bu yolla uygulamanın amacını değiştiremez, yeni özellik ekleyemezsin (App Review 2.5.2). |
| Paketler | İhtiyacın olan kütüphane var mı? | React Native için npm, Flutter için pub.dev'de ara; ödeme, harita ve bildirim SDK'larının resmî desteğine bak. |
| İş | Bu dille iş de arayacak mısın? | Kendi şehrindeki ilanlarda hangisinin daha çok arandığına bak; forumdaki tartışmalara değil. |
| Dokümantasyon | Resmî belgesini anlıyor musun? | Her birinin resmî belgesini bir saat oku, en rahat anladığını seç. |

## Aylık maliyet

[Bu videodaki](https://www.instagram.com/reel/DeFHyGwIzc4/) senaryo: 1.000 aktif kullanıcı, ayda 500 $ abonelik geliri, küçük işletme programlarına kayıtlı, reklam yok.
En büyük kalem araçlar değil mağaza payıdır.

| Kalem | Aylık | Not |
|---|---|---|
| Apple Developer Program | ≈ 8,25 $ | Yıllık 99 $. |
| Google Play hesabı | 0 $ | Bir kerelik 25 $. |
| Mağaza payı | 75 $ | 500 $'ın %15'i; programlara kayıt yoksa genelde %30 (150 $). Kayıt adımları [Şirket kurmadan yayın](/rehberler/sirket-kurmadan-yayin/) sekmesinde. |
| Vergi | — | Türkiye'deki satışlarda fiyatın içindeki %20 KDV'yi mağaza tahsil edip öder; Apple payını vergisiz fiyattan hesaplar ve Türkiye gelirinden ayrıca %5 dijital hizmet vergisi keser. 20/B hesabına gelen paradan banka da %15 stopaj keser. |
| Abonelik altyapısı (RevenueCat) | 0 $ | Aylık izlenen gelir 2.500 $'a kadar ücretsiz. |
| Veritabanı (Firestore ya da Supabase) | 0 $ | Firestore'da günde 50.000 okuma, Supabase'de proje başına 500 MB ücretsiz. |
| Sunucu fonksiyonları | 0 $ | Firebase Cloud Functions kullandıkça öde (Blaze) planı ister, kart gerekir; ayda 2 milyon çağrıya kadar ücretsiz. |
| Giriş (Firebase Authentication) | 0 $ | 50.000 aylık aktif kullanıcıya kadar; SMS ile giriş her mesaj için ücretli. |
| Bildirim ve çökme raporu | 0 $ | Firebase Cloud Messaging ve Crashlytics ücretsiz. |
| Analitik (PostHog) | 0 $ | Ayda 1 milyon olay ücretsiz. |
| E-posta (Resend) | 0 $ | Ayda 3.000 e-posta ücretsiz. |
| Alan adı | ≈ 1 $ | `.com` için yılda yaklaşık 10–15 $. |
| Tanıtım sitesi | 0 $ | Firebase Hosting ya da Cloudflare Pages ücretsiz; Vercel'in ücretsiz planı ticari kullanıma kapalı. |
| AI özelliği | 3–60 $ | İsteğe bağlı; kullanıma ve modele göre değişir, kullanıcı başına kota koy ([yayın öncesi 40. madde](/listeler/yayin-oncesi/#yo-maliyet-kotasi)). |
| Toplam | ≈ 84 $ | AI hariç; 75 $'ı mağaza payı. |

Öğrenciysen [GitHub Student Developer Pack](https://education.github.com/pack) birçok geliştirici aracını ücretsiz ya da indirimli açar (GitHub Pro, JetBrains IDE'leri, Azure'da 100 $ kredi, Copilot'un öğrenci planı gibi); teklifler sık değiştiği için güncel listeye paketin sayfasından bak.

## Ölçülecek olaylar

Kullanıcının nerede bıraktığını görmek için ilk günden kurulacak 20 ölçüm; [bu videodan](https://www.instagram.com/reel/DeCi_g3Alhd/) alındı.
Olay adları örnektir; PostHog, Mixpanel ya da Firebase Analytics'te aynı mantıkla kurulur.
Olay özelliklerine e-posta ya da ad gibi kişisel veri koyma; onay kuralları için [yayın öncesi 100. madde](/listeler/yayin-oncesi/#yo-cerez-onayi).

| Ölçüm | Olay ya da hesap | Neyi gösterir |
|---|---|---|
| İlk açılış | `app_opened` (ilk açılışta `first_open`) | İndirenlerin kaçının uygulamayı gerçekten açtığı. |
| Onboarding | `onboarding_step` (adım numarasıyla) | Karşılama ekranlarında hangi adımda kaç kişinin bıraktığı. |
| Kayıt | `signup_viewed`, `signup_done` | Kayıt ekranını görenlerin kaçının kaydolduğu. |
| Aha anı | Ürüne özgü olay (ilk sonuç, ilk kayıt gibi) | Kullanıcının değeri ilk gördüğü an; paywall'ı bundan sonra göster. |
| Paywall | `paywall_viewed` (hangi ekrandan açıldığıyla) | Satın alma ekranını kimin, nereden gördüğü. |
| Deneme | `trial_started` | Ücretsiz denemeyi başlatanlar. |
| Satın alma | `purchase` (plan özelliğiyle) | Hangi planın (haftalık, aylık, yıllık) satıldığı. |
| İptal ve yenileme | Mağaza sunucu bildirimlerinden ya da RevenueCat webhook'undan gelen `cancel`, `renew` | Uygulama kapalıyken olan iptal ve yenilemeler; uygulamanın içinden görülmez. |
| D1 | Ertesi gün geri dönenlerin oranı | İlk deneyimin işe yarayıp yaramadığı. |
| D7 | 7. gün geri dönenlerin oranı | Alışkanlık oluşup oluşmadığı. |
| D30 | 30. gün geri dönenlerin oranı | Uzun vadede kalanlar. |
| Yapışkanlık | Günlük aktif ÷ aylık aktif kullanıcı (DAU/MAU) | Kullanıcıların ayın kaç gününde geldiği. |
| Bildirim izni | `push_permission` (verildi ya da reddedildi) | İzni isteme anının ve metninin işe yarayıp yaramadığı. |
| Bildirim açma | `push_opened` | Bildirimlerin gerçekten açılıp açılmadığı. |
| Sürüm | Her olaya `app_version` özelliği | Hangi sürümde sorun çıktığı, yeni sürümün sayıları düşürüp düşürmediği. |
| Kaynak | Yükleme kaynağı (kampanya, mağaza araması, davet) | Kullanıcıların nereden geldiği. |
| Çökmesiz kullanıcı | Crashlytics ya da Sentry'deki crash-free users oranı | Kullanıcıların yüzde kaçının hiç çökme yaşamadığı. |
| Açılış süresi | `app_start_ms` (p50 ve p90) | Uygulamanın kaç saniyede açıldığı; yavaş cihazları p90 gösterir. |
| Özellik kullanımı | `feature_used` (özellik adıyla) | Hangi özelliklerin kullanıldığı, hangilerinin hiç açılmadığı. |
| Kimlik | Girişte `identify(kullanıcı_id)`, çıkışta `reset()` | Aynı kişinin cihazlar arasında tek kullanıcı sayılması; çıkışta sıfırlanmazsa iki kişi tek kullanıcı gibi görünür. |

## Kullanıcıda çökme sebepleri

Geliştiricinin telefonunda çalışıp kullanıcıda çöken uygulamanın 20 sebebi; [bu videodan](https://www.instagram.com/reel/Dd_-MTjDxxQ/) alındı.
Hepsi cihazda değil kodda düzeltilir; örnekler Flutter'dan, Swift ve Kotlin'de karşılıkları aynıdır.

| Sebep | Ne olur | Düzeltme |
|---|---|---|
| Tip uyuşmazlığı | Sunucu tarih gönderir, uygulama metin bekler; dönüştürürken çöker. | Gelen veriyi modele çevirirken tipini kontrol et, şemayı tek yerde tanımla. |
| Eski sürüm | Sunucuda bir alan yeniden adlandırılınca güncellememiş kullanıcının uygulaması onu bulamaz. | Alanı yeniden adlandırma, yenisini ekleyip eskisini bir süre koru ([yayın öncesi 115. madde](/listeler/yayin-oncesi/#yo-geriye-uyumlu-sema)); gerekirse zorunlu güncelleme ekranı kur. |
| Null | Boş gelebilecek alana değer varmış gibi erişilir. | Eksik olabilecek her alana varsayılan değer ver (`??`). |
| Ünlem | `!` ile "kesin dolu" denen değer bir gün boş gelir. | `!` yerine boşluk kontrolü yap, değerin neden boş olabileceğini ele al. |
| Dispose | Ekran kapandıktan sonra gelen cevapla ekranın durumu güncellenir. | Güncellemeden önce ekranın açık olduğunu kontrol et (`mounted`), dinleyicileri `dispose` içinde kapat. |
| Context | `await`'ten sonra kapanmış ekranın context'iyle gezinme yapılır. | `await`'ten sonra `context.mounted` kontrolü yap. |
| Zaman aşımı | İnternet yokken istek sonsuza kadar bekler. | Her ağ isteğine zaman aşımı, hata ekranı ve tekrar dene düğmesi koy. |
| Yakalanmayan hata | `await` edilmeyen bir Future'daki hata hiçbir yerde yakalanmaz. | Her Future'ı `await` et ya da hatasını yakala; genel hata yakalayıcıları (`FlutterError.onError`, `PlatformDispatcher.instance.onError`) çökme aracına bağla. |
| Büyük görsel | 4000 piksellik fotoğraf olduğu gibi belleğe alınır, eski telefonda bellek biter. | Görseli gösterileceği boyutta çöz (`cacheWidth`), sunucuda küçült. |
| Ana thread | Büyük JSON ana thread'de çözülür, ekran donar. | Ağır işleri arka planda yap (`compute`, isolate). |
| Arka plan | Sistem arka plandaki uygulamayı kapatır, kullanıcı döndüğünde bellekteki durum gitmiştir. | Yarım form gibi önemli durumu kaydet, açılışta geri yükle. |
| İzin reddi | Kullanıcı izni reddedince akış izin verilmiş gibi devam eder ve durur. | Reddedilme dalını yaz: açıklama göster, özelliği izinsiz çalıştır ya da ayarlara yönlendir. |
| Token | Süresi dolan oturum token'ı yenilenmez, istekler hata verir. | Token yenileme akışını kur; yenileme başarısızsa kullanıcıyı girişe yönlendir. |
| Push token | Bildirim token'ı değişir ama sunucu eskisini tutmaya devam eder. | Token yenilenince (`onTokenRefresh`) sunucuya yeniden kaydet. |
| Derin link | Linkten gelen parametre eksik ya da bozuk gelir. | Parametreyi doğrula, yoksa ana ekrana düş ([yayın öncesi 70. madde](/listeler/yayin-oncesi/#yo-deep-link)). |
| Çift satın alma | Satın alma dinleyicisi iki kez kurulur, aynı satın alma iki kez işlenir. | Açılışta tek bir dinleyici kur, satın almayı sunucuda doğrula ve bir kez işle. |
| Silinen hesap | Hesap sunucuda silinmiştir ama cihazdaki oturum açık kalır. | Açılışta oturumu sunucudan doğrula, geçersizse çıkış yap. |
| Bozuk önbellek | Eski sürümün yazdığı ya da bozulmuş önbellek her açılışta aynı yerde çöktürür. | Önbelleğe sürüm numarası koy, sürüm değişince ya da okunamayınca temizle. |
| Saat dilimi | Gece yarısı tarih bir gün kayar. | Tarihi UTC sakla, gösterirken yerel saate çevir. |
| Rapor yok | Çökme raporu olmadığı için sorunu kullanıcının yorumundan öğrenirsin. | Crashlytics ya da Sentry'yi ilk günden kur ([yayın öncesi 60. madde](/listeler/yayin-oncesi/#yo-hata-izleme)). |

## Satmıyorsa

Yayında olup satış almayan uygulamanın 20 sebebi; [bu videodan](https://www.instagram.com/reel/Dd7CiLrj1P0/) alındı.
Neredeyse hiçbiri kod değil: mağaza sayfası, fiyat ve iletişim.

| Sebep | Ne yapmalı |
|---|---|
| Bulunmuyor | İnsanların mağazada aradığı kelimeyi başlığa ve alt başlığa koy (ikisi de 30 karakter); App Store'da 100 baytlık anahtar kelime alanını da doldur, Türkçe karakterler 2 bayt sayılır, başlıktaki kelimeleri orada tekrarlama. |
| Sadece isim | Başlıkta adın yanında ne yaptığı yazsın ("Yastık: Uyku Takibi" gibi). |
| Şablon ikon | Hazır görünen ikon yerine küçük boyutta da tanınan, tek fikirli özgün bir ikon kullan. |
| İlk görsel | İlk ekran görüntüsü ayarlar ya da giriş ekranı olmasın; ürünün ana faydasını tek cümleyle göstersin. |
| Sıfır yorum | Kullanıcı bir işi bitirip değeri gördüğü anda sistemin puan isteme penceresini göster; ayrıntı [İlk kullanıcılar](#ilk-kullanıcılar) bölümünde. |
| Deneme yok | Ücretsiz deneme ekle ([Paywall 17. madde](/listeler/paywall/#pw-deneme-yok)). |
| Erken paywall | Ödeme ekranını açılışta değil değer görüldükten sonra göster ([Paywall 1. madde](/listeler/paywall/#pw-yanlis-anda-gosteriliyor)). |
| Ne sattığın belli değil | "Premium'a geç" yerine neyin açılacağını fayda olarak yaz ([Paywall 6. madde](/listeler/paywall/#pw-ozellik-yazilmis)). |
| Ülke fiyatı | Her ülkede aynı dolar fiyatını kullanma; Türkiye gibi ülkelere mağazanın yerel fiyat kademelerinden ayrı fiyat ver. |
| Yıllık yok | Yıllık plan ekle ve seçili göster ([Paywall 13. madde](/listeler/paywall/#pw-yillik-plan-secili)). |
| Bozuk ödeme | Satın almayı her sürümde test hesabıyla baştan sona dene ([Paywall 27. madde](/listeler/paywall/#pw-test-edilmiyor)). |
| Beş iş | Uygulama beş iş yapmaya çalışmasın; tek işi iyi yapsın, mağaza sayfası da o işi anlatsın. |
| Herkes | "Herkes için" değil, kimin için olduğunu seç; mağaza sayfası o kişiye konuşsun. |
| Video yok | İlk saniyelerinde ana özelliği gösteren bir önizleme videosu ekle: App Store'da 15–30 saniyelik en fazla 3 video, Google Play'de tek bir YouTube videosu (ilk 30 saniyesi sessiz oynar). |
| Güncelleme yok | Düzenli sürüm çıkar ve sürüm notu yaz; aylardır güncellenmeyen uygulama güven vermez. |
| Tek dil | Mağaza sayfasını hedef ülkelerin diline çevir; her dil ayrı aramada çıkar. |
| Rakip | Rakipten farkını tek cümleyle yaz ("Onlar veri gösterir, Yastık uyutur" gibi). |
| Ölçüm yok | Açılıştan ödemeye kadar huniyi ölç ([Ölçülecek olaylar](#ölçülecek-olaylar)). |
| Sessiz | Bırakan ya da yorum yazan kullanıcıya yaz, uygulamayı neden indirdiğini ve neden bıraktığını sor. |
| Görünmez | Uygulamayı kimse bilmiyorsa aşağıdaki [İlk kullanıcılar](#ilk-kullanıcılar) yollarından başla. |

## Kullanıcı kalmıyorsa

İndirilen ama kullanıcıyı tutamayan uygulamanın sekiz sebebi; [bu gönderiden](https://www.instagram.com/p/DeCg_SCiGq6/) alındı.
Elde tutmayı [Ölçülecek olaylar](#ölçülecek-olaylar)'daki D1, D7 ve D30 ile ölç.

| Sebep | Ne olur | Ne yapmalı |
|---|---|---|
| Alışkanlık yok | İlk kullanımdan sonra sunacak bir şey kalmaz; kullanıcı işini görüp gider. | Geri gelmek için sebep ver: ilerleme, yeni içerik, zamanında hatırlatma. |
| Kişiselleştirme yok | Uygulama kullanıcının ne yaptığını hatırlamaz, her açılışta sıfırdan başlar. | Kaldığı yeri, tercihlerini ve geçmişini hatırla. |
| Güven oluşmadan kayıp | Kullanıcı değeri görmeden bir hataya çarpar ve bildirmeden gider. | Yayından önce ilk oturumu baştan sona test et; ilk oturumdaki hata kullanıcıyı kalıcı kaybettirir. |
| Seyrek ihtiyaç | Uygulama ayda bir yaşanan bir sorunu çözer, alışkanlık oluşmaz. | Her hafta tekrarlanan bir ihtiyaca bağla; olmuyorsa geri dönüşü hatırlatmalarla planla. |
| Beklenti farkı | Kullanıcı vaat edilen şey için kaydolur, ilk deneyim onu vermez. | Mağaza sayfası ve reklam neyi vaat ediyorsa ilk ekranda onu göster. |
| Aha anı yok | Kullanıcı boş bir ekranla karşılaşır, ne yapacağını bilmez. | İlk dakikalarda değeri gösteren yönlendirmeli bir ilk adım koy: örnek içerik, tek dokunuşla ilk sonuç. |
| Özellik eskimesi | Uygulama sadece AI özellikleriyle yarışır; daha yenisi çıkınca kullanıcı gider. | Kullanıcının biriktirdiği veri, geçmiş ve kişiselleştirme gibi kopyalanması zor bir değer kur. |
| Yeniden kazanma yok | Kullanıcı sessizleşince uygulama hiçbir şey yapmaz. | Bir süre gelmeyene e-posta ya da bildirim gönder; ne zaman ve ne gönderileceğini önceden planla. |

## İlk kullanıcılar

İlk 1.000 kullanıcı için reklamsız 20 yol; [bu videodan](https://www.instagram.com/reel/DeHbXrajYZF/) alındı.

| Yol | Ne yapılır |
|---|---|
| 5 dil | Mağaza sayfasını (başlık, alt başlık, açıklama, görseller) 5 dile çevir; her dil ayrı aramada çıkar. |
| Öne çıkarma | App Store Connect'ten Apple'a öne çıkarma başvurusu (Featuring Nomination) gönder: yeni uygulama, büyük güncelleme ya da etkinlik için en az 3 hafta, mümkünse 3 ay önce. |
| Etkinlik | App Store'da uygulama içi etkinlik (In-App Event) yayınla; ürün sayfasında, aramada ve App Store'un önerilerinde ayrı kart olarak görünür. Aynı anda 10 etkinlik yayında olabilir, her biri en fazla 31 gün sürer ve başlamadan 14 gün önce tanıtılabilir. |
| Ön kayıt | Google Play'de yayından en fazla 90 gün önce ön kayıt aç; kaydolanlara yayın günü bildirim gider, isteyenin cihazına uygulama kendiliğinden kurulur, kaydolanlara ödül verilebilir. |
| Reddit | İlgili subreddit'lerde önce soruları cevapla, kurallar izin veriyorsa sonra paylaş; doğrudan reklam silinir. |
| Product Hunt | Lansman gününü hazırla (görseller, ilk yorum, kısa demo); gün Pasifik saatiyle 00:01'de başlar ve 24 saat sürer. Oy istemek kurallara aykırı, ürün sıralamadan düşürülebilir; linki paylaşıp yorum ve geri bildirim istemek serbest. |
| Yaparken paylaş | Geliştirme sürecini her gün kısa paylaşımlarla anlat. |
| Yorum → DM | Paylaşımına yorum yazanlara otomatik mesajla link gönder; Instagram profesyonel hesapta yorumdan sonraki 7 gün içinde yorumcuya tek bir özel yanıt gönderilebilir, kişi cevap verirse 24 saat içinde yazışma sürer. Resmî API'yi kullanan araçlarla kur. |
| Forum | Türkçe forumlarda konu aç; ürünü satmak yerine fikir ve geri bildirim iste. |
| Topluluk | Kitlenin olduğu niş Discord ve Telegram gruplarına katıl, önce katkı ver. |
| Mini araç | Uygulamanın işinin küçük bir parçasını bedava web aracı olarak yap; arama trafiği getirir. |
| Site | Tek sayfalık bir tanıtım sitesi kur ve temel SEO'sunu yap ([yayın öncesi SEO maddeleri](/listeler/yayin-oncesi/)). |
| AI arama | Sitene sık sorulan sorular sayfası koy; AI asistanlarının "hangi uygulama" sorularına verdiği cevaplarda çıkmana yardım eder. |
| Davet | Davet eden de edilen de kazansın (ör. ikisine birer ay ücretsiz). |
| Puan iste | Kullanıcı bir işi bitirip değeri gördüğü anda sistemin puan isteme penceresini göster; Apple bunu bir kullanıcıya 365 günde en fazla 3 kez gösterir, Google da kotayla sınırlar. Pencereyi bir düğmeye bağlama (düğme istiyorsan mağaza sayfasına götür) ve öncesinde "Beğendin mi?" diye sorma. |
| Basın | Teknoloji sitelerine üç paragraf ve bir görselden oluşan kısa bir bülten gönder: tek cümlelik başlık, ne yaptığı, neden şimdi. |
| Çapraz tanıtım | Aynı kitleye farklı iş yapan bir uygulamayla karşılıklı tanıtım yap. |
| Üniversite | Öğrenci kulüplerine ulaş, kampüste tanıtım günü yap. |
| Shorts | Aynı videoyu Reels, TikTok ve YouTube Shorts'a filigransız yükle. |
| İlk 100 | İlk 100 kullanıcıya tek tek, elle yaz; ne işe yaradığını ve neyin eksik olduğunu sor. |

## Reklam terimleri

Reklam vermeden önce bilinmesi gereken 20 terim; [bu videodan](https://www.instagram.com/reel/Dd9ZY3SCHVu/) alındı.

| Terim | Formül | Ne anlatır |
|---|---|---|
| CPM | harcama ÷ gösterim × 1000 | Bin gösterimin maliyeti. |
| CPC | harcama ÷ tıklama | Tıklama başına maliyet. |
| CTR | tıklama ÷ gösterim | Reklamı görenlerin yüzde kaçının tıkladığı. |
| CPI | harcama ÷ indirme | İndirme başına maliyet. |
| CPR | harcama ÷ sonuç | Meta'nın "sonuç başına maliyet"i; sonuç, kampanyada seçtiğin hedeftir (yükleme, kayıt, satın alma), hedef değişince sayı da başka şeyi ölçer. |
| CPT | harcama ÷ dokunma | Apple Ads'te dokunma başına maliyet. |
| TTR | dokunma ÷ gösterim | Apple Ads'te reklamı görenlerin yüzde kaçının dokunduğu. |
| CR | indirme ÷ dokunma | Apple Ads'te dokunanların yüzde kaçının indirdiği. |
| CPA | harcama ÷ satın alma | Satın alma (ya da seçilen eylem) başına maliyet. |
| CAC | tüm pazarlama harcaması ÷ yeni ödeyen kullanıcı | Bir ödeyen müşteriyi kazanmanın toplam maliyeti. |
| ARPU | gelir ÷ kullanıcı | Kullanıcı başına ortalama gelir. |
| LTV | ARPU × ortalama kalma süresi | Bir kullanıcının toplamda getireceği gelir; CAC'tan büyük olmalı. |
| ROAS | reklamdan gelen gelir ÷ reklam harcaması | 1'in altındaysa reklam para kaybettiriyor. |
| Geri dönüş süresi | CAC ÷ kullanıcı başına aylık gelir | Bir kullanıcıya harcanan paranın kaç ayda geri geldiği. |
| D1, D7, D30 | o gün geri dönen ÷ indiren | İndirenlerin 1., 7. ve 30. günde kaçının geri geldiği. |
| Öğrenme | — | Meta'da yeni ya da büyük ölçüde değiştirilmiş reklam setinin 7 günde yaklaşık 50 sonuç toplayana kadar geçtiği dönem; bu sürede sonuçlar dalgalanır, hedef kitle, kreatif ya da bütçe değişikliği dönemi yeniden başlatır. |
| ATT | — | iOS'ta uygulamalar arası takip için kullanıcıdan izin isteyen pencere; izin yoksa reklam kimliği (IDFA) sıfırlardan oluşur. |
| AdAttributionKit | — | Apple'ın kullanıcıyı tanımadan reklamın indirmeye dönüşüp dönüşmediğini ölçen çerçevesi (iOS 17.4'ten beri); ATT izni gerektirmez. Apple yeni kampanyalar için bunu öneriyor, SKAdNetwork da çalışmaya devam ediyor. |
| MMP | — | AppsFlyer, Adjust gibi ölçüm ortakları: Meta, Google ve Apple Ads'ten gelen yüklemeleri tek yerde toplar. |
| eCPM | gelir ÷ gösterim × 1000 | Uygulamana reklam koyuyorsan bin gösterimden kazandığın. |
