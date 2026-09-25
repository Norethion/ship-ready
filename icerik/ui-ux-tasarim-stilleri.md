# UI/UX: stiller ve araçlar

<!-- sira: 4 -->
<!-- grup: Rehberler -->
<!-- ikon: palette -->

<!-- yan-yana -->

Claude'a arayüz yaptırırken stilin İngilizce adını prompt'a yazmak yeterli, örneğin "Bento Grid düzeninde, Glassmorphism kartlarla bir özellik sayfası".
İşe yarayan tasarım skill'leri: [Impeccable](https://github.com/pbakaus/impeccable), [Taste Skill](https://github.com/Leonxlnx/taste-skill), [UI/UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill).
Arayüzün her sayfada aynı kalması için projeye bir `DESIGN.md` koy: renkleri, yazı tiplerini ve boşlukları tanımlar, ajan arayüzü buna göre üretir; hazır örnekler [awesome-design-md](https://github.com/VoltAgent/awesome-design-md) reposunda.

## Stiller

| Stil | Nasıl görünür | Nerede işe yarar |
|---|---|---|
| Claymorphism | Kil ya da hamurdan yapılmış gibi şişkin, yumuşak 3B şekiller; iç ve dış yumuşak gölgeler, pastel renkler, çok yuvarlak köşeler. | Eğlenceli uygulamalar, eğitim ve çocuk ürünleri, ikon ve illüstrasyonlar |
| Cybercore | Erken internet ve dijital dünya estetiği: ikili kod, piksel grafikler, eski işletim sistemi pencereleri, parlak mavi ve yeşil. | Teknoloji meraklısı kitle, etkinlik ve kampanya sayfaları |
| Neo-Brutalism | Kalın siyah kenarlıklar, bulanıklığı olmayan sert gölgeler, doygun düz renkler, bilerek "ham" bırakılmış görünüm. | Startup ve ürün tanıtımı, genç kitleye hitap eden markalar |
| Scrapbook | Karalama defteri kolajı: yırtık kâğıt, bant, çıkartma, el yazısı, polaroid fotoğraflar. | Kişisel blog, portfolyo, etkinlik, hobi markaları |
| Surrealism | Rüya gibi, mantık dışı kompozisyonlar; beklenmedik nesne birleşimleri, gerçeküstü 3B sahneler. | Sanat projeleri, kampanya ve açılış (hero) görselleri, marka hikâyesi |
| Y2K Aesthetic | 2000'lerin başı: krom ve metalik yüzeyler, holografik gradyanlar, kabarcık yazılar, parlak pembe ve mavi. | Moda, müzik, genç kitle |
| Pixel Art | Piksel piksel çizilmiş düşük çözünürlüklü grafikler, bitmap fontlar, retro oyun hissi. | Oyunlar, nostaljik markalar, eğlenceli küçük etkileşimler |
| Synthwave | 80'ler retro-fütürizmi: neon pembe, mor ve turkuaz, gün batımı, ızgara zemin, krom yazılar. | Müzik, oyun, etkinlik sayfaları |
| Glassmorphism | Buzlu cam paneller: yarı saydam yüzey, arkasını bulanıklaştırma, ince açık kenarlık, renkli arka plan. Metnin okunabilirliğine dikkat. | Dashboard kartları, modal ve açılır pencereler, iOS/macOS benzeri arayüzler |
| Neumorphism | Arka planla aynı renkte, açık ve koyu iki gölgeyle kabartılmış ya da gömülmüş öğeler. Kontrast düşük olduğu için erişilebilirlik zayıf. | Kontrol panelleri, akıllı ev ve müzik çalar arayüzleri; küçük alanlarda |
| Bento Grid | Farklı boyutlarda, yuvarlak köşeli kutulardan oluşan ızgara; Apple'ın tanıtım sayfalarındaki gibi. | Özellik tanıtımı, dashboard, portfolyo |
| Editorial Design | Dergi ve gazete düzeni: güçlü başlık hiyerarşisi, çok sütun, büyük görseller, bol beyaz alan. | Blog, haber ve içerik siteleri, vaka çalışmaları |
| Swiss Design | Katı ızgara, sans-serif fontlar (Helvetica tarzı), asimetrik ama düzenli yerleşim, az renk, net hiyerarşi. | Kurumsal siteler, ajanslar, bilgi yoğun sayfalar |
| Minimalism | Az öğe, bol boşluk, sınırlı renk paleti; sadece gerekeni gösterir. | SaaS ve ürün sayfaları, portfolyo; çoğu proje için güvenli varsayılan |
| Maximalism | Bilinçli fazlalık: yoğun renk, desen ve katman, karışık fontlar, cesur kompozisyon. | Moda, sanat, yaratıcı ajanslar, dikkat çekmesi gereken kampanyalar |
| Luxury Typography | İnce serif fontlar, geniş harf aralığı, büyük başlıklar, siyah-beyaz-altın, bol boşluk. | Lüks ürün, otel, parfüm, mücevher, emlak |
| Conceptual Sketch | Elle çizilmiş eskiz görünümü: kalem çizgileri, taslak ikonlar, kâğıt dokusu. | Fikir ve süreç anlatımı, eğitim içerikleri, taslak hissi verilmek istenen sayfalar |
| Ethereal | Rüya gibi hafif ve havadar: soluk pastel tonlar, yumuşak ışık ve gradyanlar, bulanıklık. | Sağlık ve wellness, güzellik, meditasyon |
| Bohemian | Doğal ve el yapımı hissi: toprak tonları, organik dokular, bitki ve desen motifleri, el yazısı fontlar. | El yapımı ürünler, kafe, yoga, seyahat |
| Victorian | 19. yüzyıl süslemesi: süslü serif fontlar, çerçeveler, gravür illüstrasyonlar, bordo, koyu yeşil ve altın. | Tarihi markalar, kitapçı, özel etkinlik, vintage ürünler |
| Cyberpunk | Distopik gelecek: koyu zemin, neon sarı, camgöbeği ve pembe, glitch efektleri, HUD tarzı arayüz çizgileri. | Oyun, teknoloji ürünleri, etkinlik |
| Wabi-Sabi | Japon "kusurun güzelliği" estetiği: doğal malzeme dokuları, asimetri, sade toprak renkleri, sakinlik. | Seramik ve el işi, mimari, çay ve kahve markaları |

## Siteler ve kütüphaneler

React dışı bir projede (Vue, Angular, Blazor, mobil) bileşen kütüphaneleri doğrudan kurulamaz ama örnek alınabilir.
Beğendiğin bileşenin kodunu Claude'a verip "bunu kendi altyapıma çevir" demek yeterli.

| Site | Tür | Ne işe yarar | Altyapı | Başka altyapıda | Ücret |
|---|---|---|---|---|---|
| [21st.dev](https://21st.dev/) | Bileşen kütüphanesi | 12.000'den fazla React ve Tailwind bileşeni, şablon ve shadcn teması; canlı önizlemeli. Bileşen shadcn CLI ile tek komutla projeye kopyalanır, kod senin olur. | React + Tailwind, shadcn kurulu proje (Next.js ya da Vite) | Doğrudan kurulmaz; örnek alınıp çevrilir | Gezinmek ücretsiz, günde 2 kopyalama; sınırsız kopyalama ve 21st AI ücretli |
| [Aceternity UI](https://ui.aceternity.com/) | Bileşen kütüphanesi | React, Tailwind ve Motion ile yapılmış 200'den fazla animasyonlu bileşen, blok ve şablon. Kopyala-yapıştır ya da shadcn ile eklenir. | React + Tailwind + Motion (Next.js ya da Vite) | Doğrudan kurulmaz; örnek alınıp çevrilir. Animasyonlar Motion kütüphanesine bağlı olduğu için çevirmek daha çok emek ister | Bileşenlerin bir kısmı ücretsiz, hazır blok ve şablonlar ücretli (All-Access Pass) |
| [Kinetics](https://kinetics.colorion.co) | Animasyon | Yay fiziğiyle çalışan 153 arayüz animasyonu: buton, slider, sürükleme, form, yükleniyor, liste, modal. Sertlik ve sönümü ayarlayıp CSS, React ya da hazır AI prompt'u olarak kopyalarsın. | Her web projesi (düz CSS); React bileşeni olarak da alınır | CSS hâli her web altyapısında çalışır; mobil gibi web dışı ortamlar için hazır AI prompt'u kullanılır | Ücretsiz, açık kaynak |
| [Animated Buttons](https://animatedbuttons.colorion.co) | Animasyon | Sadece CSS ile yapılmış 99 hover efektli buton; JavaScript ya da bağımlılık yok, kopyala-yapıştır. | Her web projesi: düz HTML, React, Vue, Angular, Blazor, PHP | Web dışında (mobil) sadece örnek alınır | Ücretsiz, MIT lisansı |
| [VibePrompt](https://vibeprompts.dev) | Prompt kütüphanesi | 15 kategoride 286'dan fazla arayüz prompt'u ve Tailwind kodu: giriş formu, dashboard, yorumlar vb. Prompt'u AI aracına yapıştırıp bileşeni ürettirirsin. | Tailwind kullanan her proje (HTML, React, Vue, Svelte) | Tailwind yoksa prompt'a kendi altyapını yazarsın ("Bootstrap ile", "düz CSS ile") | Ücretsiz |
| [MotionSites](https://motionsites.ai/) | Prompt kütüphanesi | Claude, Lovable, Bolt, Cursor gibi AI site yapıcılar için hazır prompt'lar; landing page, portfolyo ve 3B siteler. | Altyapıdan bağımsız; çıkan kod kullandığın AI aracına bağlı | Prompt'a altyapıyı eklemen yeterli ("Vue 3 ile", "düz HTML ile") | Bir kısmı ücretsiz, sınırsız erişim ücretli |
| [Stitch](https://stitch.withgoogle.com) | Arayüz tasarımı (AI) | Google'ın aracı: metinden, eskizden ya da ekran görüntüsünden web ve mobil arayüz tasarlar, HTML/CSS koduna çevirir; Figma'ya, AI Studio'ya ya da Antigravity'ye aktarır. | Her proje: çıktı HTML/CSS | Kodu Claude'a kendi altyapına çevirttirirsin | Fiyat belirtilmemiş, kotalı; Google Labs deneyi, 18+ |
| [Forma - Icon Creator](https://iconcreator.dev) | İkon | Tabler, Lucide, Phosphor, Iconoir ve Heroicons ikonlarından uygulama ikonu tasarlayıp SVG ya da PNG olarak indirirsin. | Her proje: SVG ve PNG web, mobil ve masaüstünde kullanılır (uygulama ikonu, favicon) | Fark yok | Sitede belirtilmemiş |
| [Invoice Generator](https://invoicegenerator.io) | Fatura (UI dışı) | Tarayıcıda fatura hazırlayıp PDF indirirsin; veriler cihazında kalır, sunucuya gönderilmez. 30'dan fazla para birimi, vergi, indirim, kargo alanları. | Kod değil; tarayıcıda doğrudan kullanılan araç | Uygulamana fatura ekranı yapacaksan düzeni örnek alınabilir | Ücretsiz, üyelik ve filigran yok |
| [shadcn/ui](https://github.com/shadcn-ui/ui) | Bileşen kütüphanesi | Kodu doğrudan projeye kopyalanan, erişilebilir bileşenler; CLI ile eklenir. 21st.dev ve Aceternity bileşenleri de shadcn CLI ile eklenir. | React + Tailwind (Next.js, Vite, Remix, Astro, TanStack, Laravel) | Doğrudan kurulmaz; örnek alınıp çevrilir | Ücretsiz, MIT |
| [Magic UI](https://github.com/magicuidesign/magicui) | Animasyonlu bileşen | Landing page ve tanıtım sayfaları için animasyonlu, kopyala-yapıştır bileşenler; kurulumu shadcn/ui ile aynı. | React + Tailwind + Motion | Doğrudan kurulmaz; örnek alınıp çevrilir | Ücretsiz, MIT |
| [React Bits](https://github.com/DavidHDev/react-bits) | Animasyonlu bileşen | Metin animasyonu, arka plan ve mikro etkileşim için 200'den fazla bileşen; her biri JS/TS ve düz CSS ya da Tailwind hâliyle gelir. | React (CSS ya da Tailwind) | Vue ve Svelte için resmi portları ayrı sitelerde | Ücretsiz; MIT + Commons Clause: sitende ticari kullanım serbest, bileşenleri satmak ya da yeniden dağıtmak yasak |
| [daisyUI](https://github.com/saadeghi/daisyui) | Tailwind eklentisi | Tailwind'e eklenti olarak kurulur, `btn`, `card` gibi hazır CSS sınıflarıyla kullanılır. | Tailwind çalışan her proje: React, Vue, Svelte, Angular, Laravel, Django, Rails | Tailwind yoksa kullanılamaz | Ücretsiz, MIT |
| [Tremor](https://github.com/tremorlabs/tremor) | Grafik ve dashboard | Grafik ve dashboard için 35'ten fazla kopyala-yapıştır bileşen; grafikleri Recharts ile çizer. | React + Tailwind + Radix | Doğrudan kurulmaz; örnek alınır | Ücretsiz, Apache-2.0; Tremor Vercel'e katıldı, kodu Nisan 2025'ten beri güncellenmiyor |
| [Motion](https://github.com/motiondivision/motion) | Animasyon | Framer Motion'ın yeni adı: yaylı animasyonlar, sayfa düzeni geçişleri, kaydırmaya bağlı efektler, sürükleme. Aceternity ve Magic UI bileşenleri bunu kullanır. | React, düz JavaScript, Vue | Web dışında kullanılmaz | Çekirdek ücretsiz, MIT; Motion+ ücretli |
| [GSAP](https://github.com/greensock/GSAP) | Animasyon | Bağımlılıksız animasyon kütüphanesi; ScrollTrigger, SplitText, MorphSVG gibi eklentiler dahil, React için `useGSAP`. | Her web projesi: düz JS, React, Vue, SVG, canvas | Web dışında kullanılmaz | Tüm eklentiler dahil ücretsiz, ticari kullanım serbest; açık kaynak değil (GreenSock lisansı) |
| [Lottie Web](https://github.com/airbnb/lottie-web) | Animasyon oynatıcı | After Effects'te yapılıp JSON'a aktarılan animasyonları web'de oynatır. | Her web projesi (düz JS, npm ya da CDN) | Mobil için Lottie'nin iOS ve Android kütüphaneleri ayrı | Ücretsiz, MIT; animasyonu üretmek için After Effects gerekir, bir yıldan uzun süredir güncellenmiyor |
| [Recharts](https://github.com/recharts/recharts) | Grafik | Bileşen tabanlı grafik kütüphanesi; eksen, tooltip, çizgi gibi parçalar ayrı bileşen olarak birleştirilir, SVG ile çizer. | React | Doğrudan kurulmaz; örnek alınır | Ücretsiz, MIT |
| [Thinking Orbs](https://github.com/Jakubantalik/thinking-orbs) | Yükleniyor göstergesi | AI ve ajan arayüzleri için noktalı "düşünen küre" animasyonları: çalışıyor, arıyor, çözüyor, dinliyor, bağlanıyor gibi dokuz durum, sohbet için 64 ve satır içi 20 piksellik iki boyut. Sayfanın açık ya da koyu temasına kendiliğinden uyar; düz 2D canvas ile çizer (WebGL yok), ekrandan çıkınca durur, hareketi azalt tercihinde sabit kare gösterir. | React (`npm install thinking-orbs`) | Doğrudan kurulmaz; örnek alınıp çevrilir | Ücretsiz, MIT |
| [mapcn](https://github.com/AnmolSaini16/mapcn) | Harita | Hazır harita bileşenleri: işaretçi, popup, rota, zoom ve pusula; shadcn/ui ile aynı yapıda. | React + Tailwind, MapLibre GL | Doğrudan kurulmaz; örnek alınır | Ücretsiz, MIT; varsayılan CARTO haritalarının ticari kullanımı lisans ister, OpenStreetMap gibi başka sağlayıcıya geçilebilir |

## İlham siteleri

Tasarıma başlarken ve takıldığında bakılan siteler; [bu gönderiden](https://www.instagram.com/p/DdRp-ZSCKeH/) alındı.
Beğendiğin örneği kaydet ve neden beğendiğini not al; düzeni değil fikri al.

| İlham | Ne var | Ücret |
|---|---|---|
| [Recent](https://recent.design) | Her gün güncellenen seçilmiş tasarım örnekleri: web sayfaları, marka, ürün ekranları, tipografi, hareket (motion), 3B. Eski adı Godly; godly.website adresi buraya yönlenir. | Ücretsiz |
| [Saaspo](https://saaspo.com) | Sadece SaaS siteleri; sayfa türüne (landing, fiyatlandırma, ürün, hakkında...), bölüme ve kullanılan altyapıya (Webflow, Next.js, Framer...) göre süzülür, OG görselleri de var. | Ücretsiz, haftalık bülten |
| [Awwwards](https://www.awwwards.com/websites/) | Jürinin ödüllendirdiği siteler ve yıllar öncesine uzanan "günün sitesi" arşivi; kategori, teknoloji (React, Webflow, Three.js), yazı tipi ve etikete göre süzülür. | Gezinmek ücretsiz; kurslar ve Pro üyelik ücretli |
| [Pinterest](https://www.pinterest.com) | "web design", "dashboard ui" gibi aramalarla geniş görsel arşiv; beğendiklerini panolara kaydedersin. | Ücretsiz |
| [X](https://x.com) | Tasarımcı ve geliştiricilerin yeni işlerini paylaştığı akış; beğendiğin kişileri bir listede toplarsın. | Ücretsiz |

## Tehlikeli işlemler

Silme gibi geri alınamaz işlemler için altı arayüz kalıbı; [bu videodan](https://www.instagram.com/reel/Da4-EmYNYAP/) alındı.

| Kalıp | Ne yapmalı | Neden |
|---|---|---|
| Basılı tutarak onayla | "Emin misin?" penceresi yerine düğmeyi kısa bir süre basılı tutturup halka dolunca sil; erken bırakılırsa hiçbir şey olmaz. | Onay pencereleri alışkanlıkla okunmadan geçilir. |
| İşi adıyla yaz | Düğmelerde "Evet" ve "Hayır" yerine "Projeyi sil" ve "Projeyi tut" yaz. | Fiil, uyarının kendisidir. |
| Ana yoldan uzak tut | Sil düğmesini ana düğmenin yerine koyma; kaydet ya da iptal ana yerde kalsın, sil ayrı ve uzakta dursun. | Kas hafızası okumadan tıklar. |
| Kırmızıyı idareli kullan | Kırmızıyı sadece yıkıcı işlemlere ayır; uyarı, bildirim ve açık-kapalı düğmelerinde kullanma. | Her yer kırmızıysa gerçek tehlike fark edilmez. |
| Tehlikeli bölge | Hesap ya da proje silme, sahipliği devretme gibi işlemleri ayarlar sayfasının en altında, çerçeveli ve başlıklı bir "Tehlikeli bölge"de topla. | Konum sürtünme yaratır; oraya yanlışlıkla gidilmez. |
| Vazgeçme süresi | Hesap silmeyi hemen yapma; örneğin 14 gün sonra kalıcı sil, bu sürede tek tıkla iptal ettir. | Son savunma hattı; süre dolunca veri yine gerçekten silinmeli ([yayın öncesi {{no:yo-hesap-silme}}. madde](yayin-oncesi-maddeler.md)). |

## Etkileşim örnekleri

Instagram'da görülen, kodu paylaşılmamış etkileşimler; kartın prompt'u etkileşimi projenin kendi altyapısında yaptırır.

| Etkileşim | Nasıl çalışır | Nerede işe yarar | Kaynak |
|---|---|---|---|
| Sıvı sekme çubuğu | Seçili sekmenin üstünde bir damla durur, çubuk damlanın etrafında eriyormuş gibi kıvrılır ve hiç kırışmaz; damla çubuk boyunca sürüklenebilir. HTML, CSS ve JavaScript ile yapılmış. | Web ve mobil alt menü, sekme geçişi | [video](https://www.instagram.com/reel/DbfG6fuPE9y/) |
| Yeni alt menü fikirleri | On mobil alt menü: sıvı yüzen çubuk, mıknatıslı dock, cam kapsül, bölümlü dinamik çubuk, yörüngeli menü, dalgalı gösterge, neon dock, biçim değiştiren damla, katmanlı kartlar, sade dock. | Mobil uygulamanın alt menüsü | [video](https://www.instagram.com/reel/DcNLxSRz08-/) |
| Animasyonlu ödeme ekranı | Kart bilgisi yazıldıkça kart önizlemesi dolar, CVC alanına gelince kart arkası görünecek şekilde döner; ödeme sırasında kart parlar, sonra başarı geçişi gelir. React ve Motion ile yapılmış. | Ödeme ve abonelik ekranı | [video](https://www.instagram.com/reel/Dac7xfXzudX/) |
| Fiş yazdırma | "Fişi yazdır"a basınca fiş yazıcıdan kayarak çıkar ve üstüne "ÖDENDİ" damgası vurulur; yeniden yazdırma, fişi koparma ve kopyalama düğmeleri var. | Ödeme sonrası onay, makbuz ve fatura ekranı | [video](https://www.instagram.com/reel/Dcptq4cI68U/) |
| Kilitli şifre gücü göstergesi | Şifre güçlendikçe simge açık kapıdan ataşa, asma kilide, sürgülü kilide ve kasa kapısına döner; şifrenin entropisini (bit) ve tahmini kırılma süresini yazar, "Güçlü öner" düğmesi şifre üretir. GSAP ile yapılmış. | Kayıt ve şifre değiştirme formu | [video](https://www.instagram.com/reel/DayJ5FBPbmb/) |
| Akıcı giriş formu | Logo çizilerek açılır; Giriş ve Kayıt sekmeleri, alanın altında anında hata mesajı, giriş düğmesinde yükleniyor simgesinden onay işaretine geçiş. Flutter ile yapılmış. | Mobil giriş ve kayıt ekranı | [video](https://www.instagram.com/reel/Ddg450QpmE2/) |
| Etkileşimli dashboard | Cam görünümlü istatistik kartları üzerine gelince hafifçe yükselir; grafik, görev ve işlem listeleri kartlarda toplanır, mobilde alt alta dizilir. React, Motion ve Lucide ikonlarıyla yapılmış. | Yönetim paneli, analitik ekranı | [video](https://www.instagram.com/reel/Ddf-7oiz126/) |

## Renk çiftleri

Yazı ve zemin için altı renk çifti; [bu videodan](https://www.instagram.com/reel/Da7hPcluJUV/) alındı.
Kontrast oranları WCAG formülüyle hesaplandı; hepsi normal metin için gereken 4,5:1 sınırını geçiyor.

| Renk çifti | Renkler | Kontrast |
|---|---|---|
| <span class="pair" style="color:#0057FF;background:#F8F7F4"></span> Signal Blue + Porcelain | Yazı `#0057FF`, zemin `#F8F7F4` | 5,1:1 (AA) |
| <span class="pair" style="color:#3A0CA3;background:#FFF275"></span> Butter Yellow + Royal Iris | Yazı `#3A0CA3`, zemin `#FFF275` | 10,3:1 (AAA) |
| <span class="pair" style="color:#B6FF2E;background:#23262F"></span> Lime Spark + Graphite | Yazı `#B6FF2E`, zemin `#23262F` | 12,5:1 (AAA) |
| <span class="pair" style="color:#FF4696;background:#1E1033"></span> Dragonfruit + Night Violet | Yazı `#FF4696`, zemin `#1E1033` | 5,6:1 (AA) |
| <span class="pair" style="color:#064E3B;background:#F8E7C9"></span> Emerald Ink + Champagne | Yazı `#064E3B`, zemin `#F8E7C9` | 8,0:1 (AAA) |
| <span class="pair" style="color:#6A00F4;background:#FFD6A5"></span> Ultra Violet + Soft Apricot | Yazı `#6A00F4`, zemin `#FFD6A5` | 5,3:1 (AA) |
