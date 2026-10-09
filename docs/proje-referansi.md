# ship-ready proje referansı

Bu belge [depo talimatlarındaki](../AGENTS.md) içerik, katalog, rapor ve site davranışı ayrıntılarını açıklar.

## Kaynak değerlendirme

Kullanıcının getirdiği kontrol işi ilgili kontrol listesine, GitHub deposu `veri/repolar.json` kataloğuna, site veya araç ise ilgili rehbere eklenir.
UI/UX rehberinde projeye kurulan ya da kodu kopyalanan şey `Kütüphaneler`, tarayıcıda kullanılan araç `Siteler` tablosuna girer; iki tabloda da satırlar `Tür` sütununa göre gruplu durur.
Geliştirmeyle ilgisi olmayan genel web siteleri (dosya araçları, alternatif bulma, fatura) `icerik/gunluk-siteler.md` rehberine eklenir.
Mobil uygulamada platform, maliyet, ölçüm, çökme ve büyüme konuları `icerik/mobil-uygulama.md`, Türkiye'de şirketsiz yayın, 20/B ve mağaza hesabı konuları `icerik/sirket-kurmadan-yayin.md` rehberine eklenir.
Repo kataloğu kullanıcının GitHub yıldızlarına bağlı değildir: yıldızlar çekilmez, repo yıldızlanmaz.
Bilgiler kaynağından doğrulanır; videodaki iddia aynen alınmaz.
Instagram videosu sadece açıklama metninden değerlendirilmez, tamamı izlenir: yt-dlp ile ses ve görüntü indirilir, ses faster-whisper ile zaman damgalı yazıya dökülür, görüntüden 2 saniyede bir kare alınıp ekrandaki yazılar okunur.
Kaydırmalı gönderilerde her slayt `?img_index=N` ile tek tek açılır.
Arayüz ve etkileşim gönderilerinden video karesi ya da ekran görüntüsü saklanmaz; tasarımın bizim yazdığımız çalışan hâli canlı örnek olarak eklenir (aşağıda [Canlı örnekler](#canlı-örnekler)).
Bu araçlar sisteme değil, geçici bir Python ortamına (venv) kurulur.
Proje sadece Türkçedir.

## Üretim ve yerel sayfa

- `site/` bir Astro Starlight projesidir ve iki derlemesi vardır:
  - Herkese açık derleme: `site/` klasöründe `npm run build`, çıktı `site/dist/`; raporlar girmez ve bu depoda canlı yayın tanımlı değildir.
  - Yerel sayfa: `guncelle.py` her çalıştığında `SHIP_YEREL=1` ile derler, çıktı `sayfa/`.
  Raporlar (`/raporlar/`), Genel bakış'ta Takip bölümü, raporu ship-ready'ye kaydettiren denetim prompt'u ve çevrimdışı arama sadece burada vardır.
  `site/yerel-derleme.mjs` yerel derlemeyi dosyadan açılır yapar: adresleri göreli yapar, modül betiklerini sayfanın içine alır.
  Pagefind sunucusuz çalışmadığı için arama `YerelArama.astro` ile yapılır.
- `python uygulama/guncelle.py` (içinde `uygulama/site_uret.py`) şunları çekirdekten üretir ve bunlar elle düzenlenmez: `site/src/content/docs/` (sayfalar), `site/src/data/katalog.json` ve `sidebar.json`, `site/public/katalog.json`, `llms.txt` (sayfalar ve kategoriye göre dizilmiş repolar) ve `llms-full.txt` (bütün içerik tek dosyada, maddeler kimlikleriyle; AI'lar için), `site/src/yerel/` (yerel sayfanın raporları, raporlu kenar menüsü ve arama dizini; `.gitignore`'da, herkese açık derleme okumaz).
- Elle düzenlenenler: `site/src/components/` (Madde, DenetimPrompt, Kart, Kartlar, RepoKatalog, PromptDugme, UstCubuk, SayfaCercevesi, AltBilgi, TemaSecici, SayfaIcerigi, AnaSayfa, Simge, RaporOzeti, YerelTakip, YerelArama), `site/src/pages/raporlar/`, `site/src/yerel.ts`, `site/src/arama.ts` (iki aramanın ortak eşleştirme kuralları: dolgu kelimeleri, kökten eşleşme), `site/src/content.config.ts`, `site/src/content/i18n/tr.json`, `site/src/styles/ship.css`, `site/astro.config.mjs`, `site/yerel-derleme.mjs`, `site/public/ornekler/` (rehber kartlarındaki canlı örnekler).
  Sadece yerel sayfada olacak bir şey `src/yerel.ts`'deki `YEREL` ile koşullanır; kişisel veri herkese açık derlemeye girmez.
## Site davranışı

- Site üst çubuğu `UstCubuk.astro` ile Starlight `Header` yerine geçer; kontrol listeleri, rehberler ve repo kataloğu bağlantıları her sayfada görünür, rapor bağlantısı yalnızca yerel derlemede eklenir.
- `SayfaCercevesi.astro` Starlight `PageFrame` yerine geçer ve sol kenar menüyü kaldırır; `AltBilgi.astro` alt bilgiyi, `TemaSecici.astro` açık/koyu tema düğmesini sağlar.
- Tema seçimi Starlight'ın `starlight-theme` anahtarında saklanır; kayıt yoksa koyu tema kullanılır.
- `SayfaIcerigi.astro` sağdaki Starlight sayfa içeriği menüsünü sarar ve sayfanın dibine inilince son başlığı seçer.
- Genel bakış `AnaSayfa.astro` ile katalog verisinden üretilir; liste ve madde sayıları, rehberler ile en son eklenen üç repo veri değiştikçe güncellenir.
- Kontrol listesinde işaretlenen maddeler `ship-ready-checks` anahtarıyla yalnızca tarayıcıda saklanır ve ana sayfadaki ilerleme bu kayıttan okunur.
- Ana sayfa araması herkese açık derlemede Starlight Pagefind penceresini, yerel derlemede `YerelArama.astro` penceresini açar.
- Adresler: kontrol listeleri `/listeler/<liste>/`, rehberler `/rehberler/<md adı>/`, repo kataloğu `/repolar/` (`#ara=<repo>` aramayla, `#dikkat` Dikkat süzgeciyle açılır), yerel sayfada raporlar `/raporlar/` ve `/raporlar/<proje>/<dosya adı>/`; her maddenin bağlantısı `#<kimlik>`. `{{no:kimlik}}` içeren linkler doğrudan o maddeye gider.
- Kontrol listelerinde maddeler kimlikli kart olur, numaralı listede her bölüme denetim prompt'u eklenir; `<!-- yan-yana -->` rehberlerinde tablolar karta dönüşür (prompt düğmesi ilk sütun başlığına göre: `site_uret.py` içindeki `CARD_PROMPTS`), diğer rehberler Markdown olarak kalır.
- Siteye sadece doğrulanmış, Türkçe açıklaması ve kurulum yeri olan repolar girer; raporlar girmez.
- Herkese açık siteyi görmek için `site/` klasöründe `npm run build` ve `npm run preview` (ya da `npm run dev`).
  Paketler sadece `site/node_modules`'a kurulur; yerel sayfanın derlenmesi için Node.js ve bu paketler gerekir.

## Katalog ve klasörler

- `icerik/*.md`: yan menüde ve Genel bakış'ta gösterilir.
  Başlığı ilk `#` satırıdır (menüde `:` öncesi kısmı), Genel bakış'taki açıklaması başlıktan sonraki ilk paragraftır.
  Başlığın altındaki satırlar:
  - `<!-- sira: N -->` menüdeki sırası,
  - `<!-- liste: kimlik -->` md'nin bir kontrol listesi olduğunu ve kimliğini söyler (`yayin-oncesi`, `app-store`, `google-play`, `paywall`); rapor dosya adlarındaki tür de budur,
  - `<!-- grup: Kontrol listeleri -->` ya da `<!-- grup: Rehberler -->` menüdeki grubu (kontrol listelerinde madde sayısı menüde rozet olarak görünür, denetim prompt'u maddelerden üretilir),
  - `<!-- ikon: ... -->` simgesi: `shield`, `phone`, `play`, `card`, `palette`, `chart`, `server`, `sparkles`, `package`, `clipboard`, `file`, `globe`, `landmark`, `devices` (yenisi gerekirse `site/src/components/Simge.astro`'ya Lucide çizgisi eklenir).
- `veri/repolar.json`: repo kataloğu, kategorileri ve alt kategorileri (`folders`: her kategoride `name`, çipte görünen kısa `kisa`, başlığın altındaki `aciklama` ve `alt` listesi).
  Her repoda `r` sahip/ad, `f` kategori, `af` alt kategori kimliği, `k` kurulum yeri, `a` kurulabildiği ajanlar, `tr` Türkçe açıklama, `w` uyarı, `src` kaynak video, `at` kataloğa eklenme tarihi; `s` yıldız sayısı, `l` dil, `d` İngilizce açıklama, `archived` ve `pushed` `--github` ile GitHub'dan tazelenir.
  Kategori reponun ne işe yaradığını söyler (tasarım, güvenlik ve test, ajana web erişimi...); skill mi, uygulama mı, kütüphane mi olduğu kategoriye değil `k` kurulum yerine yazılır.
  Yeni repo mevcut bir alt kategoriye konur; hiçbirine uymuyorsa yeni alt kategori açılır, yeni ana kategori açmadan önce kullanıcıya sorulur.
  `k` README'deki kurulum talimatına göre seçilir ve kartta etiket ile kurulum prompt'unu belirler:
  - `proje`: projeye eklenen kütüphane, paket ya da dosya; prompt aracı kullanılacak projenin oturumuna yapıştırılır.
  - `ajan`: kodlama ajanına kurulan skill, eklenti, MCP sunucusu ya da hook; prompt kapsamı (tüm projeler ya da tek proje) kullanıcıya sordurur.
    `a` listesi README'ye göre kurulabildiği ajanlardır (`claude`, `codex`); her biri kartta ayrı etiket ve kurulum düğmesi olur.
    `npx skills add` ile kurulanlar ve düz `SKILL.md` skill'leri Codex'e de kurulur (Codex `.agents/skills` klasörünü okur); sadece Claude'a özel eklenti, hook ya da ayar kuranlar `["claude"]` kalır.
  - `uygulama`: bilgisayara ya da sunucuya kurulan, kendi başına çalışan program veya komut satırı aracı.
  - `kaynak`: kurulmaz; okunur ya da örnek alınır, kurulum düğmesi yoktur.
  İki yolu olan repoda (örneğin hem eklenti hem projeye dosya yazan tam kurulum) asıl kullanım yolu seçilir, fark `w` uyarısına yazılır.
- `veri/linkler.json`: `--github` çalıştırmasında içerikteki linklerden açılmayanlar; sitede ⚠ ile işaretlenir, Genel bakış'taki Dikkat kutucuğunda sayılır.
- `veri/raporlar/<proje-adi>/<YYYY-MM-DD>.md` yayın öncesi, `<YYYY-MM-DD>-<liste>.md` diğer listelerin (ör. `-app-store`, `-google-play`, `-paywall`) denetim raporudur; yerel sayfanın "Proje raporları" bölümünde gösterilir ve aynı projenin aynı türdeki önceki raporuyla karşılaştırılır; klasör kök `.gitignore` ile git'e girmez, raporlar sadece bu bilgisayarda durur.
- `skills/`: yayın öncesi, App Store ve Google Play denetim skill'leri.
  `skills/*/kontrol-listesi.md` elle düzenlenmez; `guncelle.py` onları `icerik/yayin-oncesi-maddeler.md`, `icerik/app-store-incelemesi.md` ve `icerik/google-play-incelemesi.md`'den kopyalar.
- `uygulama/`: `katalog.py` (çekirdek), `mcp_sunucu.py` (AI arayüzü), `site_uret.py` (sitenin içeriğini üretir), `guncelle.py` (her şeyi üretir, yerel sayfayı derler, kopyaları eşitler).
  `python uygulama/katalog.py dogrula` kimlik, atıf ve rapor sorunlarını listeler; `ara <sorgu>` maddelerde, rehberlerde ve repolarda sitedeki kuralla arar (dolgu kelimeleri atılır, kökten eşleşir, kelimelerin en az yarısı yeter); `json` kataloğun tamamını verir.

## MCP arayüzü

- `uygulama/mcp_sunucu.py` çekirdeği stdio üzerinden MCP araçları olarak açar; paket kurulumu gerektirmez, her çağrıda dosyaları yeniden okur.
- Araçlar: `ara` (maddeler, rehber öğeleri, repolar), `kontrol_listesi` (maddeler kimlikleriyle ve denetim talimatıyla), `arac_oner` (ihtiyaç, altyapı ve kurulum yerine göre), `repolar` (repo kataloğu; kategori ve alt kategoriye göre süzer, kategori listesini de verir), `belge` (belge listesi ya da atıfları çözülmüş metin), `rapor_kaydet` (raporu doğrulayıp `veri/raporlar/`'a yazar, sayfayı günceller, önceki raporla karşılaştırır), `rapor_karsilastir`.
- Yeni araç ya da alan eklenince önce çekirdeğe (`katalog.py`) eklenir, sunucu çekirdeği kullanır; sunucu kendi başına md ayrıştırmaz.
- Sunucu Claude Code'a ya da Codex'e kullanıcı istemeden eklenmez.

## İçerik biçimi ve site görünümü

- `##` bölümleri sayfanın sağındaki "Sayfa içeriği" menüsünde görünür; bölüm adları kısa tutulur.
- Kod blokları (```) sayfada "Kopyala" düğmesi alır; hazır prompt ve komutlar kod bloğu olarak yazılır.
- Sayfadaki prompt düğmeleri ne yaptığını adıyla ve simgesiyle söyler: denetim (kalkan), projeye kurulum (indirme), Claude'a kurulum (robot), Codex'e kurulum (komut satırı), uygulama kurulumu (ekran), kullanım (fiş), tasarım (palet), canlı örneğin kodu (belge), düz kopyalama; üzerine gelince prompt'un kendisi görünür.
  Repo kartlarında kurulum düğmeleri "Kurulum prompt'u" başlıklı tek grupta hedefin adıyla (Proje, Claude, Codex, Uygulama) durur.
- Rehber ve repo kartları aynı yapıdadır (shadcn/ui kartı): isteğe bağlı üst önizleme, başlık kısmı, açıklama, gri kutuda alanlar, alt şerit.
  Başlık kısmında ad, altında soluk satırda tür (repo kartında sahip, dil ve eklenme tarihi), sağ üstte eylem durur: bağlantılı kartta siteyi yeni sekmede açan düğme, üstünde canlı örnek olan kartta örneği tam ekran açan düğme, repo kartında yıldız sayısı.
  Alt şeritte asıl prompt düğmesi dolu (`PromptDugme` `ana`), diğer düğmeler çerçevelidir; düğmeler şeridin üstüne hizalanır.
- Kartlar CSS subgrid ile ızgaranın satırlarına bağlanır: aynı sıradaki kartlarda başlık, açıklama, her alan ve alt şerit aynı hizada başlar, kısa içerikli kartta boşluk parçanın altında kalır.
  Bunun için kartın doğrudan çocuklarının sayısı kapladığı satır sayısına eşit olmalıdır: rehber kartında `site_uret.py` bunu `satir` olarak verir, repo kartı her zaman 6 satırdır (başlık, açıklama, uyarı, kurulum, kaynak, alt şerit); boş kalan parça da yerini korur (uyarısız repoda boş uyarı satırı).
- Repo kartlarında görünen kartlar arasında açıklaması ve uyarısı en uzun olan %15'lik dilim (en az 170 karakter) üç ve daha çok sütunlu ekranda iki sütun genişliğinde olur.
  Yeni düğme eklenirse `site/src/components/PromptDugme.astro` bu türlerden biriyle (`tur`) kullanılır.
- Sayfa içeriği en çok 1200 px genişliğinde ortalanır; masaüstünde 32 px, mobilde 16 px yan boşluk kullanılır.
- Renkler koyu ve açık tema için `site/src/styles/ship.css` içinde tasarım tokenlarıyla tanımlanır; Geist ve Geist Mono fontları `@fontsource-variable` paketlerinden yerel olarak yüklenir.
- Kontrol listelerinde maddeler ya numaralı satırdır (yayın öncesi listesi) ya da ilk sütunu `#` olan tablo satırıdır.
  Numaralı satırlı en uzun liste denetim listesi sayılır; her bölümüne "Bu bölümü denetle" prompt'u eklenir.
  Başka md'lerde uzun numaralı liste kullanma; tablo kullan.
- Her maddenin değişmeyen bir kimliği vardır: numaralı satırda satır sonunda, tabloda `#` hücresinde numaradan sonra `<!-- id: yo-hesap-silme -->`.
  Kimlik küçük harf ve rakamdan, tirelerle ayrılmış parçalardan oluşur ve listenin önekiyle başlar (`yo-` yayın öncesi, `as-` App Store, `gp-` Google Play, `pw-` Paywall).
  Madde yeniden yazılsa, taşınsa ya da numarası değişse de kimliği değişmez; yeni madde yeni kimlik alır, silinen maddenin kimliği başka maddeye verilmez.
  Numaralar sırayla verilir, madde eklenince sonrakiler kayabilir.
- Başka bir md'den bir maddeye numarasıyla atıf verilecekse numara yazılmaz, `{{no:kimlik}}` yazılır (ör. `[yayın öncesi {{no:yo-hesap-silme}}. madde](yayin-oncesi-maddeler.md)`); sayfa ve skill kopyaları maddenin o anki numarasını gösterir.
- `<!-- yan-yana -->` satırı olan md'de tablolar karta dönüşür.
  Kartta ilk sütun başlık olur, `Tür` sütunu ve bağlantı olan `Kaynak` sütunu başlığın altındaki soluk satırda görünür (düz metin kaynak alan olarak kalır), sonraki ilk sütun açıklama, kalanlar sütun sırasıyla gri kutuda "ad üstte, değer altta" alan olur.
  Boş hücre de alan olarak yerini korur; alan sırası tablonun sütun sırasıdır, bu yüzden aynı tablodaki kartlarda "Ücret" hep aynı yerde durur.
- Böyle bir md'de kartın prompt düğmesi tablonun ilk sütun başlığına göre seçilir: `Stil` "Bu stilde tasarla", `Kalıp` "Bu kalıbı uygula", `Renk çifti` "Bu renklerle dene", `İlham` "Bu fikri uyarla", `Etkileşim` "Bu etkileşimi yap", `Hareket` "Bu hareketi ekle", `İşaret` "Bu işareti temizle", `Yasa` "Bu yasaya göre incele", `Prompt` "Prompt'u kopyala" (açıklama sütunu prompt'un kendisidir), diğerleri araç sayılıp "Kullanım prompt'u" alır (`uygulama/site_uret.py` içindeki `CARD_PROMPTS`).
- Böyle bir md'de ilk sütun başlığı `Stil` olan tablolarda her karta o stilin CSS örneği eklenir.
  Örnekler `site/src/styles/ship.css` içindeki `.pv-<stil-adı>` sınıflarıdır (ad küçük harf, harf ve rakam dışı karakterler `-`); yeni stil eklenince örneğini de oraya yaz.
- Md'ler arasında göreli link ver (`[yayın öncesi](yayin-oncesi-maddeler.md)`); site bunları sayfa adresine çevirir.

## Canlı örnekler

- `<!-- yan-yana -->` rehberindeki bir tablo satırının ilk hücresine `<!-- ornek: ad -->` yazılırsa kart `site/public/ornekler/<ad>.html` örneğini gösterir ve "Kodu kopyala" (dosyanın tamamı) düğmesi çıkar.
  Tablonun bütün satırlarında örnek varsa örnek kartın üstünde iframe içinde çalışır, sağ üstteki düğme onu tam ekran açar; sadece bazı satırlarda varsa (kütüphane tablosu gibi) "Örneği aç" düğmesi örneği pencerede (dialog) açar, satırlar boşuna uzamaz.
  `python uygulama/katalog.py dogrula` dosyası olmayan örneği sorun sayar; `llms-full.txt` örneği bağlantı olarak verir.
- Örnek tek dosyadır: CSS ve JavaScript içinde, CDN, web fontu ya da uzak görsel yok; ikonlar satır içi SVG.
  Yerel sayfada dosyadan açıldığı için `<script type="module">` ve `/` ile başlayan adres kullanılmaz.
- Kartın iframe yüksekliği örneğin `<meta name="yukseklik" content="420">` satırından gelir; örnek 280 px ile 900 px genişlik arasında yatay kaydırmasız görünür.
- Metinler Türkçedir, etkileşim klavyeyle de çalışır, `prefers-reduced-motion` açıkken animasyon kapanır.
- Örnek, gönderideki tasarımın bizim kodumuzla yeniden kurulmuş hâlidir; başkasının kodu kopyalanmaz.
  Kütüphane kartındaki örnek kütüphanenin etkisini kendi kısa kodumuzla gösterir, kütüphaneyi içine gömmez; dosyanın başındaki yorumda kütüphanenin gerçek kurulumu ve kullanımı yazar.
  Özgün kod paylaşılmışsa yeri ve koşulu (ücretsiz, ücretli, DM ile, lisanssız) `Özgün kod` sütununa yazılır; lisansı olmayan kod sadece incelenir.

## Proje raporları

- Rapor biçimi: ilk satır `# <Proje adı>`, sonra `- Proje: <yol ya da repo>` ve `- Kontrol tarihi: YYYY-MM-DD` maddeleri, ardından kontrol listesindeki her bölüm için `## <bölüm adı>` ve `| Kimlik | Madde | Durum | Bulgu |` tablosu.
- `Kimlik` sütunu maddenin kalıcı kimliğidir; `Durum` ✅ tamam, ⚠️ kısmen, ❌ eksik, ➖ uygulanmaz simgelerinden biriyle başlar.
  Karşılaştırma bu iki sütundan yapılır, madde numaraları değişse de bozulmaz.
- Eski raporlar silinmez; her denetim yeni tarihli dosyadır.
- Denetim yerel sayfadaki prompt ile (raporun kaydedileceği yolu ve `guncelle.py` komutunu içerir) ya da kuruluysa skill'lerle yapılır; skill'ler raporun yerini `~/.ship-ready.json`'dan bulur (`guncelle.py` bu dosyayı yazar).

## Katalog güncellemesi

Yeni repo kullanıcının getirdiği bağlantı veya videodan eklenir; özgün README ile doğrulanır.
`veri/repolar.json` kaydına `r`, Türkçe `tr` açıklaması, `f` kategorisi, `k` kurulum yeri, ajansa `a` hedefleri, `at` tarihi ve gerekirse `w` uyarısı ile `src` kaynak eklenir.
`python uygulama/guncelle.py --github` GitHub alanlarını tazeler ve içerik bağlantılarını denetler.
GitHub 404 yanıtı silinmiş, gizli veya erişilemeyen bir depoyu gösterebilir; katalog kaydı yalnızca sahibinin onayıyla kaldırılır.
Taşınmış deponun `r` alanı güncel adla düzeltilir.
`veri/linkler.json` açılmayan içerik bağlantılarını tutar; bunlar sitede uyarıyla görünür.
