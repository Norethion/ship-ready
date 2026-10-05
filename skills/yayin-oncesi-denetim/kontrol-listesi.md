# Yayına almadan önce: 115 benzersiz iş

<!-- sira: 1 -->
<!-- liste: yayin-oncesi -->
<!-- grup: Kontrol listeleri -->
<!-- ikon: shield -->

Yayına çıkmadan önce kontrol edilecek güvenlik, kimlik doğrulama, veri, başlık, ödeme, operasyon, tedarik zinciri, mobil, SEO, içerik, KVKK ve alan adı maddeleri.
Hukuki maddeler bilgilendirme amaçlıdır, hukuki tavsiye değildir; kendi durumun için bir hukukçuya danış.

## Sırlar & erişim (8)

1. API anahtarlarını/secret'ları koddan çıkar, env'e taşı; JWT secret'ı güçlü olsun, token kısa ömürlü olsun, algoritma sabitlensin (`alg: none` reddedilsin) <!-- id: yo-secret-koddan-cikar -->
2. `.env`'i git geçmişinden temizle ve sızan anahtarları rotate et; `/.env` ve `/.git` web'den açılmasın, staging/dev ortamları dışarıya kapalı olsun, canlıda debug modu kapalı olsun <!-- id: yo-env-gecmisten-temizle -->
3. Veritabanı kullanıcısına ve üçüncü parti API anahtarlarına sadece gereken yetkiyi ver (least privilege); uygulama ana (master) anahtarla değil, kısıtlı anahtarla çalışsın (ör. Supabase'de istemcide secret ya da service_role değil publishable ya da anon anahtar ve RLS, Stripe'ta restricted key) <!-- id: yo-en-az-yetki -->
4. Directory listing'i kapat <!-- id: yo-directory-listing -->
5. Varsayılan/tahmin edilebilir admin route'unu kaldır + admin'e rol tabanlı yetki koy <!-- id: yo-admin-rotasi-rol -->
6. Tüm varsayılan şifreleri değiştir (admin paneli, veritabanı, sunucu ve yönetim araçları) <!-- id: yo-varsayilan-sifreler -->
7. Canlı ortamda source map dosyalarını kapat ya da herkese açık yerden kaldır <!-- id: yo-source-map-kapali -->
8. GitHub, bulut, alan adı, ödeme ve e-posta hesaplarında ve admin panelinde iki adımlı doğrulamayı (2FA) aç; bu hesaplardan biri ele geçirilirse koddaki güvenliğin anlamı kalmaz <!-- id: yo-hesaplarda-2fa -->

## Kimlik doğrulama & oturum (13)

9. Yetki kontrolünü sunucuda tut, client'tan gelen id/role'a güvenme <!-- id: yo-yetki-sunucuda -->
10. Ownership/izin kurallarını her sorguda açıkça uygula <!-- id: yo-sahiplik-kontrolu -->
11. Supabase kullanıyorsan herkese açık şemadaki her tabloda RLS'i aç (panelden oluşturulan tablolarda açık gelir, SQL ya da migration ile oluşturulanlarda elle açılır) ve kuralları kullanıcıya bağla (ör. `auth.uid() = user_id`); `using (true)` kuralı tabloyu herkese açar, sadece gerçekten herkese açık veride kullan. Tabloları sadece herkese açık anahtarla sorgulayarak dene, AI her değişiklik yaptığında tekrarla ve Security Advisor'daki uyarıları (`supabase db advisors --type security`) sıfırla; UpGuard Eylül 2026'da 16 binden fazla Supabase veritabanında dışarıdan okunabilen tablo buldu. Firebase'de güvenlik kurallarını test modunda (`allow read, write: if true`) bırakma <!-- id: yo-rls-kurallari -->
12. Şifreleri güçlü algoritmayla hash'le <!-- id: yo-sifre-hash -->
13. Kayıtta zayıf ve sızmış şifreleri reddet: en az 8 karakter iste (şifre tek doğrulama yöntemiyse daha uzun), sızıntılarda görülmüş şifreleri Have I Been Pwned'in Pwned Passwords servisiyle kontrol et (şifrenin kendisi değil, karmasının ilk 5 karakteri gider); karmaşık karakter kuralı yerine uzunluk ve sızıntı kontrolü daha etkilidir (NIST SP 800-63B). Supabase Auth'un ücretli planlarında sızmış şifre koruması ayardan açılır <!-- id: yo-sifre-kurallari -->
14. Çerezlere HttpOnly + Secure + SameSite ver <!-- id: yo-guvenli-cerez -->
15. CSRF token'ları ekle <!-- id: yo-csrf -->
16. Şifre değişiminde tüm oturumları sıfırla; girişte oturum kimliğini yenile, oturuma boşta kalma ve toplam süre sınırı koy, çıkışta oturumu sunucuda da geçersiz kıl <!-- id: yo-oturum-yonetimi -->
17. Şifre sıfırlama linklerini süreli ve tek kullanımlık yap <!-- id: yo-sifirlama-linki -->
18. Kullanıcı enumerasyonunu engelle (jenerik hata mesajı) <!-- id: yo-kullanici-enumerasyonu -->
19. Başarısız girişlerden sonra hesabı kilitle / kademeli gecikme <!-- id: yo-hesap-kilitleme -->
20. Tüm API'ye genel rate limit koy; login ve şifre sıfırlamaya daha sıkı limit uygula; kayıt, iletişim ve bülten gibi herkese açık formlara bot koruması koy (Cloudflare Turnstile, reCAPTCHA) <!-- id: yo-rate-limit-bot-korumasi -->
21. OTP kodlarını kısa süreli ve tek kullanımlık yap, deneme ve yeniden gönderme sayısını sınırla; SMS'i sadece hizmet verdiğin ülkelere gönder, yoksa sahte numaralara toplu SMS attırılıp fatura şişirilir (SMS pumping) <!-- id: yo-otp-sms-limit -->

## Girdi & veri (10)

22. Girdiyi sunucuda şema ile doğrula <!-- id: yo-girdi-dogrulama -->
23. Kaydetmeden önce sanitize et <!-- id: yo-sanitize -->
24. Çıktıyı XSS'e karşı escape et <!-- id: yo-xss-escape -->
25. SQL sorgularını parametrele <!-- id: yo-sql-parametre -->
26. Request body boyutunu sınırla <!-- id: yo-istek-boyutu -->
27. Dosya yüklemede tip whitelist'i + boyut sınırı; gerçek tipi dosya içeriğinden (magic byte) kontrol et, dosyaya rastgele ad ver, çalıştırılamayan bir yerde sakla <!-- id: yo-dosya-yukleme -->
28. Dosya yolu kullanıcı girdisinden oluşuyorsa normalize et, izin verilen klasörün dışına çıkmayı (`../`) engelle (path traversal) <!-- id: yo-path-traversal -->
29. Sunucunun kullanıcının verdiği URL'ye istek attığı yerlerde (link önizleme, webhook test, URL'den avatar ya da PDF) whitelist kullan; iç adresleri (`127.0.0.1`, `169.254.169.254`, `10.x`, `192.168.x`) engelle, sadece `https`'e izin ver, yönlendirmeden sonraki son adresi de kontrol et, isteğe zaman aşımı ve yanıt boyutu sınırı koy (SSRF) <!-- id: yo-ssrf -->
30. API yanıtında sadece gereken alanları döndür (başka kullanıcıların e-postası, telefonu ya da iç alanlar gitmesin); girdide sadece izin verilen alanları kabul et, `role`, `isAdmin`, `ownerId` gibi alanları istemciden alma (mass assignment) <!-- id: yo-fazla-alan-mass-assignment -->
31. Dosya depolamayı (S3, R2, Firebase Storage, Supabase Storage) herkese açık bırakma; kullanıcı sadece kendi dosyasına erişsin, özel dosyaları süreli imzalı linkle ver; herkese açık görselleri yedeklerle, yapılandırma ve kullanıcı dosyalarıyla aynı bucket'ta tutma, erişim kaydını (access logging) aç <!-- id: yo-depolama-erisimi -->

## Taşıma & başlıklar (3)

32. HTTPS zorunlu + HSTS <!-- id: yo-https-hsts -->
33. Güvenlik başlıkları (CSP, X-Frame-Options, nosniff, Referrer-Policy, Permissions-Policy) <!-- id: yo-guvenlik-basliklari -->
34. CORS'u whitelist ile kilitle <!-- id: yo-cors -->

## Entegrasyon, ödeme, AI (15)

35. Webhook imzalarını doğrula (ödeme webhook'ları dahil) <!-- id: yo-webhook-imzasi -->
36. Fiyatları sunucu tarafında belirle <!-- id: yo-fiyat-sunucuda -->
37. Canlıya almadan önce ödeme sağlayıcısının yasaklı ve kısıtlı işler listesini oku (Stripe, iyzico, PayTR, Paddle, Lemon Squeezy): listedeki bir işi yapıyorsan hesap haber verilmeden askıya alınabilir, para aylarca tutulabilir. Paddle ve Lemon Squeezy sadece yazılım satışını kabul eder, danışmanlık gibi hizmetleri almaz <!-- id: yo-odeme-yasakli-isler -->
38. Prompt injection'a karşı savunma ekle <!-- id: yo-prompt-injection -->
39. Uygulamadaki AI ajanına sadece gereken araç ve veriye erişim ver; silme, ödeme, e-posta gönderme gibi geri alınamaz işlemleri kullanıcı onayına bağla <!-- id: yo-ai-ajan-yetkisi -->
40. AI kullanımına ve SMS, e-posta gibi maliyeti olan uç noktalara kullanıcı başına kota/tavan koy <!-- id: yo-maliyet-kotasi -->
41. Harcama uyarısı (billing alert) kur <!-- id: yo-harcama-uyarisi -->
42. AI çağrılarında değişmeyen kısmı (sistem prompt'u, araç tanımları, uzun doküman) başa koy ve prompt önbelleğini (prompt caching) aç; önbellekten okunan kısım çok daha ucuza gelir (Claude'da giriş fiyatının onda biri ya da daha azı), değişen kısım sona yazılsın; sık gelen aynı sorunun cevabını da anlamına göre önbellekten ver (semantic cache) <!-- id: yo-prompt-onbellegi -->
43. Her isteği en pahalı modele gönderme: kolay istekleri küçük model karşılasın, emin olamadığında bir üst modele aktarsın (model cascade); aktarma eşiğini kendi test setinle ayarla <!-- id: yo-model-kademesi -->
44. Modeli değiştirmeden önce yenisini gerçek isteklerin kopyasıyla arka planda çalıştır (shadow test) ve cevapları model adları gizli AI hakemlere karşılaştırt; açık farkla kazanmadıkça geçiş yapma <!-- id: yo-model-golge-testi -->
45. Kodun işleyeceği AI cevaplarını (kategori, evet/hayır, alanlar) serbest metin yerine şemalı JSON olarak al (structured outputs) ve değerleri izin verilen listeye göre doğrula <!-- id: yo-ai-semali-cikti -->
46. Belgelere dayanan AI cevaplarında (RAG) cevabın hangi belgeden geldiğini göster, belgede yoksa "bilmiyorum" dedirt; kullanıcının göremeyeceği belgeleri arama sorgusunun içinde süz, arama ve cevap kalitesini ayrı ölç <!-- id: yo-rag-kaynak-yetki -->
47. LLM ve diğer dış API çağrılarına zaman aşımı koy; 429 ve 5xx hatasında hemen tekrar deneme, `Retry-After` başlığına uy, beklemeyi her denemede artırıp rastgele kaydır, deneme sayısını sınırla ve yoğun anlarda istekleri kuyruğa al <!-- id: yo-api-yeniden-deneme -->
48. AI ajanının kayıt oluşturan işlemlerine (randevu, sipariş) idempotency key ver ki aynı mesaj iki kez gelince çift kayıt oluşmasın; "gelecek perşembe" gibi tarih ve saatleri model değil kod hesaplasın. Ajanın "yaptım" dediği işlemi araç çağrısının sonucuyla doğrula: araç hiç çağrılmadıysa ya da hata döndüyse kullanıcıya başarılı gösterme <!-- id: yo-ajan-kayit-guvencesi -->
49. AB'deki kullanıcılara AI özelliği sunuyorsan şeffaflık kurallarına uy (AB Yapay Zekâ Yasası md. 50, 2 Ağustos 2026'dan beri): kullanıcıya AI ile konuştuğunu en geç ilk etkileşimde söyle, ürettiğin görsel, ses, video ve metni makine tarafından okunur biçimde işaretle (meta veri ya da filigran), deepfake'leri etiketle. Türkiye'den hizmet vermek kapsam dışı bırakmaz; ceza 15 milyon €'ya ya da cironun %3'üne kadar. 2 Ağustos 2026'dan önce piyasaya sürülmüş üretken sistemlerde işaretleme için süre 2 Aralık 2026'da bitiyor <!-- id: yo-ai-seffaflik -->

## Operasyon & dayanıklılık (12)

50. Hata mesajlarını kıs (stack trace/iç detay sızdırma) <!-- id: yo-hata-mesajlari -->
51. Loglardan hassas veriyi temizle; log dosyaları ve log sayfaları herkese açık olmasın <!-- id: yo-log-hassas-veri -->
52. Güvenlik olaylarını logla (audit trail) <!-- id: yo-guvenlik-logu -->
53. Bağımlılıkları denetle (audit / otomatik güncelleme) <!-- id: yo-bagimlilik-denetimi -->
54. Otomatik yedekleme kur + geri yükleme testi yap <!-- id: yo-yedekleme -->
55. Hesap silme gerçekten silsin (kalıcı silme) <!-- id: yo-hesap-silme -->
56. Saldırgan gibi test et (pentest / düşmanca inceleme) <!-- id: yo-pentest -->
57. Sık okunan veriyi önbelleğe al: statik dosyalara uzun `Cache-Control` ver, herkese açık sayfaları CDN'de tut, sık sorguları Redis gibi bir önbellekte sakla; her okuma veritabanına gitmesin, veri değişince önbelleği temizle <!-- id: yo-onbellek-katmanlari -->
58. Veritabanına bağlantı havuzu (connection pooling) üzerinden bağlan: her istek yeni bağlantı açarsa birkaç düzine eşzamanlı kullanıcıda veritabanının bağlantı sınırı dolar ve uygulama durur; Supabase'de hazır havuzlayıcının (Supavisor) adresini kullan, kendi Postgres'inde PgBouncer kur. Sunucusuz fonksiyonlarda her çağrı ayrı bağlantı açtığı için bu daha da önemli <!-- id: yo-baglanti-havuzu -->
59. Yayından önce yük testi yap: k6 ya da Artillery ile 100 eşzamanlı kullanıcıyı taklit et, yavaşlayan uç noktaları ve veritabanı sınırlarını kullanıcılardan önce bul; testi canlı sisteme değil staging'e karşı çalıştır <!-- id: yo-yuk-testi -->
60. Canlıdaki hataları izle: Sentry gibi bir hata izleme aracıyla uygulama ve sunucu hatalarını cihaz, tarayıcı, işletim sistemi ve sürüm bilgisiyle topla, yeni hata çıkınca bildirim al; web'de kaynak haritalarını (source map) sadece izleme aracına yükle, kişisel veriyi (e-posta, IP, form içeriği) gönderme <!-- id: yo-hata-izleme -->
61. Sitenin ve API'nin ayakta olduğunu dışarıdan izle (uptime monitoring): birkaç dakikada bir istek atan bir izleyici kur, kesintide ve SSL sertifikasının süresi dolmadan önce bildirim al; izleyiciyi izlenen sunucudan ayrı bir yerde çalıştır (ör. kendi sunucunda Uptime Kuma) <!-- id: yo-calisirlik-izleme -->

## Tedarik zinciri & CI (3)

62. Lock dosyasını (`package-lock.json`, `pnpm-lock.yaml`) commit'le, CI'da ve sunucuda lock'a sadık komutla kur (`npm ci`, `pnpm install --frozen-lockfile`); paket sürümleri kendiliğinden yükselmesin <!-- id: yo-lock-dosyasi -->
63. Paketlerin kurulum script'lerini kapat (`npm config set ignore-scripts true`, pnpm'de sadece izin verdiğin paketler); kötü amaçlı bir paket kurulurken bilgisayarında ya da CI'da kod çalıştıramasın <!-- id: yo-kurulum-scriptleri -->
64. Fork'tan gelen PR'ların kodunu secret'lara erişen iş akışında çalıştırma (GitHub Actions'ta `pull_request_target` ile PR kodunu checkout etme); CI secret'ları dışarıdan gelen koda açılmasın <!-- id: yo-fork-pr-secret -->

## Mobil uygulama (8)

65. Uygulama paketine (APK, AAB, IPA) gizli anahtar koyma; paket açılıp okunabilir, istemcide sadece herkese açık anahtarlar kalsın (ör. Supabase anon key), gizli işlemler sunucudan geçsin <!-- id: yo-mobil-pakette-anahtar -->
66. Oturum token'larını ve hassas veriyi iOS'ta Keychain'de, Android'de Keystore ile şifrelenmiş depoda sakla; AsyncStorage, SharedPreferences ya da UserDefaults'a düz metin yazma <!-- id: yo-mobil-guvenli-depolama -->
67. Android'de uygulama verisinin yedeklenmesini kapat ya da hassas dosyaları yedekten çıkar (`android:allowBackup="false"`, `dataExtractionRules`); yedekten token ve veritabanı çıkarılamasın <!-- id: yo-android-yedekleme -->
68. Firebase kullanıyorsan App Check'i aç ve zorunlu kıl (enforce); istekler sadece gerçek uygulamandan gelsin (iOS'ta App Attest, Android'de Play Integrity) <!-- id: yo-firebase-app-check -->
69. Android sürümünde kod küçültme ve karartmayı aç (R8, `isMinifyEnabled = true`); tersine mühendisliği zorlaştırır ama gizli anahtarı korumaz <!-- id: yo-android-r8 -->
70. Deep link'leri doğrula: Android App Links (`autoVerify`) ve iOS Universal Links kullan, linkten gelen parametrelere güvenme, giriş ya da ödeme gibi işlemleri sadece linkle tetikleme <!-- id: yo-deep-link -->
71. Hassas API'lerde sertifika sabitlemeyi (certificate pinning) değerlendir; yedek anahtar ve son kullanma tarihi koy, yoksa sertifika yenilenince uygulama sunucuya bağlanamaz <!-- id: yo-sertifika-sabitleme -->
72. Sadece gerçekten kullandığın izinleri iste (kamera, konum, rehber, bildirim); kullanılmayan izin saldırı yüzeyini büyütür ve mağaza incelemesinde sorun çıkarır <!-- id: yo-mobil-izinler -->

## SEO & teknik site (13)

73. Özel 404 sayfası <!-- id: yo-404-sayfasi -->
74. Benzersiz sayfa başlıkları <!-- id: yo-sayfa-basliklari -->
75. Meta description'lar <!-- id: yo-meta-description -->
76. Her sayfada tek bir H1 olsun, alt başlıklar sırayla H2 ve H3 gitsin; başlık gibi görünen yazılar gerçekten başlık etiketiyle işaretlensin, başlık etiketi sadece yazıyı büyütmek için kullanılmasın <!-- id: yo-baslik-hiyerarsisi -->
77. Sosyal paylaşım görseli (OG/Twitter card) <!-- id: yo-og-gorseli -->
78. robots.txt <!-- id: yo-robots-txt -->
79. Sayfanın metni HTML kaynağında olsun: içerik sadece JavaScript ile sonradan geliyorsa (kaynakta boş `<div id="root">`) sayfaları sunucuda ya da derlemede üret (SSR, SSG ya da prerender); tarayıcıda "Sayfa kaynağını görüntüle" ile metni göremiyorsan arama motorları ve AI botları da eksik görebilir <!-- id: yo-icerik-kaynakta -->
80. Yapısal veriyi JSON-LD ile ekle (yerel işletmede LocalBusiness: ad, adres, telefon, çalışma saatleri); bilgiler sayfada görünenle aynı olsun. Google, AI özelliklerinde görünmek için llms.txt ya da özel bir dosya gerekmediğini söylüyor <!-- id: yo-yapisal-veri -->
81. Breadcrumb'lar <!-- id: yo-breadcrumb -->
82. İç linkler <!-- id: yo-ic-linkler -->
83. Her hizmet, ürün ya da konu için kendi adresi olan ayrı bir sayfa aç; her şey tek sayfadaysa aramada çıkacak sayfa olmaz. Google'da `site:alanadi.com` aratıp kaç sayfanın dizinde olduğuna bak <!-- id: yo-sayfa-basina-konu -->
84. Görsellerde alt text <!-- id: yo-alt-text -->
85. Google Analytics <!-- id: yo-analitik -->

## İçerik & dönüşüm (10)

86. CTA'yı fold üstüne koy <!-- id: yo-cta-ust -->
87. Mobilde sticky CTA <!-- id: yo-sticky-cta -->
88. Teşekkür (thank you) sayfası <!-- id: yo-tesekkur-sayfasi -->
89. 5 soruluk SSS <!-- id: yo-sss -->
90. Vaka çalışmaları <!-- id: yo-vaka-calismalari -->
91. Gerçek kullanıcı yorumları <!-- id: yo-kullanici-yorumlari -->
92. Yanıt süresi taahhüdü <!-- id: yo-yanit-suresi-taahhudu -->
93. Harita + yol tarifi <!-- id: yo-harita-yol-tarifi -->
94. Ekip fotoğrafı <!-- id: yo-ekip-fotografi -->
95. Gizlilik politikası sayfası <!-- id: yo-gizlilik-politikasi -->

## Hukuki & KVKK (15)

96. Fontları (Google Fonts dahil) kendi sunucundan ver; ziyaretçinin IP adresi yurt dışına gitmesin (KVKK / GDPR) <!-- id: yo-yerel-fontlar -->
97. Oturum kaydı ve ısı haritası araçlarında (Clarity vb.) form alanlarını maskele, çerez onayı olmadan başlatma, aydınlatma metninde belirt <!-- id: yo-oturum-kaydi-maskeleme -->
98. Aydınlatma metnini başka bir siteden kopyalama, uygulamanın gerçekte yaptığına göre yaz: hangi veriyi hangi amaçla topladığını ve kimlere aktardığını (analitik, e-posta, ödeme, hata izleme servisleri) eksiksiz yaz, yeni bir piksel ya da SDK eklediğinde metni güncelle; Kurul kopya metni ve yurt dışına aktarım yokken varmış gibi yazmayı hukuka aykırı sayıyor (Aydınlatma Tebliği md. 5, Kurul'un 2026/347 sayılı İlke Kararı) <!-- id: yo-aydinlatma-gercege-uygun -->
99. Aydınlatma ile açık rızayı ayrı metin ve ayrı onayla al: aydınlatma için sadece "okudum, anladım" yaz, açık rıza zorunlu olmayan ayrı bir onay kutusu olsun; "okudum, kabul ediyorum" diyen tek kutu ya da rızayı üyelik şartına bağlamak hukuka aykırı. Veriyi sözleşmenin ifası gibi başka bir hukuki sebeple işliyorsan açık rıza isteme (Kurul'un 2026/347 sayılı İlke Kararı) <!-- id: yo-acik-riza-ayri -->
100. Zorunlu olmayan çerezleri, reklam piksellerini ve takip SDK'larını onay alınmadan çalıştırma: çerez panelinde bu seçenekler kapalı gelsin, reddetmek kabul etmek kadar kolay olsun, onay kullanım koşullarına gömülmesin; IP'yi maskeleyen, siteler arası takip yapmayan ve veriyi üçüncü taraflara vermeyen birinci taraf anonim analitik onaysız kullanılabilir (KVKK Çerez Uygulamaları Hakkında Rehber, 2025) <!-- id: yo-cerez-onayi -->
101. Kişisel veri yurt dışındaki bir servise gidiyorsa (analitik, e-posta, hata izleme, bulut veritabanı) aktarımı hukuka bağla: Kurul'un ilan ettiği standart sözleşmeyi servisle imzala ve imzadan sonra 5 iş günü içinde Kurum'a bildir; sürekli aktarımlarda açık rızaya dayanılamaz, bildirim yapmamanın da ayrı cezası var (KVKK md. 9, 7499 sayılı Kanunla değişik). Google Cloud gibi bazı sağlayıcılar Türk standart sözleşmesini veri işleme ekinde sunuyor, birçok küçük servisin sözleşmesinde ise Türkiye geçmiyor; o zaman veriyi Türkiye'de ya da kendi sunucunda tutan bir alternatif düşün <!-- id: yo-yurt-disi-aktarim -->
102. Veri ihlali olursa ne yapacağını önceden yaz: kişisel veri sızdığında ihlali öğrendiğin andan itibaren en geç 72 saat içinde KVKK Kurulu'na bildir, etkilenen kişilere de en kısa sürede haber ver (KVKK md. 12/5, Kurul'un 2019/10 sayılı kararı); AB'deki kullanıcılar için GDPR'da da süre 72 saat. İhlali fark etmek için hata izleme ve güvenlik logu gerekir <!-- id: yo-veri-ihlali-bildirimi -->
103. Ticari e-posta ve SMS için önceden onay al, İYS'ye kayıt ol, her iletide ret (abonelikten çıkma) linki ve gönderenin kimliği olsun: tacirse ticaret unvanı ve MERSİS numarası, esnafsa adı soyadı ve T.C. kimlik numarası, ayrıca en az bir iletişim bilgisi (6563 sayılı Kanun, Ticari İletişim Yönetmeliği); ABD'ye gönderiyorsan posta adresi de şart (CAN-SPAM) <!-- id: yo-ticari-ileti -->
104. Abonelik satılıyorsa yenileme şartlarını ve iptal yolunu abone ol butonunun yanında göster, iptal abone olmak kadar kolay olsun (6502 sayılı Kanun, Mesafeli Sözleşmeler Yönetmeliği) <!-- id: yo-abonelik-sartlari -->
105. Kayıtta yaş sor ya da çocukların kaydını engelle; ABD'de 13 yaş altı çocukların verisini ebeveyn onayı olmadan toplamak COPPA ihlalidir ve ceza ihlal başınadır. Uygulama çocuklara yönelikse mağazaların çocuk kategorisi kurallarına da uy <!-- id: yo-yas-kontrolu -->
106. Kullanıcılar görsel ya da dosya yüklüyorsa telif şikâyeti yolu kur: kaldırma talebi için iletişim adresi ve süreç yaz. ABD'li kullanıcıların varsa DMCA temsilcini ABD Telif Ofisi'ne kaydet (6 $); kayıt yoksa yüklenen içerikteki telif ihlalinden sen de sorumlu tutulabilirsin <!-- id: yo-telif-sikayeti -->
107. Uygulama mağazası dışında (web'den) dijital ürün ya da abonelik satıyorsan vergiyi baştan kur: AB'deki tüketiciye ilk satıştan itibaren onun ülkesinin KDV'si (VAT) uygulanır, ABD'de birçok eyalet satış eşiğini geçince satış vergisi ister; bunu Paddle ya da Lemon Squeezy gibi satıcı olarak kayıtlı (merchant of record) bir ödeme sağlayıcısına bırak ya da Stripe Tax ile hesaplat <!-- id: yo-dijital-satis-vergisi -->
108. AB'deki tüketiciye dijital içerik satıyorsan 14 günlük cayma hakkı vardır; erişimi hemen veriyorsan ödeme ekranında müşterinin açık onayını ve cayma hakkını kaybettiğini kabul ettiğini al <!-- id: yo-ab-cayma-hakki -->
109. Türkiye'deki tüketiciye web'den abonelik ya da dijital içerik satıyorsan ödeme adımından hemen önce ön bilgilendirme formunu göster (satıcının adı ya da unvanı, adresi, telefonu, toplam fiyat, cayma hakkı, dijital içeriğin işlevselliği), mesafeli satış sözleşmesini onaylat ve ikisini e-posta ya da PDF gibi kalıcı bir yolla gönder; onay alınmazsa sözleşme kurulmamış sayılır. Hemen kullanılmaya başlanan dijital içerikte cayma hakkı tüketicinin onayıyla düşer (Mesafeli Sözleşmeler Yönetmeliği md. 5–8, 15) <!-- id: yo-on-bilgilendirme -->
110. Web'den satış yapıyorsan ana sayfadan doğrudan ulaşılan bir "İletişim" sayfasında künyeni ver: tacirsen ticaret unvanı, MERSİS numarası ve merkez adresi, esnafsan ad soyad ve vergi kimlik numarası; ayrıca KEP adresi, e-posta, telefon ve bağlı olduğun meslek odası (Elektronik Ticarette Hizmet Sağlayıcı ve Aracı Hizmet Sağlayıcılar Hakkında Yönetmelik, 2022, md. 5) <!-- id: yo-iletisim-kunyesi -->

## Alan adı, e-posta & indeksleme (3)

111. Uygulamayı alt alan adında yayınla (`app.alanadi.com`), tanıtım sayfaları ana alan adında kalsın (`alanadi.com`); ikisi ayrı ekiplerce birbirini bozmadan değiştirilebilsin (DNS'te `app` için CNAME kaydı) <!-- id: yo-alt-alan-adi -->
112. E-postaları ana alan adından değil ayrı alt alan adlarından gönder: uygulama e-postaları (fatura, kayıt, şifre sıfırlama) `mail.alanadi.com`, pazarlama e-postaları (bülten, kampanya) `news.alanadi.com`; her biri için SPF, DKIM ve DMARC kayıtlarını kur (ör. Resend), spam bildirimi ana alan adının itibarını düşürmesin <!-- id: yo-eposta-alt-alan -->
113. Herkese açık sayfalar için `sitemap.xml` oluştur ve Google Search Console'da Dizin oluşturma > Site haritaları bölümünden gönder <!-- id: yo-sitemap -->

## Sürüm çıkarma & geri dönüş (2)

114. Yeni sürümü canlıyı bozmadan yayına al ve sorun çıkarsa önceki sürüme dakikalar içinde dönebil (blue-green ya da sağlık kontrollü kesintisiz güncelleme; istersen önce trafiğin küçük bir kısmına aç ve hata oranını izleyerek artır: canary); geri dönüşü yayından önce bir kez dene <!-- id: yo-kesintisiz-surum -->
115. Veritabanı değişikliklerini geriye uyumlu yap (genişlet-daralt): sütunu yeniden adlandırma ya da silme yerine önce yenisini ekle, iki yapıyı da okuyan kodu çıkar, veriyi taşı, eskisini sonraki sürümde kaldır; yoksa eski sürüme dönüş veritabanında kırılır <!-- id: yo-geriye-uyumlu-sema -->
