# Yayına almadan önce: 98 benzersiz iş

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

## Entegrasyon, ödeme, AI (13)

33. Webhook imzalarını doğrula (ödeme webhook'ları dahil) <!-- id: yo-webhook-imzasi -->
34. Fiyatları sunucu tarafında belirle <!-- id: yo-fiyat-sunucuda -->
35. Prompt injection'a karşı savunma ekle <!-- id: yo-prompt-injection -->
36. Uygulamadaki AI ajanına sadece gereken araç ve veriye erişim ver; silme, ödeme, e-posta gönderme gibi geri alınamaz işlemleri kullanıcı onayına bağla <!-- id: yo-ai-ajan-yetkisi -->
37. AI kullanımına ve SMS, e-posta gibi maliyeti olan uç noktalara kullanıcı başına kota/tavan koy <!-- id: yo-maliyet-kotasi -->
38. Harcama uyarısı (billing alert) kur <!-- id: yo-harcama-uyarisi -->
39. AI çağrılarında değişmeyen kısmı (sistem prompt'u, araç tanımları, uzun doküman) başa koy ve prompt önbelleğini (prompt caching) aç; önbellekten okunan kısım çok daha ucuza gelir (Claude'da giriş fiyatının onda biri ya da daha azı), değişen kısım sona yazılsın; sık gelen aynı sorunun cevabını da anlamına göre önbellekten ver (semantic cache) <!-- id: yo-prompt-onbellegi -->
40. Her isteği en pahalı modele gönderme: kolay istekleri küçük model karşılasın, emin olamadığında bir üst modele aktarsın (model cascade); aktarma eşiğini kendi test setinle ayarla <!-- id: yo-model-kademesi -->
41. Modeli değiştirmeden önce yenisini gerçek isteklerin kopyasıyla arka planda çalıştır (shadow test) ve cevapları model adları gizli AI hakemlere karşılaştırt; açık farkla kazanmadıkça geçiş yapma <!-- id: yo-model-golge-testi -->
42. Kodun işleyeceği AI cevaplarını (kategori, evet/hayır, alanlar) serbest metin yerine şemalı JSON olarak al (structured outputs) ve değerleri izin verilen listeye göre doğrula <!-- id: yo-ai-semali-cikti -->
43. Belgelere dayanan AI cevaplarında (RAG) cevabın hangi belgeden geldiğini göster, belgede yoksa "bilmiyorum" dedirt; kullanıcının göremeyeceği belgeleri arama sorgusunun içinde süz, arama ve cevap kalitesini ayrı ölç <!-- id: yo-rag-kaynak-yetki -->
44. LLM ve diğer dış API çağrılarına zaman aşımı koy; 429 ve 5xx hatasında hemen tekrar deneme, `Retry-After` başlığına uy, beklemeyi her denemede artırıp rastgele kaydır, deneme sayısını sınırla ve yoğun anlarda istekleri kuyruğa al <!-- id: yo-api-yeniden-deneme -->
45. AI ajanının kayıt oluşturan işlemlerine (randevu, sipariş) idempotency key ver ki aynı mesaj iki kez gelince çift kayıt oluşmasın; "gelecek perşembe" gibi tarih ve saatleri model değil kod hesaplasın <!-- id: yo-ajan-kayit-guvencesi -->

## Operasyon & dayanıklılık (9)

46. Hata mesajlarını kıs (stack trace/iç detay sızdırma) <!-- id: yo-hata-mesajlari -->
47. Loglardan hassas veriyi temizle; log dosyaları ve log sayfaları herkese açık olmasın <!-- id: yo-log-hassas-veri -->
48. Güvenlik olaylarını logla (audit trail) <!-- id: yo-guvenlik-logu -->
49. Bağımlılıkları denetle (audit / otomatik güncelleme) <!-- id: yo-bagimlilik-denetimi -->
50. Otomatik yedekleme kur + geri yükleme testi yap <!-- id: yo-yedekleme -->
51. Hesap silme gerçekten silsin (kalıcı silme) <!-- id: yo-hesap-silme -->
52. Saldırgan gibi test et (pentest / düşmanca inceleme) <!-- id: yo-pentest -->
53. Sık okunan veriyi önbelleğe al: statik dosyalara uzun `Cache-Control` ver, herkese açık sayfaları CDN'de tut, sık sorguları Redis gibi bir önbellekte sakla; her okuma veritabanına gitmesin, veri değişince önbelleği temizle <!-- id: yo-onbellek-katmanlari -->
54. Canlıdaki hataları izle: Sentry gibi bir hata izleme aracıyla uygulama ve sunucu hatalarını cihaz, tarayıcı, işletim sistemi ve sürüm bilgisiyle topla, yeni hata çıkınca bildirim al; web'de kaynak haritalarını (source map) sadece izleme aracına yükle, kişisel veriyi (e-posta, IP, form içeriği) gönderme <!-- id: yo-hata-izleme -->

## Tedarik zinciri & CI (3)

55. Lock dosyasını (`package-lock.json`, `pnpm-lock.yaml`) commit'le, CI'da ve sunucuda lock'a sadık komutla kur (`npm ci`, `pnpm install --frozen-lockfile`); paket sürümleri kendiliğinden yükselmesin <!-- id: yo-lock-dosyasi -->
56. Paketlerin kurulum script'lerini kapat (`npm config set ignore-scripts true`, pnpm'de sadece izin verdiğin paketler); kötü amaçlı bir paket kurulurken bilgisayarında ya da CI'da kod çalıştıramasın <!-- id: yo-kurulum-scriptleri -->
57. Fork'tan gelen PR'ların kodunu secret'lara erişen iş akışında çalıştırma (GitHub Actions'ta `pull_request_target` ile PR kodunu checkout etme); CI secret'ları dışarıdan gelen koda açılmasın <!-- id: yo-fork-pr-secret -->

## Mobil uygulama (8)

58. Uygulama paketine (APK, AAB, IPA) gizli anahtar koyma; paket açılıp okunabilir, istemcide sadece herkese açık anahtarlar kalsın (ör. Supabase anon key), gizli işlemler sunucudan geçsin <!-- id: yo-mobil-pakette-anahtar -->
59. Oturum token'larını ve hassas veriyi iOS'ta Keychain'de, Android'de Keystore ile şifrelenmiş depoda sakla; AsyncStorage, SharedPreferences ya da UserDefaults'a düz metin yazma <!-- id: yo-mobil-guvenli-depolama -->
60. Android'de uygulama verisinin yedeklenmesini kapat ya da hassas dosyaları yedekten çıkar (`android:allowBackup="false"`, `dataExtractionRules`); yedekten token ve veritabanı çıkarılamasın <!-- id: yo-android-yedekleme -->
61. Firebase kullanıyorsan App Check'i aç ve zorunlu kıl (enforce); istekler sadece gerçek uygulamandan gelsin (iOS'ta App Attest, Android'de Play Integrity) <!-- id: yo-firebase-app-check -->
62. Android sürümünde kod küçültme ve karartmayı aç (R8, `isMinifyEnabled = true`); tersine mühendisliği zorlaştırır ama gizli anahtarı korumaz <!-- id: yo-android-r8 -->
63. Deep link'leri doğrula: Android App Links (`autoVerify`) ve iOS Universal Links kullan, linkten gelen parametrelere güvenme, giriş ya da ödeme gibi işlemleri sadece linkle tetikleme <!-- id: yo-deep-link -->
64. Hassas API'lerde sertifika sabitlemeyi (certificate pinning) değerlendir; yedek anahtar ve son kullanma tarihi koy, yoksa sertifika yenilenince uygulama sunucuya bağlanamaz <!-- id: yo-sertifika-sabitleme -->
65. Sadece gerçekten kullandığın izinleri iste (kamera, konum, rehber, bildirim); kullanılmayan izin saldırı yüzeyini büyütür ve mağaza incelemesinde sorun çıkarır <!-- id: yo-mobil-izinler -->

## SEO & teknik site (10)

66. Özel 404 sayfası <!-- id: yo-404-sayfasi -->
67. Benzersiz sayfa başlıkları <!-- id: yo-sayfa-basliklari -->
68. Meta description'lar <!-- id: yo-meta-description -->
69. Sosyal paylaşım görseli (OG/Twitter card) <!-- id: yo-og-gorseli -->
70. robots.txt <!-- id: yo-robots-txt -->
71. Yapısal veri / schema (local schema dahil) <!-- id: yo-yapisal-veri -->
72. Breadcrumb'lar <!-- id: yo-breadcrumb -->
73. İç linkler <!-- id: yo-ic-linkler -->
74. Görsellerde alt text <!-- id: yo-alt-text -->
75. Google Analytics <!-- id: yo-analitik -->

## İçerik & dönüşüm (10)

76. CTA'yı fold üstüne koy <!-- id: yo-cta-ust -->
77. Mobilde sticky CTA <!-- id: yo-sticky-cta -->
78. Teşekkür (thank you) sayfası <!-- id: yo-tesekkur-sayfasi -->
79. 5 soruluk SSS <!-- id: yo-sss -->
80. Vaka çalışmaları <!-- id: yo-vaka-calismalari -->
81. Gerçek kullanıcı yorumları <!-- id: yo-kullanici-yorumlari -->
82. Yanıt süresi taahhüdü <!-- id: yo-yanit-suresi-taahhudu -->
83. Harita + yol tarifi <!-- id: yo-harita-yol-tarifi -->
84. Ekip fotoğrafı <!-- id: yo-ekip-fotografi -->
85. Gizlilik politikası sayfası <!-- id: yo-gizlilik-politikasi -->

## Hukuki & KVKK (8)

86. Fontları (Google Fonts dahil) kendi sunucundan ver; ziyaretçinin IP adresi yurt dışına gitmesin (KVKK / GDPR) <!-- id: yo-yerel-fontlar -->
87. Oturum kaydı ve ısı haritası araçlarında (Clarity vb.) form alanlarını maskele, çerez onayı olmadan başlatma, aydınlatma metninde belirt <!-- id: yo-oturum-kaydi-maskeleme -->
88. Ticari e-posta ve SMS için önceden onay al, İYS'ye kayıt ol, her iletide ret (abonelikten çıkma) linki ve gönderenin kimliği olsun: tacirse ticaret unvanı ve MERSİS numarası, esnafsa adı soyadı ve T.C. kimlik numarası, ayrıca en az bir iletişim bilgisi (6563 sayılı Kanun, Ticari İletişim Yönetmeliği); ABD'ye gönderiyorsan posta adresi de şart (CAN-SPAM) <!-- id: yo-ticari-ileti -->
89. Abonelik satılıyorsa yenileme şartlarını ve iptal yolunu abone ol butonunun yanında göster, iptal abone olmak kadar kolay olsun (6502 sayılı Kanun, Mesafeli Sözleşmeler Yönetmeliği) <!-- id: yo-abonelik-sartlari -->
90. Kayıtta yaş sor ya da çocukların kaydını engelle; ABD'de 13 yaş altı çocukların verisini ebeveyn onayı olmadan toplamak COPPA ihlalidir ve ceza ihlal başınadır. Uygulama çocuklara yönelikse mağazaların çocuk kategorisi kurallarına da uy <!-- id: yo-yas-kontrolu -->
91. Kullanıcılar görsel ya da dosya yüklüyorsa telif şikâyeti yolu kur: kaldırma talebi için iletişim adresi ve süreç yaz. ABD'li kullanıcıların varsa DMCA temsilcini ABD Telif Ofisi'ne kaydet (6 $); kayıt yoksa yüklenen içerikteki telif ihlalinden sen de sorumlu tutulabilirsin <!-- id: yo-telif-sikayeti -->
92. Uygulama mağazası dışında (web'den) dijital ürün ya da abonelik satıyorsan vergiyi baştan kur: AB'deki tüketiciye ilk satıştan itibaren onun ülkesinin KDV'si (VAT) uygulanır, ABD'de birçok eyalet satış eşiğini geçince satış vergisi ister; bunu Paddle ya da Lemon Squeezy gibi satıcı olarak kayıtlı (merchant of record) bir ödeme sağlayıcısına bırak ya da Stripe Tax ile hesaplat <!-- id: yo-dijital-satis-vergisi -->
93. AB'deki tüketiciye dijital içerik satıyorsan 14 günlük cayma hakkı vardır; erişimi hemen veriyorsan ödeme ekranında müşterinin açık onayını ve cayma hakkını kaybettiğini kabul ettiğini al <!-- id: yo-ab-cayma-hakki -->

## Alan adı, e-posta & indeksleme (3)

94. Uygulamayı alt alan adında yayınla (`app.alanadi.com`), tanıtım sayfaları ana alan adında kalsın (`alanadi.com`); ikisi ayrı ekiplerce birbirini bozmadan değiştirilebilsin (DNS'te `app` için CNAME kaydı) <!-- id: yo-alt-alan-adi -->
95. E-postaları ana alan adından değil ayrı alt alan adlarından gönder: uygulama e-postaları (fatura, kayıt, şifre sıfırlama) `mail.alanadi.com`, pazarlama e-postaları (bülten, kampanya) `news.alanadi.com`; her biri için SPF, DKIM ve DMARC kayıtlarını kur (ör. Resend), spam bildirimi ana alan adının itibarını düşürmesin <!-- id: yo-eposta-alt-alan -->
96. Herkese açık sayfalar için `sitemap.xml` oluştur ve Google Search Console'da Dizin oluşturma > Site haritaları bölümünden gönder <!-- id: yo-sitemap -->

## Sürüm çıkarma & geri dönüş (2)

97. Yeni sürümü canlıyı bozmadan yayına al ve sorun çıkarsa önceki sürüme dakikalar içinde dönebil (blue-green ya da sağlık kontrollü kesintisiz güncelleme; istersen önce trafiğin küçük bir kısmına aç ve hata oranını izleyerek artır: canary); geri dönüşü yayından önce bir kez dene <!-- id: yo-kesintisiz-surum -->
98. Veritabanı değişikliklerini geriye uyumlu yap (genişlet-daralt): sütunu yeniden adlandırma ya da silme yerine önce yenisini ekle, iki yapıyı da okuyan kodu çıkar, veriyi taşı, eskisini sonraki sürümde kaldır; yoksa eski sürüme dönüş veritabanında kırılır <!-- id: yo-geriye-uyumlu-sema -->
