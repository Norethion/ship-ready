# AI geliştirme akışı

<!-- sira: 7 -->
<!-- grup: Rehberler -->
<!-- ikon: sparkles -->

Claude Code ile proje geliştirirken işe yarayan komutlar, MCP sunucuları, skill'ler ve hazır prompt'lar.

## Claude Code komutları

| Komut | Ne yapar |
|---|---|
| `/init` | Projeyi inceleyip `CLAUDE.md` oluşturur; Claude sonraki oturumlarda projeyi buradan tanır. |
| `/code-review` | Değişiklikleri hata açısından inceler. `--fix` bulguları düzeltir, `ultra` bulutta çok ajanlı derin inceleme yapar. |
| `/security-review` | Daldaki değişiklikleri güvenlik açısından inceler. |
| `/simplify` | Değişen kodu tekrar, sadelik ve verimlilik açısından gözden geçirip düzeltir. |
| `/run` | Uygulamayı başlatıp değişikliğin gerçekten çalıştığını görür. |
| `/loop` | Bir komutu belli aralıklarla tekrar çalıştırır; örneğin yayına almanın durumunu 5 dakikada bir kontrol etmek. |
| `/schedule` | Bulutta zamanlanmış ajan (routine) kurar. |
| `/remote-control` | Bu bilgisayardaki oturumu telefondaki Claude uygulamasından ya da claude.ai/code'dan sürdürür. Team ve Enterprise planında yöneticinin açması gerekir. |
| `/voice` | Yazmak yerine konuşarak prompt verirsin: `Space`'i basılı tutup konuş ya da `/voice tap` ile dokunarak başlat. Türkçe için `/config`'te dili `tr` yap. claude.ai hesabıyla giriş ister; ses Anthropic'in sunucusunda yazıya dökülür, mesaj hakkından düşmez. |
| `/chrome` | Claude Code'u Chrome'daki "Claude in Chrome" eklentisine bağlar (`claude --chrome` ile de açılır): senin oturumunla sayfaları açar, form doldurur, konsolu okur, GIF kaydeder. Pro, Max, Team ya da Enterprise planı ve `/login` ile giriş ister. |
| `/agents` | Alt ajanlar (subagent) `.claude/agents/` (proje) ya da `~/.claude/agents/` (tüm projeler) altında Markdown dosyasıdır; Claude'a "şu işi yapan bir alt ajan oluştur" demen yeter, ana ajan işi uygun alt ajana devreder. |
| `/output-style` | Claude'un cevap biçimini değiştirir: `Concise` sonucu ilk cümlede verir, giriş, anlatım ve özet kısmını atar (işi yine tam yapar, hata ve güvenlik uyarılarını kısaltmaz); `Explanatory` kodun yanına kısa açıklama ekler, `Learning` bazı kodları sana yazdırır, `Proactive` rutin kararlarda sormadan ilerler. `/output-style concise` ya da `/config` ile seçilir, bir sonraki mesajdan itibaren geçerli olur; tüm projeler için `~/.claude/settings.json`'a `"outputStyle": "Concise"` yazılır. |
| `/fewer-permission-prompts` | Sık kullanılan salt okunur komutlar için izin listesi ekleyip onay sorularını azaltır. |

## MCP sunucuları

MCP sunucuları Claude'a yeni yetenekler verir: tarayıcı, tasarım aracı gibi.
Kurulum komutlarının sonuna `--scope user` eklersen sunucu tüm projelerde kullanılabilir.

| Sunucu | Ne işe yarar |
|---|---|
| [Playwright MCP](https://github.com/microsoft/playwright-mcp) | Claude'a tarayıcı verir: sayfayı açar, tıklar, form doldurur, ekran görüntüsü alır; yaptığı işi kendisi test eder. |
| [Chrome DevTools MCP](https://github.com/ChromeDevTools/chrome-devtools-mcp) | Chrome'u geliştirici araçlarıyla kontrol eder: konsol, ağ istekleri, performans kaydı, Lighthouse denetimi, farklı cihaz ve ağ hızı taklidi. |
| [Figma MCP](https://developers.figma.com/docs/figma-mcp-server/) | Figma tasarımını okuyup frame'i koda çevirir. |
| [shadcn MCP](https://ui.shadcn.com/docs/mcp) | shadcn/ui ve projede tanımlı registry'lerdeki (Cult UI, Canvas UI gibi) bileşenleri Claude'a listeletir, arattırır ve doğal dille kurdurur; projede `components.json` olmalı. Ücretsiz, hesap gerekmez. |
| [Context7](https://github.com/upstash/context7) | Kütüphanelerin güncel, sürüme özel dokümanını ve kod örneklerini ajana verir; eski ya da uydurma API önerilerini azaltır. Sorgular context7.com'a gider. |
| [RevenueCat MCP](https://www.revenuecat.com/docs/tools/mcp) | Abonelik uygulamanın ürün, teklif, yetki (entitlement) ve gelir verisini Claude'a sordurur ve düzenletir; OAuth ile bağlanır. |
| [Buffer MCP](https://buffer.com/mcp) | Instagram, LinkedIn, X, TikTok gibi 9 platforma gönderi taslağı hazırlatır, zamanlar ve paylaşır, istatistikleri getirir; ücretsiz planda da açık. |
| Meta Ads MCP | Meta'nın resmi reklam bağlayıcısı (`mcp.facebook.com/ads`, Nisan 2026): kampanya performansını raporlar, kampanya ve reklam oluşturur; yeni kampanyalar varsayılan olarak duraklatılmış başlar. |
| [ElevenLabs MCP](https://github.com/elevenlabs/elevenlabs-mcp) | Metni sese çevirir, ses klonlar, konuşmayı yazıya döker; Claude'un cevabını seslendirmek için. Yerel sunucu artık bakımda değil, barındırılan sürüm (`api.elevenlabs.io/v1/mcp`) öneriliyor; ElevenLabs hesabı ister. |
| Gmail ve Google Takvim | claude.ai'deki Bağlayıcılar sayfasından (claude.ai/customize/connectors) eklenir; claude.ai hesabıyla girişte Claude Code'da kendiliğinden görünür, `/mcp` ile yönetilir. `claude mcp add` ile yerelde kurulamaz. |
| [Artemis](https://github.com/google/artemis) | Android uygulamanı doğal dille verilen talimatlarla gerçek cihazda ya da emülatörde test ettirir; logcat ve ekran görüntüsü toplar. Bir LLM API anahtarı ister. |

Playwright MCP:

```
claude mcp add playwright npx @playwright/mcp@latest
```

Chrome DevTools MCP:

```
claude mcp add chrome-devtools -- npx -y chrome-devtools-mcp@latest
```

Figma MCP:

```
claude mcp add --transport http figma https://mcp.figma.com/mcp
```

shadcn MCP (projenin klasöründe çalıştır, `.mcp.json` dosyasına ekler):

```
npx shadcn@latest mcp init --client claude
```

Context7 (kurulumda hangi ajana kurulacağını sorar, ücretsiz API anahtarı alır):

```
npx ctx7 setup
```

RevenueCat MCP:

```
claude mcp add --transport http revenuecat https://mcp.revenuecat.ai/mcp
```

## MCP izinleri

Her MCP sunucusu Claude'a senin yetkinle okuma, değiştirme ve gönderme izni verir; yedi kontrol [bu gönderiden](https://www.instagram.com/p/Dd3Vb4BCIu2/) alındı.
Ayda bir bu listeyle kurulu sunucuları gözden geçir.

| Kontrol | Ne yapılır |
|---|---|
| Kullanmadığını kaldır | `claude mcp list` ile kurulu sunucuları listele, kullanmadığını `claude mcp remove <ad>` ile kaldır; claude.ai bağlayıcılarını da `/mcp` ile gözden geçir. |
| Dosya erişimini daralt | Dosya sistemi sunucusuna ana dizini ya da diski değil sadece çalıştığın klasörü ver; `~/.ssh`, `~/.aws`, `.env` ve şifre dosyaları dışarıda kalsın. Claude Code'da `.claude/settings.json` içindeki `permissions.deny` ile (ör. `"Read(./.env)"`) bu dosyaları okumayı da kapat. |
| Geri dönüşü olmayana onay | Okumak yetiyorsa sunucuyu salt okunur kur; silme, e-posta ya da mesaj gönderme, ödeme ve yayınlama her seferinde senin onayından geçsin. |
| Token'a en az yetki | GitHub gibi servislerde tam yetkili kişisel token yerine sadece gereken repo ve izinleri olan, süresi dolan (fine-grained) token üret; token'ı ayar dosyasına düz metin yazma, ortam değişkeninden ver, sızarsa hemen iptal et. |
| "Her zaman izin ver"i temizle | Onay penceresinde "her zaman" dediğin araç bir daha sormadan çalışır. `/permissions` ile izin listesini aç, silme ve gönderme araçlarını çıkar, sadece zararsız okuma araçları kalsın. |
| Kaynağı ve sürümü doğrula | Sunucu bilgisayarında senin yetkinle çalışan bir koddur: resmî ya da tanınmış yayıncıdan kur, tanımadığın paketlerde sürümü sabitle (`@latest` yerine `@1.4.2`), uzak sunucunun OAuth izin ekranında istediği izinleri oku. |
| Okuduğu içeriğe güvenme | Web sayfası, e-posta ya da dosyanın içine gizlenmiş talimat Claude'u yönlendirebilir (prompt injection). Dış içerik okuyan bir araçla veri gönderebilen bir aracı aynı oturumda otomatik onaylama. |

MCP izinlerini denetle:

```
Bu bilgisayarda ve bu projede kurulu MCP sunucularını ve izinlerini denetle: claude mcp list çıktısını, ~/.claude.json, .mcp.json ve .claude/settings.json dosyalarını oku. Her sunucu için ne yapabildiğini (okuma, yazma, silme, gönderme, ödeme), hangi klasörlere ve hangi token'la eriştiğini, sürümünün sabit olup olmadığını ve kalıcı izin verilmiş araçlarını tablo hâlinde listele. Token değerlerini ekrana yazma. Kaldırılabilecek sunucuları ve daraltılması gereken izinleri öner; hiçbir şeyi onayım olmadan değiştirme.
```

## Skill'ler ve eklentiler

- **Skill nedir:** Claude'a belirli bir işi nasıl yapacağını öğreten `SKILL.md` dosyası. `npx skills add <sahip>/<repo>` ile kurulur, `npx skills find` ile aranır, dizini [skills.sh](https://skills.sh).
- **Eklenti (plugin):** Skill, komut ve ayarları bir arada getirir; `claude plugin marketplace add <sahip>/<repo>` ve ardından `claude plugin install <ad>@<pazar>` ile kurulur.
- **Örnekler:** Yazı için [Humanizer](https://github.com/blader/humanizer) ve [Stop Slop](https://github.com/hardikpandya/stop-slop), tasarım için [Impeccable](https://github.com/pbakaus/impeccable), kod tabanını tanımak için [Understand Anything](https://github.com/Egonex-AI/Understand-Anything).
- **Çalışma yöntemi:** [Superpowers](https://github.com/obra/superpowers), [gstack](https://github.com/garrytan/gstack), [Agent Skills](https://github.com/addyosmani/agent-skills) ve [GSD Core](https://github.com/open-gsd/gsd-core) ajana plan, test ve yayın adımları olan bir çalışma düzeni kurar; hepsi Claude Code ve Codex'e kurulur. Aynı işi yaptıkları için birini seç.
- **Hafıza ve bağlam:** [claude-mem](https://github.com/thedotmack/claude-mem) oturumları kaydedip sonraki oturuma bağlam verir (varsayılan kurulum ücretli barındırılan servise bağlanır); [context-mode](https://github.com/mksglu/context-mode) araç çıktılarını bağlamın dışında tutar.
- **Güvenlik taraması:** Anthropic'in resmî eklenti pazarındaki Claude Security projeyi birden çok ajanla tarar, bulguları ve yama önerilerini `CLAUDE-SECURITY-<zaman>/` klasörüne rapor olarak yazar, yamaları kendisi uygulamaz (`claude plugin install claude-security@claude-plugins-official`, sonra `/claude-security`); çok token harcar, sadece daldaki değişiklik için yerleşik `/security-review` yeter. [Bu videodaki](https://www.instagram.com/reel/DdqI39ERRuF/) beş adımlı tarama aşağıdaki hazır prompt'ta; araçları (Gitleaks, Semgrep, ZAP) repo kataloğunda.
- **Claude'dan Codex'e:** [codex-plugin-cc](https://github.com/openai/codex-plugin-cc) ile Claude Code içinden Codex'e kod incelemesi yaptırır ya da görev devredersin.
- **Kurmadan önce tara:** Skill'ler ajanın yetkileriyle çalışır; başkasının skill'ini kurmadan önce [SkillSpector](https://github.com/NVIDIA/SkillSpector) ile prompt injection ve veri sızdırma açısından tara. NVIDIA'nın incelediği 31.132 skill'in %26,1'inde güvenlik açığı, %5,2'sinde kötü niyet belirtisi bulunmuş.

SkillSpector'ı kur ve skill'i kurmadan önce GitHub linkinden tara:

```
uv tool install git+https://github.com/NVIDIA/skillspector.git
skillspector scan https://github.com/<sahip>/<skill-reposu>
```

## Proje talimat dosyaları

- **CLAUDE.md ve AGENTS.md:** Projenin nasıl çalıştığını, komutlarını ve kurallarını anlatır; Claude Code `CLAUDE.md`'yi, Codex ve diğer ajanlar `AGENTS.md`'yi okur.
- **İkisini aynı tut:** Projede ikisi de varsa biri diğerinin birebir kopyası olsun; düzenleme tek dosyada yapılsın. ship-ready'de `uygulama/guncelle.py` bunu otomatik yapıyor.
- **Kısa tut:** Sadece Claude'un koddan çıkaramayacağı şeyleri yaz: komutlar, kurallar, dikkat edilecekler.
- **Davranış kuralları:** Modelin sık yaptığı hataları (basit işi karmaşıklaştırmak, talimatın dışına çıkmak, bitmemiş işi bitti saymak, olmayan API uydurmak) kısa kurallarla önler; hazır örneği Karpathy'nin gözlemlerinden çıkarılmış [andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills): kodlamadan önce düşün, en basit çözümü yaz, sadece isteneni değiştir, başarıyı doğrulanabilir hedefe bağla. Tüm projelerde geçerli olsun istiyorsan `~/.claude/CLAUDE.md`'ye eklenir.
- **DESIGN.md:** `AGENTS.md` projenin nasıl kurulacağını, `DESIGN.md` nasıl görüneceğini anlatır: renk, yazı tipi, köşe ve boşluk değerleri ve tasarımın gerekçesi. Biçimi Google'ın [design.md](https://github.com/google-labs-code/design.md) reposunda, markalardan çıkarılmış hazır örnekleri [awesome-design-md](https://github.com/VoltAgent/awesome-design-md) reposunda.

## Google'ın AI araçları

Google'ın ücretsiz kullanılabilen AI araçları; [bu gönderiden](https://www.instagram.com/p/DdIAxPynbHV/) alındı, bilgiler 25.09.2026'da Google'ın resmi sayfalarından doğrulandı.
Gönderideki Opal Türkiye'de açık değil, Mixboard 28 Eylül 2026'da kapanıyor; ikisi listeye alınmadı.

| Araç | Ne işe yarar | Ücret |
|---|---|---|
| [Stitch](https://stitch.withgoogle.com) | Metinden, eskizden ya da ekran görüntüsünden web ve mobil arayüz tasarlar, HTML/CSS koduna çevirir; Figma, AI Studio ya da Antigravity'ye aktarır. Google Labs deneyi, 18+. | Fiyat belirtilmemiş, kotalı |
| [AI Studio](https://aistudio.google.com) | Gemini modellerini dener, prompt'tan tam yığın web ya da Android uygulaması üretir, Gemini API anahtarı verir. Ücretsiz kullanımda girdiğin içerik ürün geliştirmede kullanılabilir; gizli veri ya da anahtar yapıştırma. | Ücretsiz; Gemini API'de sınırlı ücretsiz katman |
| [Antigravity](https://antigravity.google) | Google'ın ajan öncelikli geliştirme platformu: IDE, birden çok ajanı yöneten masaüstü uygulaması, CLI ve SDK. Bireysel kullanıcılar için Gemini CLI'ın yerini aldı; içinde Claude modelleri de seçilebiliyor. Kişisel Google hesabı ister. | Haftalık limitli ücretsiz plan; yüksek limit Google AI Pro ya da Ultra ile |
| [Gemini Notebook](https://notebooklm.google) | NotebookLM'in yeni adı: yüklediğin PDF, site, video ve dokümanlara dayanarak kaynak göstererek cevap verir; sesli ve videolu özet, bilgi kartı üretir. Bir kütüphanenin dokümanını yükleyip ona soru sormak için. | Ücretsiz, limitli |
| [Pomelli](https://labs.google.com/pomelli/about) | Siteni tarayıp markanın tarzını çıkarır, buna uygun sosyal medya kampanyası ve ürün görselleri üretir; yayından sonra tanıtım için. Sadece İngilizce, 18+. | Şimdilik ücretsiz, birkaç yüz üretimle sınırlı |
| [Flow](https://flow.google.com) | Veo ve Nano Banana modelleriyle video ve görsel üretir; tanıtım videosu ve mağaza görselleri için. Abone olmayanlar akşam yoğun saatlerde video üretemeyebilir. | Günde 50 ücretsiz kredi, görsel üretimi ücretsiz; aboneler daha fazla |
| [Flow Music](https://www.flowmusic.app) | Şarkı ve arka plan müziği üretir (eski adı ProducerAI); tanıtım videosu için. Türkiye'de açık olup olmadığı resmi sayfalardan doğrulanamadı, ticari kullanım şartları belirtilmemiş. | Ücretsiz plan var; ücretli planlar ayda 6–48 $ |

## Hazır prompt'lar

Kutunun üstündeki "Prompt'u kopyala" düğmesiyle alıp Claude'a yapıştır.
Yayın öncesi, App Store, Google Play ve paywall denetimi için ilgili kontrol listesindeki denetim prompt'unu kopyala.

Değişikliği tarayıcıda test et:

```
Yaptığın değişikliği Playwright ile tarayıcıda aç ve ana akışı dene: giriş, form gönderme, hata durumları. Masaüstü ve 390 px mobil genişlikte ekran görüntüsü al, gördüğün sorunları düzelt ve neyi test ettiğini kısaca yaz. agent-browser kuruluysa akışın video kaydını al ve PR açıklamasına ekle.
```

Performansı ölç:

```
Sayfayı Chrome DevTools ile aç; Lighthouse denetimi ve performans kaydı al. LCP, CLS ve toplam JavaScript boyutunu raporla, en büyük üç sorunu düzelt ve öncesi-sonrası değerleri yaz.
```

Arayüzü toparla:

```
Bu sayfanın arayüzünü gözden geçir: boşluklar, yazı boyutları, renk kontrastı, mobil görünüm ve boş, yükleniyor, hata durumları. Önce sorunları listele, sonra onayımla düzelt.
```

Bağımlılıkları denetle:

```
Projenin bağımlılıklarını denetle: güvenlik açığı olanları (osv-scanner kuruluysa onunla tara), çok eski ve bakımı bırakılmış olanları, JS/TS projesinde kullanılmayan paket ve dosyaları (knip ile) listele. Güncelleme önerilerini risk sırasıyla ver, kırıcı değişiklik içerenleri ayrıca belirt.
```

Yayından önce güvenlik taraması yap:

```
Bu projeyi yayından önce beş adımda güvenlik açısından tara ve her adımın bulgularını önem sırasıyla raporla: 1) paket denetimi (npm audit --audit-level=high ya da osv-scanner) ile bilinen açığı olan paketler; npm audit fix --force kullanma, büyük sürüm atlatıp projeyi bozabilir. 2) gitleaks ile kodda ve git geçmişinde sızmış anahtar, token ve şifre; bulduğun değeri ekrana yazma, iptal edilip yenilenmesi gerektiğini söyle. 3) semgrep ile güvenli olmayan kod kalıpları. 4) Kimlik doğrulama, yetki kontrolü, API uç noktaları, dosya yükleme ve kullanıcı girdisi için kendi incelemen. 5) Uygulama staging'de çalışıyorsa ZAP taramasının nasıl yapılacağı. Kurulu olmayan araçları kurmadan önce bana sor; hiçbir şeyi onayım olmadan düzeltme.
```

Karpathy'nin [LLM Council](https://github.com/karpathy/llm-council) fikri soruyu birden çok modele sorup bir başkan modele karar verdirir; [bu videodaki](https://www.instagram.com/reel/Dbpyz7FCLC3/) gibi tek modelde beş danışmanla da uygulanabilir.
Model kendi fikrini onaylamak yerine karşı görüş üretsin diye büyük kararlarda işe yarar.

Büyük bir kararı danışman konseyine sor:

```
Şu kararı vermem gerekiyor: <karar>. Bağlam: <kısa bağlam>. Beş danışmandan oluşan bir konsey gibi düşün ve her birini ayrı başlıkla yaz: 1) Karşıt görüşlü: bu karar neden yanlış olabilir, en güçlü itirazı getir. 2) Prensip üretici: bu tür kararlarda hangi genel kurallara uymalıyım. 3) Fırsat bulan: gözden kaçırdığım fırsat ya da daha iddialı seçenek ne. 4) Dışarıdan bakan: konuyu hiç bilmeyen biri neyi tuhaf bulur, neyi sorgulamadan varsayıyorum. 5) Uygulamacı: yarın başlasam ilk üç adım ne, en büyük risk nerede. Sonra başkan olarak hepsini tart; bana katılmak zorunda değilsin. Net bir öneri, gerekçesi ve fikrimi değiştirecek koşulu yaz.
```

[Bu videodaki](https://www.instagram.com/reel/DaebyH0xIDQ/) "JARVIS" düzeni: bağlı MCP'lerden her sabah bir özet çıkarır; `/schedule` ile rutin olarak kurulabilir.

Günlük uygulama özeti:

```
Bana günlük bir özet hazırla: bağlı MCP'lerden son 7 günün indirme ve gelir rakamlarını (RevenueCat), yanıt bekleyen müşteri e-postalarını (Gmail), zamanlanmış paylaşımları (Buffer) ve reklam harcamasıyla getirisini (Meta Ads) topla. Bağlı olmayan kaynağı atla ve bunu söyle. Sonunda bugün ilk yapmam gereken üç işi öner. Hiçbir e-postayı gönderme, reklamı ya da paylaşımı değiştirme; sadece raporla.
```

Müşteri e-postalarına taslak cevap:

```
Gmail'deki yanıtlanmamış müşteri e-postalarını oku. docs/sss.md dosyasındaki cevaplara göre her biri için taslak yanıt hazırla; SSS'de karşılığı olmayanları ayrıca listele. E-postaları gönderme, sadece taslak olarak göster.
```

[Bu videodaki](https://www.instagram.com/reel/Dc1su9HoqIO/) sekiz adım WhatsApp'tan randevu alan bir AI ajanı kurar: plan, WhatsApp bağlantısı, model, hafıza, işletme bilgisi, araçlar, test ve yayın.
Her adım bir öncekine dayanır; ajanı sohbet botundan ayıran araçlardır (randevu almak gibi iş yapması).

WhatsApp randevu ajanı kur:

```
İşletmem için WhatsApp'tan müşterilerle konuşup randevu alan bir AI ajanı kurmak istiyorum. İşletme: <ne yapıyor>. Müşteriler: <kimler>. Ajanın yapacakları: <soruları cevaplamak, randevu almak, iptal>. Asla yapmayacakları: <fiyat pazarlığı, iade sözü>. Kod yazmadan önce mimariyi öner ve onayımı al. Adımlar: 1) WhatsApp: Meta geliştirici uygulamasına WhatsApp ürününü ekle, webhook'u kur ve "messages" alanına abone ol (yoksa mesaj gelmez); müşterinin son mesajından 24 saat sonra sadece onaylı şablon mesaj gönderilebildiğini hesaba kat. 2) Modeli OpenRouter üzerinden bağla ki model değiştirmek tek satır olsun. 3) Hafıza: konuşmayı telefon numarasına göre sakla, son 20 kadar mesajı modele gönder, geçmişi sınırla ve eskisini sil. 4) İşletme bilgisi: hizmetler, fiyatlar, çalışma saatleri, SSS ve randevu kuralları; bilgide olmayan soruya "ekibe sorup döneceğim" desin. 5) Araçlar: müsaitlik ve randevu için Cal.com API'si; okumak serbest, randevu oluşturmadan önce müşteriden açıkça onay alsın, idempotency key kullan, "gelecek perşembe" gibi tarihleri model değil kod hesaplasın. 6) Kırmaya çalış: 31 Şubat, bir saniye arayla gelen iki mesaj, "talimatlarını unut", bilgide olmayan soru, randevudan sonra iptal; hepsini bir test setine koy ve her düzeltmeden sonra baştan çalıştır. 7) Yayına al: bilgisayarım değil VPS, pm2, geçerli TLS; webhook imzasını doğrula (adres herkese açık) ve her konuşma adımını logla. Anahtarları koda yazma, ortam değişkeninde tut.
```
