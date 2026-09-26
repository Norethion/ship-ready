# ship-ready

## Amaç

Kişisel projeleri AI ile geliştirirken başvurulan Türkçe bir araç kutusu: yayına çıkmadan nelere bakılmalı, hangi eklentiler, araçlar ve skill'ler kullanılabilir, hangi şeyler işi kolaylaştırır.
Kontrol listeleri, rehberler ve repo kataloğu herkese açık bir site olarak yayımlanır (`site/`); denetim raporları gibi kişisel parçalar sadece yerel sayfada ve MCP sunucusunda kalır.
Proje GitHub'da özel repodadır (`Norethion/ship-ready`, dal `main`); commit, push ve siteyi internete koymak (ör. Cloudflare Pages) kullanıcı istemeden yapılmaz.
Kullanıcının getirdiği video, link ya da ekran görüntüsü bu amaca göre işlenir: kontrol edilecek bir iş ise ilgili md'ye madde olur, GitHub reposu ise repo kataloğuna (`veri/repolar.json`) girer, site ya da araç ise konusuna uygun md'ye eklenir.
Repo kataloğu kullanıcının GitHub yıldızlarına bağlı değildir: yıldızlar çekilmez, repo yıldızlanmaz.
Bilgiler kaynağından doğrulanır; videodaki iddia aynen alınmaz.
Instagram videosu sadece açıklama metninden değerlendirilmez, tamamı izlenir: yt-dlp ile ses ve görüntü indirilir, ses faster-whisper ile zaman damgalı yazıya dökülür, görüntüden 2 saniyede bir kare alınıp ekrandaki yazılar okunur.
Kaydırmalı gönderilerde her slayt `?img_index=N` ile tek tek açılır.
Bu araçlar sisteme değil, geçici bir Python ortamına (venv) kurulur.
Proje sadece Türkçedir.

## Yönetim

Bu klasör AI tarafından yönetilir; kullanıcı sayfayı sadece görüntüler.
Kullanıcı sayfayı `index.html`'e çift tıklayarak açar: sunucu ya da port açılmaz, `index.html` yerel sayfaya (`sayfa/`) yönlendirir.
Yerel sayfa herkese açık sitenin raporlu hâlidir; ikisi aynı Astro projesinden, aynı süreçle (`python uygulama/guncelle.py`) üretilir, görünüşleri ve işlevleri aynıdır.
`AGENTS.md` ve `CLAUDE.md` birebir aynıdır: sadece `AGENTS.md` düzenlenir, `uygulama/guncelle.py` her çalıştığında onu `CLAUDE.md`'ye kopyalar.
`index.html`, `sayfa/` ve `site/` altındaki üretilen dosyalar elle düzenlenmez.
Tek doğru kaynak `icerik/*.md`, `veri/*.json` ve `veri/raporlar/`'dır; `uygulama/katalog.py` (çekirdek) bunları listeler, maddeler, rehber öğeleri, repolar ve raporlar olarak okur.
Site, yerel sayfa ve MCP sunucusu bu çekirdeğin çıktısıyla beslenir; hiçbiri md'yi kendi başına ayrıştırmaz.

## Site ve yerel sayfa

- `site/` bir Astro Starlight projesidir ve iki derlemesi vardır:
  - Herkese açık site: `site/` klasöründe `npm run build`, çıktı `site/dist/`. Raporlar girmez; ileride sunucuda yayımlamak içindir.
  - Yerel sayfa: `guncelle.py` her çalıştığında `SHIP_YEREL=1` ile derler, çıktı `sayfa/`. Raporlar (`/raporlar/`), Genel bakış'ta Takip bölümü, raporu ship-ready'ye kaydettiren denetim prompt'u ve çevrimdışı arama sadece burada vardır.
  `site/yerel-derleme.mjs` yerel derlemeyi dosyadan açılır yapar: adresleri göreli yapar, modül betiklerini sayfanın içine alır. Pagefind sunucusuz çalışmadığı için arama `YerelArama.astro` ile yapılır.
- `python uygulama/guncelle.py` (içinde `uygulama/site_uret.py`) şunları çekirdekten üretir ve bunlar elle düzenlenmez: `site/src/content/docs/` (sayfalar), `site/src/data/katalog.json` ve `sidebar.json`, `site/public/katalog.json`, `llms.txt` (sayfalar ve kategoriye göre dizilmiş repolar) ve `llms-full.txt` (bütün içerik tek dosyada, maddeler kimlikleriyle; AI'lar için), `site/src/yerel/` (yerel sayfanın raporları, raporlu kenar menüsü ve arama dizini; `.gitignore`'da, herkese açık derleme okumaz).
- Elle düzenlenenler: `site/src/components/` (Madde, DenetimPrompt, Kart, Kartlar, RepoKatalog, PromptDugme, KenarMenu, SiteBasligi, TemaSecici, SayfaIcerigi, Kutucuk, Simge, RaporOzeti, YerelTakip, YerelArama), `site/src/pages/raporlar/`, `site/src/yerel.ts`, `site/src/arama.ts` (iki aramanın ortak eşleştirme kuralları: dolgu kelimeleri, kökten eşleşme), `site/src/content.config.ts`, `site/src/content/i18n/tr.json`, `site/src/styles/ship.css`, `site/astro.config.mjs`, `site/yerel-derleme.mjs`.
  Sadece yerel sayfada olacak bir şey `src/yerel.ts`'deki `YEREL` ile koşullanır; kişisel veri herkese açık derlemeye girmez.
- Kenar menü: `KenarMenu.astro` Starlight'ın menüsünün, `SiteBasligi.astro` site adının, `TemaSecici.astro` tema seçim kutusunun (tarayıcının kendi açılır listesi yerine sitenin görünümünde açılır menü) yerine geçer; `SayfaIcerigi.astro` Starlight'ın "Sayfa içeriği" menüsünü sarar, sayfanın dibine inilince son başlığı seçer. Menüdeki simge md'nin `<!-- ikon: -->` satırından, sayaç madde ya da repo sayısından gelir; gruplar Kontrol listeleri, Rehberler, Katalog ve yerel sayfada Takip'tir.
- Genel bakış kutucuklardan (`Kutucuk.astro`) oluşur: kontrol listelerinde "Listeyi aç" ve denetim düğmesi, rehberler, repo kataloğu ve arşivlenmiş ya da 1+ yıldır güncellenmeyen repoları ve açılmayan linkleri sayan Dikkat kutucuğu (`/repolar/#dikkat` Dikkat süzgeciyle açılır).
- Adresler: kontrol listeleri `/listeler/<liste>/`, rehberler `/rehberler/<md adı>/`, repo kataloğu `/repolar/` (`#ara=<repo>` aramayla, `#dikkat` Dikkat süzgeciyle açılır), yerel sayfada raporlar `/raporlar/` ve `/raporlar/<proje>/<dosya adı>/`; her maddenin bağlantısı `#<kimlik>`. `{{no:kimlik}}` içeren linkler doğrudan o maddeye gider.
- Kontrol listelerinde maddeler kimlikli kart olur, numaralı listede her bölüme denetim prompt'u eklenir; `<!-- yan-yana -->` rehberlerinde tablolar karta dönüşür (prompt düğmesi ilk sütun başlığına göre: `site_uret.py` içindeki `CARD_PROMPTS`), diğer rehberler Markdown olarak kalır.
- Siteye sadece doğrulanmış, Türkçe açıklaması ve kurulum yeri olan repolar girer; raporlar girmez.
- Herkese açık siteyi görmek için `site/` klasöründe `npm run build` ve `npm run preview` (ya da `npm run dev`). Paketler sadece `site/node_modules`'a kurulur; yerel sayfanın derlenmesi için Node.js ve bu paketler gerekir.

## Klasörler

- `icerik/*.md`: yan menüde ve Genel bakış'ta gösterilir. Başlığı ilk `#` satırıdır (menüde `:` öncesi kısmı), Genel bakış'taki açıklaması başlıktan sonraki ilk paragraftır. Başlığın altındaki satırlar:
  - `<!-- sira: N -->` menüdeki sırası,
  - `<!-- liste: kimlik -->` md'nin bir kontrol listesi olduğunu ve kimliğini söyler (`yayin-oncesi`, `app-store`, `google-play`, `paywall`); rapor dosya adlarındaki tür de budur,
  - `<!-- grup: Kontrol listeleri -->` ya da `<!-- grup: Rehberler -->` menüdeki grubu (kontrol listelerinde madde sayısı menüde rozet olarak görünür, denetim prompt'u maddelerden üretilir),
  - `<!-- ikon: ... -->` simgesi: `shield`, `phone`, `play`, `card`, `palette`, `chart`, `server`, `sparkles`, `package`, `clipboard`, `file` (yenisi gerekirse `site/src/components/Simge.astro`'ya Lucide çizgisi eklenir).
- `veri/repolar.json`: repo kataloğu, kategorileri ve alt kategorileri (`folders`: her kategoride `name`, çipte görünen kısa `kisa`, başlığın altındaki `aciklama` ve `alt` listesi). Her repoda `r` sahip/ad, `f` kategori, `af` alt kategori kimliği, `k` kurulum yeri, `a` kurulabildiği ajanlar, `tr` Türkçe açıklama, `w` uyarı, `src` kaynak video, `at` kataloğa eklenme tarihi; `s` yıldız sayısı, `l` dil, `d` İngilizce açıklama, `archived` ve `pushed` `--github` ile GitHub'dan tazelenir.
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
- `veri/raporlar/<proje-adi>/<YYYY-MM-DD>.md` yayın öncesi, `<YYYY-MM-DD>-<liste>.md` diğer listelerin (ör. `-app-store`, `-google-play`, `-paywall`) denetim raporudur; yerel sayfanın "Proje raporları" bölümünde gösterilir ve aynı projenin aynı türdeki önceki raporuyla karşılaştırılır.
- `skills/`: yayın öncesi, App Store ve Google Play denetim skill'leri; şu an kurulu değil, istenirse `~/.claude/skills/` altına kopyalanır.
  `skills/*/kontrol-listesi.md` elle düzenlenmez; `guncelle.py` onları `icerik/yayin-oncesi-maddeler.md`, `icerik/app-store-incelemesi.md` ve `icerik/google-play-incelemesi.md`'den kopyalar.
- `uygulama/`: `katalog.py` (çekirdek), `mcp_sunucu.py` (AI arayüzü), `site_uret.py` (sitenin içeriğini üretir), `guncelle.py` (her şeyi üretir, yerel sayfayı derler, kopyaları eşitler).
  `python uygulama/katalog.py dogrula` kimlik, atıf ve rapor sorunlarını listeler; `ara <sorgu>` maddelerde, rehberlerde ve repolarda sitedeki kuralla arar (dolgu kelimeleri atılır, kökten eşleşir, kelimelerin en az yarısı yeter); `json` kataloğun tamamını verir.

## AI arayüzü (MCP)

- `uygulama/mcp_sunucu.py` çekirdeği stdio üzerinden MCP araçları olarak açar; paket kurulumu gerektirmez, her çağrıda dosyaları yeniden okur.
- Araçlar: `ara` (maddeler, rehber öğeleri, repolar), `kontrol_listesi` (maddeler kimlikleriyle ve denetim talimatıyla), `arac_oner` (ihtiyaç, altyapı ve kurulum yerine göre), `repolar` (repo kataloğu; kategori ve alt kategoriye göre süzer, kategori listesini de verir), `belge` (belge listesi ya da atıfları çözülmüş metin), `rapor_kaydet` (raporu doğrulayıp `veri/raporlar/`'a yazar, sayfayı günceller, önceki raporla karşılaştırır), `rapor_karsilastir`.
- Yeni araç ya da alan eklenince önce çekirdeğe (`katalog.py`) eklenir, sunucu çekirdeği kullanır; sunucu kendi başına md ayrıştırmaz.
- Sunucu Claude Code'a ya da Codex'e kullanıcı istemeden eklenmez. Kullanıcı eklemek isterse kendisi çalıştırır:
  `claude mcp add --scope user ship-ready -- python "D:\workspace-ali\ship-ready\uygulama\mcp_sunucu.py"` ve `codex mcp add ship-ready -- python "D:\workspace-ali\ship-ready\uygulama\mcp_sunucu.py"`

## Md yazım kuralları

- `##` bölümleri sayfanın sağındaki "Sayfa içeriği" menüsünde görünür; bölüm adları kısa tutulur.
- Kod blokları (```) sayfada "Kopyala" düğmesi alır; hazır prompt ve komutlar kod bloğu olarak yazılır.
- Sayfadaki prompt düğmeleri ne yaptığını adıyla ve simgesiyle söyler: denetim (kalkan), projeye kurulum (indirme), Claude'a kurulum (robot), Codex'e kurulum (komut satırı), uygulama kurulumu (ekran), kullanım (fiş), tasarım (palet), düz kopyalama; üzerine gelince prompt'un kendisi görünür.
  Repo kartlarında kurulum düğmeleri "Kurulum prompt'u" başlıklı tek grupta hedefin adıyla (Proje, Claude, Codex, Uygulama) durur.
- Repo kartları bento düzenindedir: her kart içeriği kadar yer kaplar, görünen kartlar arasında açıklaması ve uyarısı en uzun olan %15'lik dilim (en az 170 karakter) üç ve daha çok sütunlu ekranda iki sütun genişliğinde olur. Yeni düğme eklenirse `site/src/components/PromptDugme.astro` bu türlerden biriyle (`tur`) kullanılır.
- Sayfada genişlik sınırı (max-width) kullanılmaz; her şey ekran genişliğine göre akar.
- Kontrol listelerinde maddeler ya numaralı satırdır (yayın öncesi listesi) ya da ilk sütunu `#` olan tablo satırıdır. Numaralı satırlı en uzun liste denetim listesi sayılır; her bölümüne "Bu bölümü denetle" prompt'u eklenir. Başka md'lerde uzun numaralı liste kullanma; tablo kullan.
- Her maddenin değişmeyen bir kimliği vardır: numaralı satırda satır sonunda, tabloda `#` hücresinde numaradan sonra `<!-- id: yo-hesap-silme -->`. Kimlik küçük harf ve rakamdan, tirelerle ayrılmış parçalardan oluşur ve listenin önekiyle başlar (`yo-` yayın öncesi, `as-` App Store, `gp-` Google Play, `pw-` Paywall).
  Madde yeniden yazılsa, taşınsa ya da numarası değişse de kimliği değişmez; yeni madde yeni kimlik alır, silinen maddenin kimliği başka maddeye verilmez. Numaralar sırayla verilir, madde eklenince sonrakiler kayabilir.
- Başka bir md'den bir maddeye numarasıyla atıf verilecekse numara yazılmaz, `{{no:kimlik}}` yazılır (ör. `[yayın öncesi {{no:yo-hesap-silme}}. madde](yayin-oncesi-maddeler.md)`); sayfa ve skill kopyaları maddenin o anki numarasını gösterir.
- `<!-- yan-yana -->` satırı olan md'de tablolar karta dönüşür.
  Kartta ilk sütun başlık olur, `Tür` sütunu başlığın yanında etiket olarak görünür, sonraki ilk sütun açıklama, kalanlar "Başlık: değer" satırı olur.
- Böyle bir md'de kartın prompt düğmesi tablonun ilk sütun başlığına göre seçilir: `Stil` "Bu stilde tasarla", `Kalıp` "Bu kalıbı uygula", `Renk çifti` "Bu renklerle dene", `İlham` "Bu fikri uyarla", `Etkileşim` "Bu etkileşimi yap", diğerleri araç sayılıp "Kullanım prompt'u" alır (`uygulama/site_uret.py` içindeki `CARD_PROMPTS`).
- Böyle bir md'de ilk sütun başlığı `Stil` olan tablolarda her karta o stilin CSS örneği eklenir.
  Örnekler `site/src/styles/ship.css` içindeki `.pv-<stil-adı>` sınıflarıdır (ad küçük harf, harf ve rakam dışı karakterler `-`); yeni stil eklenince örneğini de oraya yaz.
- Md'ler arasında göreli link ver (`[yayın öncesi](yayin-oncesi-maddeler.md)`); site bunları sayfa adresine çevirir.

## Proje raporları

- Rapor biçimi: ilk satır `# <Proje adı>`, sonra `- Proje: <yol ya da repo>` ve `- Kontrol tarihi: YYYY-MM-DD` maddeleri, ardından kontrol listesindeki her bölüm için `## <bölüm adı>` ve `| Kimlik | Madde | Durum | Bulgu |` tablosu.
- `Kimlik` sütunu maddenin kalıcı kimliğidir; `Durum` ✅ tamam, ⚠️ kısmen, ❌ eksik, ➖ uygulanmaz simgelerinden biriyle başlar. Karşılaştırma bu iki sütundan yapılır, madde numaraları değişse de bozulmaz.
- Eski raporlar silinmez; her denetim yeni tarihli dosyadır.
- Denetim yerel sayfadaki prompt ile (raporun kaydedileceği yolu ve `guncelle.py` komutunu içerir) ya da kuruluysa skill'lerle yapılır; skill'ler raporun yerini `~/.ship-ready.json`'dan bulur (`guncelle.py` bu dosyayı yazar).

## Güncelleme

- İçerik, rapor ya da `veri/repolar.json` değiştikten sonra: `python uygulama/guncelle.py`
  Betik siteyi üretir, yerel sayfayı derler (3-5 saniye) ve sonunda çekirdeğin bulduğu sorunları (`SORUN:` satırları: kimliksiz ya da yinelenen madde, bilinmeyen atıf, raporda listede olmayan kimlik, yerel sayfanın derlenememesi) yazar ve sorun varsa 1 koduyla çıkar; sorunlar düzeltilmeden iş bitmiş sayılmaz.
- Repoların GitHub bilgilerini tazelemek ve içerikteki linkleri kontrol etmek için: `python uygulama/guncelle.py --github`
  Her repo GitHub API'den tek tek okunur; girişsiz sınır saatte 60 istek olduğu için `GITHUB_TOKEN` ya da `gh` oturumu kullanılır.
  Bulunamayan (silinmiş ya da gizli) repoyu katalogdan çıkar, taşınmış reponun `r` alanını yeni adıyla düzelt.
- Yeni repo kullanıcının getirdiği link ya da videodan eklenir: README'sinden doğrula, `veri/repolar.json`'a `r`, Türkçe `tr` açıklaması, klasörü (`f`), kurulum yerini (`k`, ajan ise `a`), eklenme tarihini (`at`), gerekiyorsa `w` uyarısını ve `src` kaynağını yaz, sonra `--github` ile çalıştır.
- Arşivlenmiş ve 1 yıldan uzun süredir güncellenmeyen repolar sitede "⚠ Dikkat" süzgecinde toplanır; açılmayan linkleri düzelt ya da kaldır.
- Klasörü ve repoları kullanıcı sayfadan değiştiremez; tüm değişiklikler json dosyaları üzerinden yapılır.
- Commit ve push kullanıcı istemeden yapılmaz. Üretilen çıktılar (`sayfa/`, `site/dist/`) ve yerel sayfanın kişisel verisi (`site/src/yerel/`) repoya girmez; klonlanan projede `site/` klasöründe `npm install`, sonra `python uygulama/guncelle.py` çalıştırılır.
