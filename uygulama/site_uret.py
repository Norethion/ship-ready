"""Starlight sitesinin içeriğini çekirdekten (uygulama/katalog.py) üretir. Üretilenler elle düzenlenmez:
  site/src/content/docs/   sayfalar (kontrol listeleri, rehberler, repo kataloğu, genel bakış)
  site/src/data/           katalog.json (bileşenler için) ve sidebar.json (kenar menü)
  site/public/             katalog.json, llms.txt ve llms-full.txt (AI'lar için)
  site/src/yerel/          sadece yerel sayfanın verisi: raporlar, raporlu kenar menü, arama dizini
Herkese açık site (npm run build) raporları içermez. Yerel sayfa aynı sitenin SHIP_YEREL=1 ile derlenmiş hâlidir:
guncelle.py onu sayfa/ klasörüne derler, index.html oraya yönlendirir ve sunucusuz, çift tıklamayla açılır.

Kullanım: python uygulama/site_uret.py   (guncelle.py de her çalıştığında çağırır)
Siteyi görmek: site/ klasöründe  npm run dev   ya da  npm run build && npm run preview
"""
import datetime, json, re, shutil, sys, unicodedata
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
import katalog

ROOT = katalog.ROOT
SITE = ROOT / "site"
DOCS = SITE / "src" / "content" / "docs"
DATA = SITE / "src" / "data"
PUBLIC = SITE / "public"
LINKS = ROOT / "veri" / "linkler.json"
LOCAL = SITE / "src" / "yerel"
LINK = re.compile(r"\[([^\]]*)\]\(([^)\s]+)\)")
DESCRIPTION = "AI ile kişisel proje geliştirip yayına çıkarırken başvurulan Türkçe kontrol listeleri, rehberler ve doğrulanmış araçlar."
# Kartın prompt düğmesi tablonun ilk sütun başlığına göre seçilir; tanınmayan tablolar araç sayılır.
CARD_PROMPTS = {
    "Stil": ("Bu stilde tasarla", "tasarim", lambda t, d, u: f'Bu arayüzü "{t}" stilinde yeniden tasarla. Stilin özellikleri: {d} Mevcut işlevleri, içeriği ve erişilebilirliği (kontrast, klavye kullanımı) koru.'),
    "Kalıp": ("Bu kalıbı uygula", "tasarim", lambda t, d, u: f'Bu projede "{t}" arayüz kalıbını uygula: {d} Önce silme gibi geri alınamaz işlemlerin olduğu ekranları bul ve kalıba uymayanları listele, sonra onayımla düzelt.'),
    "Renk çifti": ("Bu renklerle dene", "tasarim", lambda t, d, u: f'Bu arayüzde "{t}" renk çiftini dene ({d}). Renkleri tema değişkeni olarak tanımla, kontrastı WCAG AA sınırının altına düşürme ve önce hangi öğelere uygulayacağını göster.'),
    "İlham": ("Bu fikri uyarla", "tasarim", lambda t, d, u: f'{t}{f" ({u})" if u else ""} sitesinden beğendiğim bir örneği ekran görüntüsü ya da adresiyle vereceğim. Düzeni birebir kopyalama; beğendiğim fikri (renk, tipografi, boşluk, hareket, bölüm akışı) bu projenin tasarımına ve altyapısına uyarla. Önce hangi fikri hangi ekrana uygulayacağını göster.'),
    "Etkileşim": ("Bu etkileşimi yap", "tasarim", lambda t, d, u: f'Bu projede "{t}" etkileşimini yap: {d} Projenin altyapısına uygun animasyon yolunu seç (web\'de CSS ya da projede varsa Motion veya GSAP, mobilde platformun kendi animasyonları), hareketi azalt tercihinde animasyonu kapat ve önce hangi ekrana uygulayacağını göster.'),
    "Hareket": ("Bu hareketi ekle", "tasarim", lambda t, d, u: f'Bu projeye "{t}" hareket türünü ekle: {d} Önce hareketin anlam katacağı yerleri öner; hareketi süs için değil geri bildirim için kullan, projenin altyapısına uygun yolu seç (web\'de CSS ya da projede varsa Motion veya GSAP), hareketi azalt tercihinde kapat.'),
    "İşaret": ("Bu işareti temizle", "tasarim", lambda t, d, u: f'Bu projenin arayüzünde "{t}" işaretini ara: {d} Bulduğun her yeri dosya ve satırıyla listele, hangisinin bilinçli bir tasarım kararı olduğunu bana sor; kalanları onayımla bu ürüne özgü bir tasarımla değiştir.'),
    # Prompt tablosunda açıklama sütunu prompt'un kendisidir; düğme onu olduğu gibi kopyalar.
    "Prompt": ("Prompt'u kopyala", "tasarim", lambda t, d, u: d),
}
TOOL_PROMPT = ("Kullanım prompt'u", "kullanim", lambda t, d, u: f"{t}{f' ({u})' if u else ''} aracını bu projede kullanmak istiyorum. Ne işe yarar: {d} Önce projenin altyapısına bak; doğrudan kullanılabiliyorsa nasıl ekleneceğini göster, kullanılamıyorsa hangi kısmının örnek alınabileceğini söyle.")


def route(doc):
    return f"/listeler/{doc['liste']}/" if doc["liste"] else f"/rehberler/{Path(doc['dosya']).stem}/"


def js(value):
    """MDX bileşen özelliği; JSON dizesi tırnak ve süslü parantez sorunu çıkarmaz."""
    return "{" + json.dumps(value, ensure_ascii=False) + "}"


def esc(text):
    """Kod parçaları dışındaki {, } ve < karakterlerini MDX için kaçırır."""
    parts = re.split(r"(`[^`]*`)", text)
    for i in range(0, len(parts), 2):
        parts[i] = parts[i].replace("{", "\\{").replace("}", "\\}").replace("<", "&lt;")
    return "".join(parts)


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def count(lst):
    return sum(len(s["maddeler"]) for s in lst["bolumler"])


class Translate:
    """Md metnindeki {{no:kimlik}} atıflarını ve md linklerini site adreslerine çevirir.
    Metni atıf içeren bir link doğrudan o maddeye (#kimlik) gider; son kontrolde açılmayan link ⚠ ile işaretlenir."""

    def __init__(self, cat):
        self.docs = {d["dosya"]: d for d in cat["belgeler"]}
        self.numbers = cat["numaralar"]
        list_doc = {d["liste"]: d for d in cat["belgeler"] if d["liste"]}
        self.item_doc = {m["id"]: list_doc[l["id"]] for l in cat["listeler"] for s in l["bolumler"] for m in s["maddeler"]}
        self.broken = json.loads(LINKS.read_text(encoding="utf-8")).get("broken", {}) if LINKS.exists() else {}

    def __call__(self, text):
        def link(m):
            label, href = m.group(1), m.group(2)
            refs = katalog.REF.findall(label)
            if refs and refs[0] in self.item_doc:
                href = route(self.item_doc[refs[0]]) + "#" + refs[0]
            elif href.split("#")[0] in self.docs:
                base, _, anchor = href.partition("#")
                href = route(self.docs[base]) + (f"#{anchor}" if anchor else "")
            elif href in self.broken:
                return f'[{label} ⚠]({href} "Son kontrolde açılmadı ({self.broken[href]})")'
            return f"[{label}]({href})"
        return katalog.resolve(LINK.sub(link, katalog.ITEM_ID.sub("", text)), self.numbers)


def body_lines(text):
    """Başlık satırı ve yalnızca HTML yorumundan oluşan satırlar (direktifler) atılmış gövde."""
    text = re.sub(r"^#\s+.*\n", "", text, count=1)
    return [l for l in text.split("\n") if not re.fullmatch(r"\s*<!--.*-->\s*", l)]


def convert(lines, tr, special):
    """Satırları MDX'e çevirir: kod blokları olduğu gibi kalır, kaynak satırlar çevrilip kaçırılır,
    special(lines, i) bir (üretilen satırlar, sonraki satır) döndürürse üretilen satırlar kaçırılmadan eklenir."""
    out, i, fence = [], 0, False
    while i < len(lines):
        line = lines[i]
        if line.strip().startswith("```"):
            fence = not fence
            out.append(line)
            i += 1
            continue
        if not fence:
            hit = special(lines, i)
            if hit:
                generated, i = hit
                out += generated
                continue
            out.append(esc(tr(line)))
        else:
            out.append(line)
        i += 1
    return out


def table_rows(lines, i):
    heads, rows = katalog.cells(lines[i]), []
    i += 1
    while i < len(lines) and lines[i].lstrip().startswith("|"):
        if not katalog.is_separator(lines[i]):
            rows.append(katalog.cells(lines[i]))
        i += 1
    return heads, rows, i


def front(**kv):
    return "---\n" + "".join(f"{k}: {json.dumps(v, ensure_ascii=False)}\n" for k, v in kv.items() if v is not None) + "---\n"


def summary(text, limit=160):
    """Meta açıklaması: özetin ilk cümlesi, gerekirse kelime sınırında kısaltılmış."""
    first = re.split(r"(?<=[.!?])\s", text, maxsplit=1)[0]
    return first if len(first) <= limit else first[:limit].rsplit(" ", 1)[0] + "…"


def list_page(doc, lst, tr, comp):
    numbered = lst["bicim"] == "liste"
    state = {"lead": False}

    def special(lines, i):
        line = lines[i]
        h = re.match(r"^##\s+(.+)$", line)
        if h:
            out = []
            if numbered and not state["lead"]:
                out += [f"<DenetimPrompt liste={js(lst['id'])} />", ""]
            state["lead"] = True
            title = re.sub(r"\s*\(\d+\)$", "", h.group(1).strip())
            out += [esc(line), ""]
            if numbered and any(s["baslik"] == title for s in lst["bolumler"]):
                out += [f"<DenetimPrompt liste={js(lst['id'])} bolum={js(title)} />", ""]
            return out, i + 1
        m = re.match(r"^(\d+)\.\s+(.*)$", line)
        if m and numbered:
            iid = katalog.ITEM_ID.search(m.group(2)).group(1)
            return [f"<Madde id={js(iid)} no={{{m.group(1)}}}>", "", esc(tr(m.group(2))), "", "</Madde>", ""], i + 1
        if line.lstrip().startswith("|") and katalog.cells(line)[0] == "#":
            heads, rows, nxt = table_rows(lines, i)
            out = []
            for row in rows:
                iid = katalog.ITEM_ID.search(row[0]).group(1)
                no = re.match(r"\d+", katalog.plain(row[0])).group()
                out += [f"<Madde id={js(iid)} no={{{no}}} baslik={js(katalog.plain(row[1]))}>", ""]
                if len(row) > 2:
                    out += [esc(tr(row[2])), ""]
                meta = " · ".join(f"**{h}:** {esc(tr(v))}" for h, v in zip(heads[3:], row[3:]) if v.strip())
                if meta:
                    out += [f'<span class="meta">{meta}</span>', ""]
                out += ["</Madde>", ""]
            return out, nxt
        return None

    body = convert(body_lines(doc["metin"]), tr, special)
    imports = [f"import Madde from '{comp}/Madde.astro';", f"import DenetimPrompt from '{comp}/DenetimPrompt.astro';"]
    return front(title=doc["baslik"], description=summary(doc["ozet"])) + "\n" + "\n".join(imports) + "\n\n" + "\n".join(body).strip() + "\n"


def cards(heads, rows, tr):
    """Tablo satırlarını kart yapar: başlık kısmı, açıklama, alanlar (sütun sırasıyla, boş olsa da yeri korunur), alt şerit.
    Tür sütunu ve bağlantı olan Kaynak sütunu başlığın altında görünür. Kart, kapladığı ızgara satırı sayısını (satir) bilir ki aynı sıradaki
    kartların satırları hizalansın. Bütün satırlarda canlı örnek varsa örnek kartın üstünde, yoksa pencerede açılır."""
    label, kind, make = CARD_PROMPTS.get(heads[0], TOOL_PROMPT)
    all_examples = all(katalog.EXAMPLE.search(r[0]) for r in rows)
    out = ["<Kartlar>", ""]
    for row in rows:
        cell0 = row[0]
        color = re.search(r'<span class="pair" style="color:(#[0-9A-Fa-f]{6});background:(#[0-9A-Fa-f]{6})"></span>', cell0)
        link = re.search(r"\]\((https?://[^)\s]+)\)", cell0)
        title = katalog.plain(cell0)
        fields = [(h, v) for h, v in zip(heads[1:], row[1:]) if h]
        tur = next((v for h, v in fields if h == "Tür"), None)
        # Kaynak bağlantıysa başlığın altına çıkar; düz metinse alan olarak kalır, kaybolmaz.
        source = LINK.search(next((v for h, v in fields if h == "Kaynak"), ""))
        rest = [(h, v) for h, v in fields if h != "Tür" and not (h == "Kaynak" and source)]
        main = rest[0][1] if rest else ""
        meta = rest[1:]
        example = katalog.EXAMPLE.search(cell0)
        # Üstteki satırlar: stil önizlemesi ve canlı örnek ayrı ayrı sayılır (ikisi birden olabilir).
        style, top = heads[0] == "Stil", bool(example and all_examples)
        props = [f"baslik={js(title)}", f"satir={{{int(style) + int(top) + 3 + len(meta)}}}"]
        if link:
            props.append(f"href={js(link.group(1))}")
            if link.group(1) in tr.broken:
                props.append(f"kirik={js(tr.broken[link.group(1)])}")
        if tur:
            props.append(f"tur={js(katalog.plain(tur))}")
        if source:
            props.append(f"kaynak={js({'ad': katalog.plain(source.group(1)), 'url': source.group(2)})}")
        if style:
            props.append(f"onizleme={js(slug(title))}")
        if example:
            props += [f"ornek={js(example.group(1))}", f"ornekYeri={js('ust' if top else 'pencere')}"]
        if color:
            props.append(f"renk={js({'yazi': color.group(1), 'zemin': color.group(2)})}")
        prompt = make(title, katalog.plain(tr(main)), link.group(1) if link else None)
        props += [f"prompt={js(prompt)}", f"promptEtiket={js(label)}", f"promptTur={js(kind)}"]
        out += [f"<Kart {' '.join(props)}>", "", esc(tr(main)) if main.strip() else "<span></span>", ""]
        for i, (h, v) in enumerate(meta):
            cls = "k-alan" + (" ilk" if i == 0 else "") + (" son" if i == len(meta) - 1 else "")
            out.append(f'<span class="{cls}"><span class="k-etiket">{esc(h)}</span><span class="k-deger">{esc(tr(v))}</span></span>')
        out += ["", "</Kart>", ""]
    return out + ["</Kartlar>", ""]


def guide_page(doc, tr, comp):
    lines = body_lines(doc["metin"])
    fm = front(title=doc["baslik"], description=summary(doc["ozet"])) + "\n"
    if not doc["yan_yana"]:
        return fm + "\n".join(tr(l) for l in lines).strip() + "\n", ".md"

    def special(lines, i):
        if lines[i].lstrip().startswith("|"):
            heads, rows, nxt = table_rows(lines, i)
            return cards(heads, rows, tr), nxt
        return None

    body = convert(lines, tr, special)
    imports = [f"import Kartlar from '{comp}/Kartlar.astro';", f"import Kart from '{comp}/Kart.astro';"]
    return fm + "\n".join(imports) + "\n\n" + "\n".join(body).strip() + "\n", ".mdx"


def public_catalog(cat):
    """Siteye ve AI'lara açılan katalog: raporlar ve Türkçe açıklaması ya da kurulum yeri olmayan repolar dışarıda kalır."""
    folders = cat["repolar"].get("folders", [])
    by_file = {d["dosya"]: d for d in cat["belgeler"]}
    list_doc = {d["liste"]: d for d in cat["belgeler"] if d["liste"]}
    repos = [r for r in cat["repolar"]["repos"] if r.get("tr") and r["kurulum"]]
    return {
        "aciklama": "ship-ready kataloğu: kontrol listeleri (maddeler kalıcı kimlikleriyle), rehber öğeleri ve doğrulanmış GitHub repoları. Repolar amaca göre kategori (klasor) ve alt kategoriye (alt_klasor) ayrılır; kategori ve alt kategori adları hem her repoda hem klasorler listesinde yazar.",
        "belgeler": [{"baslik": d["baslik"], "adres": route(d), "grup": d["grup"], "liste": d["liste"], "ozet": d["ozet"]} for d in cat["belgeler"]],
        "listeler": [{"id": l["id"], "baslik": l["baslik"], "adres": route(list_doc[l["id"]]), "bicim": l["bicim"], "bolumler": l["bolumler"]}
                     for l in cat["listeler"]],
        "ogeler": [{**o, "belge": route(by_file[o["belge"]])} for o in cat["ogeler"]],
        "klasorler": [{"id": f["id"], "ad": f["name"], "kisa": f.get("kisa", f["name"]), "aciklama": f.get("aciklama", ""),
                       "alt": [{"id": a["id"], "ad": a["name"]} for a in f.get("alt", []) if any(r.get("f") == f["id"] and r.get("af") == a["id"] for r in repos)]}
                      for f in folders if any(r.get("f") == f["id"] for r in repos)],
        "repolar": [{"repo": r["r"], "klasor": r.get("f"), "alt_klasor": r.get("af"), "kategori": r["kategori"], "alt_kategori": r["alt_kategori"],
                     "kurulum": r["kurulum"], "aciklama": r.get("tr", ""), "uyari": r.get("w") or "",
                     "dil": r.get("l"), "yildiz": r.get("s"), "eklenme": r.get("at") or None, "son_guncelleme": r.get("pushed") or None,
                     "arsiv": bool(r.get("archived")),
                     "kaynak": {"ad": r["src"]["t"], "url": r["src"]["u"]} if r.get("src") and r["src"].get("u") else None} for r in repos],
    }


def home_page(cat, pub, tr, comp):
    """Genel bakış: eski sayfadaki gibi kutucuklar; kontrol listelerinde "Listeyi aç" ve denetim düğmesi,
    katalogda repo sayısı ve arşivlenmiş, eskimiş repoları ya da açılmayan linkleri gösteren Dikkat kutucuğu."""
    lists = {l["id"]: l for l in cat["listeler"]}
    repos = pub["repolar"]
    year_ago = (datetime.date.today() - datetime.timedelta(days=365)).isoformat()
    stale = [r for r in repos if r["arsiv"] or (r["son_guncelleme"] and r["son_guncelleme"] < year_ago)]
    synced = cat["repolar"].get("syncedAt")
    tile = lambda **p: "<Kutucuk " + " ".join(f"{k}={js(v)}" for k, v in p.items() if v is not None) + " />"
    grid = lambda tiles: ['<div class="kutucuklar not-content">', *tiles, "</div>", ""]
    lines = [f"import Kutucuk from '{comp}/Kutucuk.astro';", f"import YerelTakip from '{comp}/YerelTakip.astro';", "",
             "Yayına çıkmadan önce nelere bakılmalı, hangi araç, eklenti ve skill işe yarar: kontrol listeleri, rehberler ve doğrulanmış repolar.", "",
             "## Kontrol listeleri", ""]
    lines += grid([tile(ikon=d["ikon"], baslik=d["kisa"], href=route(d), ozet=summary(d["ozet"]),
                        bilgi=f"{count(lists[d['liste']])} madde · {len(lists[d['liste']]['bolumler'])} bölüm", liste=d["liste"])
                   for d in cat["belgeler"] if d["liste"]])
    lines += ["## Rehberler", ""]
    lines += grid([tile(ikon=d["ikon"], baslik=d["kisa"], href=route(d), ozet=summary(d["ozet"])) for d in cat["belgeler"] if not d["liste"]])
    info = f"repo · {len(pub['klasorler'])} kategori" + (f" · {'.'.join(reversed(synced[:10].split('-')))} güncellendi" if synced else "")
    tiles = [tile(ikon="package", baslik="Repo kataloğu", href="/repolar/", sayi=len(repos), bilgi=info,
                  ozet="Türkçe açıklaması, kurulum yeri (proje, Claude, Codex, ayrı uygulama) ve uyarısıyla doğrulanmış GitHub repoları.")]
    warn = [f"{len(stale)} repo arşivlenmiş ya da 1+ yıldır güncellenmiyor" if stale else "", f"{len(tr.broken)} link açılmıyor" if tr.broken else ""]
    if stale or tr.broken:
        tiles.append(tile(ikon="alert", baslik="Dikkat", href="/repolar/#dikkat", sayi=len(stale) + len(tr.broken),
                          bilgi="; ".join(w for w in warn if w), uyari=True))
    lines += ["## Katalog", ""] + grid(tiles)
    lines += ["<YerelTakip />", ""]
    lines += ["## AI'lar için", "",
              "Kataloğun tamamı makinenin okuyacağı biçimde de yayımlanır: [katalog.json](/katalog.json) maddeleri kalıcı kimlikleriyle (ör. `yo-hesap-silme`), rehber öğelerini ve repoları, [llms.txt](/llms.txt) sayfaların ve kategoriye göre dizilmiş repoların özetini, [llms-full.txt](/llms-full.txt) bütün içeriği tek dosyada verir.",
              "Denetim prompt'ları raporu bu kimliklerle ister; madde numaraları değişse de raporlar karşılaştırılabilir kalır."]
    return front(title="Genel bakış", description=DESCRIPTION, tableOfContents=False) + "\n" + "\n".join(lines) + "\n"


def repo_page(pub, comp):
    return (front(title="Repo kataloğu", description=f"{len(pub['repolar'])} doğrulanmış GitHub reposu; Türkçe açıklama, kurulum yeri ve uyarılarıyla.", tableOfContents=False) +
            f"\nimport RepoKatalog from '{comp}/RepoKatalog.astro';\n\n"
            "AI ile proje geliştirirken işe yarayan repolar; her biri README'sinden doğrulandı.\n"
            "Kurulum yeri projeye eklenen kütüphaneyi, Claude ya da Codex'e kurulan skill ve eklentiyi, ayrı çalışan uygulamayı ya da sadece okunan kaynağı gösterir.\n"
            "Kurulum düğmeleri aracı kuracak ajana yapıştırılacak prompt'u kopyalar.\n\n<RepoKatalog />\n")


KURULUM_METNI = {"proje": "projeye eklenir", "claude": "Claude Code'a kurulur", "codex": "Codex'e kurulur",
                 "uygulama": "ayrı uygulama", "kaynak": "kaynak, kurulmaz"}


def repo_groups(pub):
    """Repolar kategori ve alt kategori sırasıyla: [(kategori, [(alt kategori, [repo])])]."""
    return [(k, [(a, [r for r in pub["repolar"] if r["klasor"] == k["id"] and r["alt_klasor"] == a["id"]]) for a in k["alt"]])
            for k in pub["klasorler"]]


def llms(cat, pub):
    """AI'lar için özet: sayfalar ve kategoriye göre dizilmiş repo listesi; ayrıntı llms-full.txt'te."""
    lines = ["# ship-ready", "", f"> {DESCRIPTION}", "",
             "Kontrol listesi maddelerinin kalıcı kimlikleri vardır (ör. yo-hesap-silme, as-paywall-linkleri); denetim raporları bu kimliklerle yazılır.",
             "Bütün içerik tek dosyada: [llms-full.txt](/llms-full.txt). Makinenin okuyacağı katalog: [katalog.json](/katalog.json).",
             "", "## Kontrol listeleri", ""]
    lines += [f"- [{d['baslik']}]({route(d)}): {d['ozet']}" for d in cat["belgeler"] if d["liste"]]
    lines += ["", "## Rehberler", ""]
    lines += [f"- [{d['baslik']}]({route(d)}): {d['ozet']}" for d in cat["belgeler"] if not d["liste"]]
    lines += ["", "## Repo kataloğu", "",
              f"{len(pub['repolar'])} doğrulanmış GitHub reposu amaca göre kategori ve alt kategoriye ayrılır; sayfası [/repolar/](/repolar/), açıklamaları ve kurulum yerleri llms-full.txt'te."]
    for k, altlar in repo_groups(pub):
        lines += ["", f"### {k['ad']}", "", k["aciklama"], ""]
        lines += [f"- {a['ad']}: " + ", ".join(f"[{r['repo']}](https://github.com/{r['repo']})" for r in rs) for a, rs in altlar if rs]
    return "\n".join(lines) + "\n"


def llms_full(cat, pub, tr):
    """Bütün içerik tek Markdown dosyasında: listeler (maddeler kimlikleriyle), rehberler ve açıklamalı repo kataloğu."""
    out = [f"# ship-ready: bütün içerik", "", f"> {DESCRIPTION}", "",
           "Kontrol listelerinde her maddenin sonundaki köşeli parantez maddenin kalıcı kimliğidir; denetim raporu bu kimliklerle yazılır.",
           "Adresler sitenin köküne göredir."]
    for d in cat["belgeler"]:
        body = katalog.ITEM_ID.sub(lambda m: f" [{m.group(1)}]", "\n".join(body_lines(d["metin"])))
        body = katalog.EXAMPLE.sub(lambda m: f" ([canlı örnek](/ornekler/{m.group(1)}.html))", body)
        out += ["", "---", "", f"# {d['baslik']}", "", f"Adres: {route(d)}", "", tr(body).strip()]
    out += ["", "---", "", "# Repo kataloğu", "", "Adres: /repolar/", ""]
    for k, altlar in repo_groups(pub):
        out += [f"## {k['ad']}", "", k["aciklama"], ""]
        for a, rs in altlar:
            if not rs:
                continue
            out += [f"### {a['ad']}", ""]
            for r in rs:
                kur = ", ".join(KURULUM_METNI.get(x, x) for x in r["kurulum"])
                out.append(f"- [{r['repo']}](https://github.com/{r['repo']}): {r['aciklama']} Kurulum: {kur}."
                           + (f" Uyarı: {r['uyari']}" if r["uyari"] else ""))
            out.append("")
    return "\n".join(out).rstrip() + "\n"


def sidebar(cat, pub):
    """Kenar menü (site/src/components/KenarMenu.astro çizer): simge md'nin <!-- ikon: --> satırından, sayaç badge'den."""
    lists = {l["id"]: l for l in cat["listeler"]}

    def item(label, link, icon, badge=None):
        return {"label": label, "link": link, "attrs": {"data-ikon": icon or "file"}, **({"badge": str(badge)} if badge is not None else {})}

    docs = cat["belgeler"]
    return [
        item("Genel bakış", "/", "home"),
        {"label": "Kontrol listeleri", "items": [item(d["kisa"], route(d), d["ikon"], count(lists[d["liste"]])) for d in docs if d["liste"]]},
        {"label": "Rehberler", "items": [item(d["kisa"], route(d), d["ikon"]) for d in docs if not d["liste"]]},
        {"label": "Katalog", "items": [item("Repo kataloğu", "/repolar/", "package", len(pub["repolar"]))]},
    ]


# ---------------- yerel sayfa (sayfa/, çift tıklamayla açılır) ----------------
# Yerel derleme aynı sitedir; raporlar, raporları kaydeden denetim prompt'u ve çevrimdışı arama sadece orada vardır.
# Verisi site/src/yerel/ altına yazılır; herkese açık derleme bu klasörü okumaz (site/.gitignore'da).

STATUS_CLASS = {"✅": "ok", "⚠": "kismen", "❌": "eksik", "➖": "yok"}


def heading_slug(text):
    """Starlight'ın başlık bağlantısı (github-slugger): küçük harf; harf, rakam, boşluk, - ve _ dışındakiler atılır, boşluk - olur."""
    s = katalog.plain(text).lower()
    return "".join(c for c in s if c in " -_" or unicodedata.category(c)[0] in "LNM").replace(" ", "-")


def date_tr(d):
    return ".".join(reversed(d.split("-")))


def counts(statuses):
    return {s: sum(1 for v in statuses.values() if v == s) for s in katalog.STATUS_SYMBOLS}


def decorate_report(text, prev, list_url, by_no):
    """Rapor md'si: ilk başlık atılır (sayfa başlığı olur), kimlik maddeye bağlanır, durum hücresi renklenir,
    önceki rapordan farklı durumun yanına önceki durum yazılır."""
    out, heads = [], None
    for line in re.sub(r"^#\s+.*\n?", "", text, count=1).split("\n"):
        if not line.lstrip().startswith("|"):
            heads = None
            out.append(line)
            continue
        c = katalog.cells(line)
        if heads is None:
            heads = c
            out.append(line)
            continue
        key = "Kimlik" if "Kimlik" in heads else "#" if "#" in heads else None
        if katalog.is_separator(line) or not key or "Durum" not in heads or len(c) <= max(heads.index(key), heads.index("Durum")):
            out.append(line)
            continue
        ki, si = heads.index(key), heads.index("Durum")
        ref = katalog.plain(c[ki])
        item = ref if key == "Kimlik" else by_no.get(int(ref)) if ref.isdigit() else None
        sym = next((s for s in katalog.STATUS_SYMBOLS if katalog.plain(c[si]).startswith(s)), None)
        if item and list_url:
            c[ki] = f"[{ref}]({list_url}#{item})"
        if sym:
            was = prev.get(item)
            note = f' <span class="onceki">önceki: {"⚠️" if was == "⚠" else was}</span>' if was and was != sym else ""
            c[si] = f'<span class="durum d-{STATUS_CLASS[sym]}">{c[si]}</span>{note}'
        out.append("| " + " | ".join(c) + " |")
    return "\n".join(out)


def local_reports(cat):
    lists = {l["id"]: l for l in cat["listeler"]}
    list_doc = {d["liste"]: d for d in cat["belgeler"] if d["liste"]}
    path = lambda r: f"{Path(r['dosya']).parent.name}/{Path(r['dosya']).stem}"
    groups = []
    for g in cat["raporlar"]:
        lst, doc = lists.get(g["liste"]), list_doc.get(g["liste"])
        by_no = {m["no"]: m["id"] for s in lst["bolumler"] for m in s["maddeler"]} if lst else {}
        reports = []
        for i, r in enumerate(g["raporlar"]):
            prev = g["raporlar"][i + 1] if i + 1 < len(g["raporlar"]) else None
            reports.append({
                "yol": path(r), "tarih": r["tarih"], "sayilar": counts(r["durumlar"]),
                "onceki": {"yol": path(prev), "tarih": prev["tarih"], "sayilar": counts(prev["durumlar"])} if prev else None,
                "fark": katalog.compare(r["durumlar"], prev["durumlar"]) if prev else None,
                "metin": decorate_report(r["metin"], prev["durumlar"] if prev else {}, route(doc) if doc else None, by_no)})
        groups.append({"proje": g["proje"], "baslik": g["baslik"], "liste": g["liste"], "liste_adi": doc["kisa"] if doc else g["liste"],
                       "raporlar": reports})
    return groups


def search_index(cat, pub, groups):
    """Yerel sayfanın çevrimdışı arama dizini: sayfalar, maddeler, rehber bölümleri, repolar ve raporlar."""
    out, numbers = [], cat["numaralar"]
    lists = {l["id"]: l for l in cat["listeler"]}

    def add(page, title, url, text=""):
        out.append({"s": page, "b": title, "u": url, "x": text})

    def line_text(line):
        line = katalog.resolve(line, numbers)
        if line.lstrip().startswith("|"):
            return " · ".join(c for c in (katalog.plain(x) for x in katalog.cells(line)) if c)
        return katalog.plain(re.sub(r"^\s*(?:#+|[-*]|\d+\.)\s+", "", line))

    for d in cat["belgeler"]:
        url = route(d)
        add(d["kisa"], d["baslik"], url, d["ozet"])
        if d["liste"]:
            for sec in lists[d["liste"]]["bolumler"]:
                for m in sec["maddeler"]:
                    add(d["kisa"], f"{m['no']}. {m['baslik']}", f"{url}#{m['id']}", m["metin"] if m["metin"] != m["baslik"] else "")
            continue
        # Her ## bölümü bir sonuç; bölümdeki tablo satırları (araç, stil, komut...) ayrı sonuç olur ve bölüme gider.
        head, text, rows, table = None, [], [], False
        for line in body_lines(d["metin"]) + ["## "]:
            h = re.match(r"^##\s+(.*)$", line)
            if h:
                if head:
                    anchor = f"{url}#{heading_slug(head)}"
                    add(d["kisa"], katalog.plain(head), anchor, " ".join(t for t in text if t))
                    for r in rows:
                        add(f"{d['kisa']} · {katalog.plain(head)}", katalog.plain(katalog.resolve(r[0], numbers)), anchor,
                            " · ".join(c for c in (katalog.plain(katalog.resolve(x, numbers)) for x in r[1:]) if c))
                head, text, rows, table = h.group(1).strip(), [], [], False
            elif head is None or not line.strip() or line.strip().startswith("```"):
                table = False
            elif line.lstrip().startswith("|"):
                if table and not katalog.is_separator(line):
                    rows.append(katalog.cells(line))
                table = True
            else:
                text.append(line_text(line))
    for r in pub["repolar"]:
        kat = next((k for k in pub["klasorler"] if k["id"] == r["klasor"]), {"ad": "", "alt": []})
        alt = next((a["ad"] for a in kat["alt"] if a["id"] == r["alt_klasor"]), "")
        add(f"Repo kataloğu · {kat['ad']}" + (f" › {alt}" if alt else ""), r["repo"], f"/repolar/#ara={r['repo']}",
            " ".join(x for x in (r["aciklama"], r["uyari"], kat["ad"], alt) if x))
    for g in groups:
        for r in g["raporlar"]:
            lines = [l for l in r["metin"].split("\n") if l.strip() and not katalog.is_separator(l)]
            add("Proje raporları", f"{g['baslik']} · {g['liste_adi']} · {date_tr(r['tarih'])}", f"/raporlar/{r['yol']}/",
                " ".join(line_text(l) for l in lines))
    return out


def local_data(cat, pub):
    groups = local_reports(cat)
    menu = sidebar(cat, pub) + [{"label": "Takip", "items": [{"label": "Proje raporları", "link": "/raporlar/", "attrs": {"data-ikon": "clipboard"},
                                                               **({"badge": str(len(groups))} if groups else {})}]}]
    if LOCAL.exists():
        shutil.rmtree(LOCAL)
    write(LOCAL / "raporlar.json", json.dumps({"gruplar": groups}, ensure_ascii=False, indent=1))
    write(LOCAL / "sidebar.json", json.dumps(menu, ensure_ascii=False, indent=1))
    write(LOCAL / "arama.json", json.dumps(search_index(cat, pub, groups), ensure_ascii=False))
    return groups


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def main(cat=None):
    sys.stdout.reconfigure(encoding="utf-8")
    cat = cat or katalog.load()
    tr = Translate(cat)
    pub = public_catalog(cat)
    if DOCS.exists():
        shutil.rmtree(DOCS)
    for d in cat["belgeler"]:
        if d["liste"]:
            lst = next(l for l in cat["listeler"] if l["id"] == d["liste"])
            write(DOCS / "listeler" / f"{d['liste']}.mdx", list_page(d, lst, tr, "../../../components"))
        else:
            text, ext = guide_page(d, tr, "../../../components")
            write(DOCS / "rehberler" / f"{Path(d['dosya']).stem}{ext}", text)
    write(DOCS / "repolar.mdx", repo_page(pub, "../../components"))
    write(DOCS / "index.mdx", home_page(cat, pub, tr, "../../components"))
    data = json.dumps(pub, ensure_ascii=False, indent=1)
    write(DATA / "katalog.json", data)
    write(DATA / "sidebar.json", json.dumps(sidebar(cat, pub), ensure_ascii=False, indent=1))
    write(PUBLIC / "katalog.json", data)
    write(PUBLIC / "llms.txt", llms(cat, pub))
    write(PUBLIC / "llms-full.txt", llms_full(cat, pub, tr))
    local_data(cat, pub)
    pages = len(list(DOCS.rglob("*.md*")))
    print(f"site: {pages} sayfa, {sum(count(l) for l in cat['listeler'])} madde, {len(pub['ogeler'])} rehber öğesi, {len(pub['repolar'])} repo")
    return 1 if cat["sorunlar"] else 0


if __name__ == "__main__":
    sys.exit(main())
