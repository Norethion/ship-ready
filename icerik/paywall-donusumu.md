# Paywall dönüşümü

<!-- sira: 4 -->
<!-- liste: paywall -->
<!-- grup: Kontrol listeleri -->
<!-- ikon: card -->

Satın alma ekranı (paywall) az satıyorsa en sık 27 sebep ve her biri için ne yapılacağı.
Liste bir videodaki 27 maddelik listeden alındı; videodaki "hepsi ölçüldü" iddiası ve etki oranları doğrulanmadı, her maddeyi kendi uygulamanda A/B testiyle dene.
Mağaza kuralına dokunan maddeler (fiyatın gösterimi, deneme süresi, şartlar, geri yükleme) Apple'ın [abonelik sayfasından](https://developer.apple.com/app-store/subscriptions/) doğrulandı ve [App Store incelemesi](app-store-incelemesi.md) sekmesine bağlandı.
Paywall'ı kodsuz değiştirip test etmek için Superwall ya da RevenueCat [Gelir & analitik](gelir-analitik.md) sekmesinde.

## Zamanlama ve akış

| # | Sebep | Ne yapmalı |
|---|---|---|
| 1 <!-- id: pw-yanlis-anda-gosteriliyor --> | Yanlış anda gösteriliyor | Paywall'ı kullanıcı değeri gördüğü anda göster: ilk sonucu aldıktan ya da bir işi tamamladıktan sonra; uygulama açılır açılmaz değil. |
| 2 <!-- id: pw-tek-ekrana-sikistirilmis --> | Tek ekrana sıkıştırılmış | Karşılamayı (onboarding) birkaç kısa adıma böl, paywall son adım olsun; kullanıcı önce ne kazanacağını görsün. |
| 3 <!-- id: pw-tek-paywall --> | Tek paywall var | Farklı yerler ve kullanıcılar için birden fazla paywall kur ve A/B testiyle karşılaştır. |
| 4 <!-- id: pw-gec-yukleniyor --> | Geç yükleniyor | Ürün ve fiyat bilgisini paywall açılmadan önce yükle; dönen yükleme göstergesi kullanıcı kaybettirir. |

## İçerik ve tasarım

| # | Sebep | Ne yapmalı |
|---|---|---|
| 5 <!-- id: pw-karsilastirma-tablosu --> | Karşılaştırma tablosu | Ücretsiz ve ücretli özellik tablosu yerine 3–4 kısa fayda maddesi yaz. |
| 6 <!-- id: pw-ozellik-yazilmis --> | Özellik yazılmış | "Sınırsız proje" gibi özellik yerine kullanıcının elde edeceği sonucu yaz. |
| 7 <!-- id: pw-baslik-baglamdan-kopuk --> | Başlık bağlamdan kopuk | Paywall'ı açan özelliğe göre başlığı değiştir; kullanıcı neye dokunduysa başlık onu anlatsın. |
| 8 <!-- id: pw-dugme-metni-sert --> | Düğme metni sert | "Satın al" yerine "Ücretsiz dene" ya da "Devam et" gibi daha yumuşak bir metin kullan; deneme varsa düğme bunu söylesin. |
| 9 <!-- id: pw-dugme-kayboluyor --> | Düğme kayboluyor | Satın alma düğmesi sayfa kaydırılınca da ekranın altında sabit dursun. |
| 10 <!-- id: pw-kalabalik --> | Kalabalık | Tek odak, az metin, tek ana düğme; dikkat dağıtan link ve animasyonları çıkar. |
| 11 <!-- id: pw-cevrilmemis --> | Çevrilmemiş | Paywall metnini kullanıcının dilinde göster; uygulama çevrilip paywall İngilizce kalmasın. |

## Fiyat ve planlar

| # | Sebep | Ne yapmalı |
|---|---|---|
| 12 <!-- id: pw-fiyat-ilk-ekranda --> | Fiyat ilk ekranda değil | Fiyat ve süre ilk ekranda, düğmenin yakınında görünsün; kaydırma ya da ikinci ekran gerektirmesin ([App Store {{no:as-fiyat-bilgisi}}. madde](app-store-incelemesi.md)). |
| 13 <!-- id: pw-yillik-plan-secili --> | Yıllık plan seçili değil | Yıllık planı varsayılan olarak seçili getir ve aylığa göre tasarrufu yaz. |
| 14 <!-- id: pw-yillik-fiyat-buyuk --> | Yıllık fiyat büyük görünüyor | Yıllık fiyatın yanında haftalık ya da aylık karşılığını göster; ama Apple tahsil edilecek tutarın en belirgin fiyat olmasını istiyor, bölünmüş fiyat daha küçük ve ikinci planda kalmalı. |
| 15 <!-- id: pw-fazla-plan --> | Çok fazla plan | En fazla üç plan göster; seçenek arttıkça karar zorlaşır. |
| 16 <!-- id: pw-teklif-yok --> | Teklif yok | Giriş indirimi ya da ilk ay indirimi gibi bir teklif sun (App Store tanıtım teklifi, Google Play giriş fiyatı). |

## Deneme süresi

| # | Sebep | Ne yapmalı |
|---|---|---|
| 17 <!-- id: pw-deneme-yok --> | Deneme yok | Ücretsiz deneme sun; deneme varsa süresini ve bitince alınacak ücreti açıkça yaz (Apple bunu istiyor). |
| 18 <!-- id: pw-deneme-kisa --> | Deneme kısa | Ürünün değeri birkaç günde anlaşılmıyorsa denemeyi uzat ve farkı ölç. |
| 19 <!-- id: pw-deneme-takvimi --> | Ne olacağı belirsiz | Deneme takvimini göster: bugün başlar, bitmeden önce hatırlatılır, şu gün ücret alınır. |
| 20 <!-- id: pw-ucret-hatirlatma --> | Ücret sürpriz oluyor | Deneme bitmeden önce bildirimle hatırlat; iade ve şikâyet azalır, güven artar. |

## Güven ve teknik

| # | Sebep | Ne yapmalı |
|---|---|---|
| 21 <!-- id: pw-sosyal-kanit-asagida --> | Sosyal kanıt aşağıda | Puanı ve kullanıcı yorumlarını paywall'ın üst kısmına koy. |
| 22 <!-- id: pw-kapatma-dugmesi-gizli --> | Kapatma düğmesi gizli | Kapatma düğmesini gizleme ya da geciktirme; kullanıcı kandırıldığını hisseder. |
| 23 <!-- id: pw-sartlar-geri-yukleme --> | Şartlar ve geri yükleme yok | Kullanım Koşulları ve Gizlilik Politikası linkleri ile "Satın almaları geri yükle" düğmesi paywall'da olsun; App Store'da zorunlu ([App Store {{no:as-paywall-linkleri}} ve {{no:as-geri-yukleme}}. maddeler](app-store-incelemesi.md)). |
| 24 <!-- id: pw-bos-ekran --> | Boş ekran | Ürünler mağazadan yüklenemezse boş paywall gösterme; hata mesajı ve "Tekrar dene" düğmesi göster. İnceleme ekibi satın alma ekranını boş görürse uygulamayı reddeder. |
| 25 <!-- id: pw-fiyat-koda-yazilmis --> | Fiyat koda yazılmış | Fiyatı sabit yazma; StoreKit ya da Google Play Billing'den kullanıcının ülkesine ve para birimine göre çek. |
| 26 <!-- id: pw-kapatan-kaybediliyor --> | Kapatan kaybediliyor | Paywall'ı kapatan kullanıcıya daha sonra indirimli bir teklif göster. |
| 27 <!-- id: pw-test-edilmiyor --> | Test edilmiyor | Satın almayı ayda bir test hesabıyla (sandbox) baştan sona dene; mağaza, SDK ya da ürün ayarı değişince paywall sessizce bozulabilir. |

## Kontrol prompt'u

```
Bu uygulamanın satın alma ekranını (paywall) şu 27 maddeye göre kontrol et: gösterildiği an, onboarding adımları, birden fazla paywall ve A/B testi, ürünlerin önceden yüklenmesi, karşılaştırma tablosu, fayda odaklı metin, bağlama göre başlık, düğme metni, sabit düğme, sadelik, çeviri, fiyatın ilk ekranda görünmesi, yıllık planın seçili gelmesi, haftalık karşılık ve tahsil edilecek tutarın en belirgin fiyat olması, plan sayısı, teklif, ücretsiz deneme ve açıklaması, deneme süresi, deneme takvimi, ücret öncesi hatırlatma, puan ve yorumların yeri, kapatma düğmesi, şartlar ve geri yükleme, ürün yüklenemezse boş ekran, fiyatın mağazadan çekilmesi, kapatan kullanıcıya teklif, satın alma testi. Her madde için durumu (✅ ⚠️ ❌ ➖) ve ilgili dosyayı yaz, sonra en çok etki edeceğini düşündüğün 3 değişikliği öner.
```
