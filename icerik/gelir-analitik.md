# Gelir & analitik

<!-- sira: 5 -->
<!-- grup: Rehberler -->
<!-- ikon: chart -->

<!-- yan-yana -->

Uygulamadan para kazanırken sık birlikte kullanılan araçlar: satın alma altyapısı, satın alma ekranı, kullanıcı analitiği ve hata izleme.
Ücretler 25.09.2026'da (Sentry 29.09.2026'da) sitelerinden alındı.

## Araçlar

| Araç | Tür | Ne işe yarar | Ücret |
|---|---|---|---|
| [RevenueCat](https://www.revenuecat.com) | Abonelik altyapısı | App Store ve Google Play satın almalarını tek yerde toplar: makbuzu doğrular, kullanıcının hangi özelliklere erişimi olduğunu tutar, aylık gelir ve abonelik iptali panelleri ve webhook'lar sunar. Satın alma ekranı, A/B testi ve web'den satış özellikleri de var. | Aylık 2.500 $ gelire kadar ücretsiz, sonrası gelirin %1'i |
| [Superwall](https://superwall.com) | Satın alma ekranı ve A/B testi | Kodsuz editörle tasarlanan, uygulamayı güncellemeden değiştirilebilen satın alma ekranları (paywall). Hangi tasarımın, fiyatın ve ekranın gösterildiği yerin daha çok sattığını A/B testiyle ölçer. Kendi abonelik altyapısı da var. iOS, Android, React Native, Flutter, Expo, Unity ve web. | Altyapısı her ölçekte ücretsiz; paywall, paywall'dan gelen aylık 10.000 $ gelire kadar ücretsiz, sonrası sadece o gelirin %1'i |
| [Mixpanel](https://mixpanel.com) | Ürün analitiği | Kullanıcının uygulamada yaptığı her işlemi kaydeder: kayıt ya da satın alma adımlarında kaç kişinin düştüğü, kullanıcıların geri gelip gelmediği, davranışa göre kullanıcı grupları. Oturum kaydı, A/B testi ve özellik açma-kapama da var. Google Analytics'ten farkı, sayfa ziyaretinden çok ürün içindeki davranışa odaklanması. | Ayda 1 milyon işleme kadar ücretsiz; veri ABD ya da AB'de tutulabiliyor |
| [Umami](https://github.com/umami-software/umami) | Web analitiği | Çerez kullanmayan, gizlilik odaklı web analitiği: trafik, kampanya, dönüşüm ve gelir tek panelde. Google Analytics'e kendi sunucunda çalışan alternatif; veri yurt dışına gitmez. | Kendi sunucunda ücretsiz (MIT, PostgreSQL ister); bulut sürümü de var |
| [OpenReplay](https://github.com/openreplay/openreplay) | Oturum kaydı | Kullanıcının oturumunu konsol ve ağ kayıtlarıyla birlikte izletir; "bende çalışmıyor" diyen kullanıcının gördüğünü görürsün. Ürün analitiği ve canlı ortak tarama da var; kendi sunucunda çalışır, veri üçüncü tarafa gitmez. | Kendi sunucunda ücretsiz (AGPL; sitene eklenen izleme kodu MIT); en az 2 vCPU ve 8 GB RAM ister |
| [Sentry](https://sentry.io) | Hata izleme | Uygulamadaki ve sunucudaki hataları cihaz, tarayıcı, işletim sistemi ve sürüm bilgisiyle tek panelde toplar, yeni hata çıkınca haber verir; kaynak haritasıyla (source map) hatanın kodda hangi satırda olduğunu gösterir. Web, React Native, Flutter, iOS ve Android SDK'ları ve oturum tekrarı var; veri ABD'de ya da AB'de tutulur (organizasyon açılırken seçilir, sonra değişmez). | Developer planı ücretsiz: tek kullanıcı, ayda 5.000 hata, 50 oturum tekrarı; Team yıllık ödemede aylık 26 $. Kendi sunucunda ücretsiz (FSL lisansı, en az 4 çekirdek ve 16 GB RAM) |

## Birlikte kullanım ve dikkat

- **Tipik düzen:** RevenueCat satın almayı yürütür, Superwall satın alma ekranını gösterip test eder, Mixpanel kullanıcının hangi adımda vazgeçtiğini gösterir.
- **Tek altyapı seç:** Superwall artık kendi abonelik altyapısıyla geliyor. RevenueCat ile ikisinden biri altyapı olur; Superwall istenirse RevenueCat'in üstünde sadece satın alma ekranı olarak da kullanılabilir.
- **Kim için:** RevenueCat ve Superwall uygulama içi aboneliği olan mobil uygulamalar içindir. Sadece web projesinde Mixpanel yeterli.
- **Türkiye'den web satışı:** RevenueCat'in web satışı Stripe ya da Paddle üzerinden çalışıyor. Stripe Türkiye'deki şirketlere açık değil (stripe.com/global listesinde yok); Paddle'ın Türkiye'den satıcı kabul edip etmediği ayrıca kontrol edilmeli.
- **Veri yurt dışına çıkmasın:** Umami ve OpenReplay kendi sunucunda çalışır; Google Analytics ya da Mixpanel yerine bunları seçersen kullanıcı verisi yurt dışına gitmez.
- **Oturum kaydı:** Mixpanel'in ya da OpenReplay'in oturum kaydında form alanlarını maskele, çerez onayı olmadan başlatma; veri yurt dışına gittiği için KVKK aydınlatma metninde belirt ([yayın öncesi {{no:yo-oturum-kaydi-maskeleme}}. madde](yayin-oncesi-maddeler.md)).
- **Hata izleme ([bu videodan](https://www.instagram.com/reel/DdwbFPOAWpP/)):** Sentry, yayından sonra hiç test etmediğin cihaz ve tarayıcılarda (ör. Instagram'ın uygulama içi tarayıcısı) çıkan hataları gösterir ([yayın öncesi {{no:yo-hata-izleme}}. madde](yayin-oncesi-maddeler.md)). Kaynak haritalarını yükledikten sonra yayındaki siteden sil (`filesToDeleteAfterUpload`), kişisel veri gönderme ayarını kapalı tut; oturum tekrarında yazı ve form alanları varsayılan olarak maskelidir.
- **AI ile takip:** RevenueCat'in resmi MCP'si abonelik ve gelir verisini Claude'a sordurur; kurulumu ve Buffer, Meta Ads gibi pazarlama MCP'leri [AI geliştirme akışı](ai-gelistirme-akisi.md) sekmesinde.
- **Abonelik ekranı:** Yenileme şartları ve iptal yolu abone ol butonunun yanında görünsün; Superwall ya da RevenueCat ile tasarlanan ekranda bu metin kalmalı ([yayın öncesi {{no:yo-abonelik-sartlari}}. madde](yayin-oncesi-maddeler.md)).
