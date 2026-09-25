# Yayına almadan önce: 87 benzersiz iş

<!-- sira: 1 -->
<!-- liste: yayin-oncesi -->
<!-- grup: Kontrol listeleri -->
<!-- ikon: shield -->

Yayına çıkmadan önce kontrol edilecek güvenlik, kimlik doğrulama, veri, başlık, ödeme, operasyon, tedarik zinciri, mobil, SEO, içerik, KVKK ve alan adı maddeleri.
Hukuki maddeler bilgilendirme amaçlıdır, hukuki tavsiye değildir; kendi durumun için bir hukukçuya danış.

## Sırlar & erişim (8)

1. API anahtarlarını/secret'ları koddan çıkar, env'e taşı; JWT secret'ı güçlü olsun, token kısa ömürlü olsun, algoritma sabitlensin (`alg: none` reddedilsin) <!-- id: yo-secret-koddan-cikar -->
2. `.env`'i git geçmişinden temizle ve sızan anahtarları rotate et; `/.env` ve `/.git` web'den açılmasın, staging/dev ortamları dışarıya kapalı olsun, canlıda debug modu kapalı olsun <!-- id: yo-env-gecmisten-temizle -->
3. Veritabanı kullanıcısına ve üçüncü parti API anahtarlarına sadece gereken yetkiyi ver (least privilege); uygulama ana (master) anahtarla değil, kısıtlı anahtarla çalışsın (ör. Supabase'de service_role yerine anon anahtar ve RLS, Stripe'ta restricted key) <!-- id: yo-en-az-yetki -->
4. Directory listing'i kapat <!-- id: yo-directory-listing -->
5. Varsayılan/tahmin edilebilir admin route'unu kaldır + admin'e rol tabanlı yetki koy <!-- id: yo-admin-rotasi-rol -->
6. Tüm varsayılan şifreleri değiştir (admin paneli, veritabanı, sunucu ve yönetim araçları) <!-- id: yo-varsayilan-sifreler -->
7. Canlı ortamda source map dosyalarını kapat ya da herkese açık yerden kaldır <!-- id: yo-source-map-kapali -->
8. GitHub, bulut, alan adı, ödeme ve e-posta hesaplarında ve admin panelinde iki adımlı doğrulamayı (2FA) aç; bu hesaplardan biri ele geçirilirse koddaki güvenliğin anlamı kalmaz <!-- id: yo-hesaplarda-2fa -->

## Kimlik doğrulama & oturum (11)

9. Yetki kontrolünü sunucuda tut, client'tan gelen id/role'a güvenme <!-- id: yo-yetki-sunucuda -->
10. Ownership/izin kurallarını her sorguda açıkça uygula <!-- id: yo-sahiplik-kontrolu -->
11. Şifreleri güçlü algoritmayla hash'le <!-- id: yo-sifre-hash -->
12. Çerezlere HttpOnly + Secure + SameSite ver <!-- id: yo-guvenli-cerez -->
13. CSRF token'ları ekle <!-- id: yo-csrf -->
14. Şifre değişiminde tüm oturumları sıfırla; girişte oturum kimliğini yenile, oturuma boşta kalma ve toplam süre sınırı koy, çıkışta oturumu sunucuda da geçersiz kıl <!-- id: yo-oturum-yonetimi -->
15. Şifre sıfırlama linklerini süreli ve tek kullanımlık yap <!-- id: yo-sifirlama-linki -->
16. Kullanıcı enumerasyonunu engelle (jenerik hata mesajı) <!-- id: yo-kullanici-enumerasyonu -->
17. Başarısız girişlerden sonra hesabı kilitle / kademeli gecikme <!-- id: yo-hesap-kilitleme -->
18. Tüm API'ye genel rate limit koy; login ve şifre sıfırlamaya daha sıkı limit uygula; kayıt, iletişim ve bülten gibi herkese açık formlara bot koruması koy (Cloudflare Turnstile, reCAPTCHA) <!-- id: yo-rate-limit-bot-korumasi -->
19. OTP kodlarını kısa süreli ve tek kullanımlık yap, deneme ve yeniden gönderme sayısını sınırla; SMS'i sadece hizmet verdiğin ülkelere gönder, yoksa sahte numaralara toplu SMS attırılıp fatura şişirilir (SMS pumping) <!-- id: yo-otp-sms-limit -->

## Girdi & veri (10)

20. Girdiyi sunucuda şema ile doğrula <!-- id: yo-girdi-dogrulama -->
21. Kaydetmeden önce sanitize et <!-- id: yo-sanitize -->
22. Çıktıyı XSS'e karşı escape et <!-- id: yo-xss-escape -->
23. SQL sorgularını parametrele <!-- id: yo-sql-parametre -->
24. Request body boyutunu sınırla <!-- id: yo-istek-boyutu -->
25. Dosya yüklemede tip whitelist'i + boyut sınırı; gerçek tipi dosya içeriğinden (magic byte) kontrol et, dosyaya rastgele ad ver, çalıştırılamayan bir yerde sakla <!-- id: yo-dosya-yukleme -->
26. Dosya yolu kullanıcı girdisinden oluşuyorsa normalize et, izin verilen klasörün dışına çıkmayı (`../`) engelle (path traversal) <!-- id: yo-path-traversal -->
27. Sunucunun kullanıcının verdiği URL'ye istek attığı yerlerde whitelist kullan; iç adresleri (`127.0.0.1`, `169.254.169.254`, `10.x`, `192.168.x`) engelle (SSRF) <!-- id: yo-ssrf -->
28. API yanıtında sadece gereken alanları döndür (başka kullanıcıların e-postası, telefonu ya da iç alanlar gitmesin); girdide sadece izin verilen alanları kabul et, `role`, `isAdmin`, `ownerId` gibi alanları istemciden alma (mass assignment) <!-- id: yo-fazla-alan-mass-assignment -->
29. Dosya depolamayı (S3, R2, Firebase Storage, Supabase Storage) herkese açık bırakma; kullanıcı sadece kendi dosyasına erişsin, özel dosyaları süreli imzalı linkle ver <!-- id: yo-depolama-erisimi -->

## Taşıma & başlıklar (3)

30. HTTPS zorunlu + HSTS <!-- id: yo-https-hsts -->
31. Güvenlik başlıkları (CSP, X-Frame-Options, nosniff, Referrer-Policy, Permissions-Policy) <!-- id: yo-guvenlik-basliklari -->
32. CORS'u whitelist ile kilitle <!-- id: yo-cors -->

## Entegrasyon, ödeme, AI (6)

33. Webhook imzalarını doğrula (ödeme webhook'ları dahil) <!-- id: yo-webhook-imzasi -->
34. Fiyatları sunucu tarafında belirle <!-- id: yo-fiyat-sunucuda -->
35. Prompt injection'a karşı savunma ekle <!-- id: yo-prompt-injection -->
36. Uygulamadaki AI ajanına sadece gereken araç ve veriye erişim ver; silme, ödeme, e-posta gönderme gibi geri alınamaz işlemleri kullanıcı onayına bağla <!-- id: yo-ai-ajan-yetkisi -->
37. AI kullanımına ve SMS, e-posta gibi maliyeti olan uç noktalara kullanıcı başına kota/tavan koy <!-- id: yo-maliyet-kotasi -->
38. Harcama uyarısı (billing alert) kur <!-- id: yo-harcama-uyarisi -->

## Operasyon & dayanıklılık (7)

39. Hata mesajlarını kıs (stack trace/iç detay sızdırma) <!-- id: yo-hata-mesajlari -->
40. Loglardan hassas veriyi temizle; log dosyaları ve log sayfaları herkese açık olmasın <!-- id: yo-log-hassas-veri -->
41. Güvenlik olaylarını logla (audit trail) <!-- id: yo-guvenlik-logu -->
42. Bağımlılıkları denetle (audit / otomatik güncelleme) <!-- id: yo-bagimlilik-denetimi -->
43. Otomatik yedekleme kur + geri yükleme testi yap <!-- id: yo-yedekleme -->
44. Hesap silme gerçekten silsin (kalıcı silme) <!-- id: yo-hesap-silme -->
45. Saldırgan gibi test et (pentest / düşmanca inceleme) <!-- id: yo-pentest -->

## Tedarik zinciri & CI (3)

46. Lock dosyasını (`package-lock.json`, `pnpm-lock.yaml`) commit'le, CI'da ve sunucuda lock'a sadık komutla kur (`npm ci`, `pnpm install --frozen-lockfile`); paket sürümleri kendiliğinden yükselmesin <!-- id: yo-lock-dosyasi -->
47. Paketlerin kurulum script'lerini kapat (`npm config set ignore-scripts true`, pnpm'de sadece izin verdiğin paketler); kötü amaçlı bir paket kurulurken bilgisayarında ya da CI'da kod çalıştıramasın <!-- id: yo-kurulum-scriptleri -->
48. Fork'tan gelen PR'ların kodunu secret'lara erişen iş akışında çalıştırma (GitHub Actions'ta `pull_request_target` ile PR kodunu checkout etme); CI secret'ları dışarıdan gelen koda açılmasın <!-- id: yo-fork-pr-secret -->

## Mobil uygulama (8)

49. Uygulama paketine (APK, AAB, IPA) gizli anahtar koyma; paket açılıp okunabilir, istemcide sadece herkese açık anahtarlar kalsın (ör. Supabase anon key), gizli işlemler sunucudan geçsin <!-- id: yo-mobil-pakette-anahtar -->
50. Oturum token'larını ve hassas veriyi iOS'ta Keychain'de, Android'de Keystore ile şifrelenmiş depoda sakla; AsyncStorage, SharedPreferences ya da UserDefaults'a düz metin yazma <!-- id: yo-mobil-guvenli-depolama -->
51. Android'de uygulama verisinin yedeklenmesini kapat ya da hassas dosyaları yedekten çıkar (`android:allowBackup="false"`, `dataExtractionRules`); yedekten token ve veritabanı çıkarılamasın <!-- id: yo-android-yedekleme -->
52. Firebase kullanıyorsan App Check'i aç ve zorunlu kıl (enforce); istekler sadece gerçek uygulamandan gelsin (iOS'ta App Attest, Android'de Play Integrity) <!-- id: yo-firebase-app-check -->
53. Android sürümünde kod küçültme ve karartmayı aç (R8, `isMinifyEnabled = true`); tersine mühendisliği zorlaştırır ama gizli anahtarı korumaz <!-- id: yo-android-r8 -->
54. Deep link'leri doğrula: Android App Links (`autoVerify`) ve iOS Universal Links kullan, linkten gelen parametrelere güvenme, giriş ya da ödeme gibi işlemleri sadece linkle tetikleme <!-- id: yo-deep-link -->
55. Hassas API'lerde sertifika sabitlemeyi (certificate pinning) değerlendir; yedek anahtar ve son kullanma tarihi koy, yoksa sertifika yenilenince uygulama sunucuya bağlanamaz <!-- id: yo-sertifika-sabitleme -->
56. Sadece gerçekten kullandığın izinleri iste (kamera, konum, rehber, bildirim); kullanılmayan izin saldırı yüzeyini büyütür ve mağaza incelemesinde sorun çıkarır <!-- id: yo-mobil-izinler -->

## SEO & teknik site (10)

57. Özel 404 sayfası <!-- id: yo-404-sayfasi -->
58. Benzersiz sayfa başlıkları <!-- id: yo-sayfa-basliklari -->
59. Meta description'lar <!-- id: yo-meta-description -->
60. Sosyal paylaşım görseli (OG/Twitter card) <!-- id: yo-og-gorseli -->
61. robots.txt <!-- id: yo-robots-txt -->
62. Yapısal veri / schema (local schema dahil) <!-- id: yo-yapisal-veri -->
63. Breadcrumb'lar <!-- id: yo-breadcrumb -->
64. İç linkler <!-- id: yo-ic-linkler -->
65. Görsellerde alt text <!-- id: yo-alt-text -->
66. Google Analytics <!-- id: yo-analitik -->

## İçerik & dönüşüm (10)

67. CTA'yı fold üstüne koy <!-- id: yo-cta-ust -->
68. Mobilde sticky CTA <!-- id: yo-sticky-cta -->
69. Teşekkür (thank you) sayfası <!-- id: yo-tesekkur-sayfasi -->
70. 5 soruluk SSS <!-- id: yo-sss -->
71. Vaka çalışmaları <!-- id: yo-vaka-calismalari -->
72. Gerçek kullanıcı yorumları <!-- id: yo-kullanici-yorumlari -->
73. Yanıt süresi taahhüdü <!-- id: yo-yanit-suresi-taahhudu -->
74. Harita + yol tarifi <!-- id: yo-harita-yol-tarifi -->
75. Ekip fotoğrafı <!-- id: yo-ekip-fotografi -->
76. Gizlilik politikası sayfası <!-- id: yo-gizlilik-politikasi -->

## Hukuki & KVKK (6)

77. Fontları (Google Fonts dahil) kendi sunucundan ver; ziyaretçinin IP adresi yurt dışına gitmesin (KVKK / GDPR) <!-- id: yo-yerel-fontlar -->
78. Oturum kaydı ve ısı haritası araçlarında (Clarity vb.) form alanlarını maskele, çerez onayı olmadan başlatma, aydınlatma metninde belirt <!-- id: yo-oturum-kaydi-maskeleme -->
79. Ticari e-posta ve SMS için önceden onay al, İYS'ye kayıt ol, her iletide ret (abonelikten çıkma) linki ve gönderenin kimliği olsun: tacirse ticaret unvanı ve MERSİS numarası, esnafsa adı soyadı ve T.C. kimlik numarası, ayrıca en az bir iletişim bilgisi (6563 sayılı Kanun, Ticari İletişim Yönetmeliği); ABD'ye gönderiyorsan posta adresi de şart (CAN-SPAM) <!-- id: yo-ticari-ileti -->
80. Abonelik satılıyorsa yenileme şartlarını ve iptal yolunu abone ol butonunun yanında göster, iptal abone olmak kadar kolay olsun (6502 sayılı Kanun, Mesafeli Sözleşmeler Yönetmeliği) <!-- id: yo-abonelik-sartlari -->
81. Kayıtta yaş sor ya da çocukların kaydını engelle; ABD'de 13 yaş altı çocukların verisini ebeveyn onayı olmadan toplamak COPPA ihlalidir ve ceza ihlal başınadır. Uygulama çocuklara yönelikse mağazaların çocuk kategorisi kurallarına da uy <!-- id: yo-yas-kontrolu -->
82. Kullanıcılar görsel ya da dosya yüklüyorsa telif şikâyeti yolu kur: kaldırma talebi için iletişim adresi ve süreç yaz. ABD'li kullanıcıların varsa DMCA temsilcini ABD Telif Ofisi'ne kaydet (6 $); kayıt yoksa yüklenen içerikteki telif ihlalinden sen de sorumlu tutulabilirsin <!-- id: yo-telif-sikayeti -->

## Alan adı, e-posta & indeksleme (3)

83. Uygulamayı alt alan adında yayınla (`app.alanadi.com`), tanıtım sayfaları ana alan adında kalsın (`alanadi.com`); ikisi ayrı ekiplerce birbirini bozmadan değiştirilebilsin (DNS'te `app` için CNAME kaydı) <!-- id: yo-alt-alan-adi -->
84. E-postaları ana alan adından değil ayrı alt alan adlarından gönder: uygulama e-postaları (fatura, kayıt, şifre sıfırlama) `mail.alanadi.com`, pazarlama e-postaları (bülten, kampanya) `news.alanadi.com`; her biri için SPF, DKIM ve DMARC kayıtlarını kur (ör. Resend), spam bildirimi ana alan adının itibarını düşürmesin <!-- id: yo-eposta-alt-alan -->
85. Herkese açık sayfalar için `sitemap.xml` oluştur ve Google Search Console'da Dizin oluşturma > Site haritaları bölümünden gönder <!-- id: yo-sitemap -->

## Sürüm çıkarma & geri dönüş (2)

86. Yeni sürümü canlıyı bozmadan yayına al ve sorun çıkarsa önceki sürüme dakikalar içinde dönebil (blue-green ya da sağlık kontrollü kesintisiz güncelleme; istersen önce trafiğin küçük bir kısmına aç ve hata oranını izleyerek artır: canary); geri dönüşü yayından önce bir kez dene <!-- id: yo-kesintisiz-surum -->
87. Veritabanı değişikliklerini geriye uyumlu yap (genişlet-daralt): sütunu yeniden adlandırma ya da silme yerine önce yenisini ekle, iki yapıyı da okuyan kodu çıkar, veriyi taşı, eskisini sonraki sürümde kaldır; yoksa eski sürüme dönüş veritabanında kırılır <!-- id: yo-geriye-uyumlu-sema -->
