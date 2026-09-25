"""ship-ready çekirdeği: icerik/*.md, veri/repolar.json ve veri/raporlar/ dosyalarını tek bir kataloğa çevirir.
Site ve yerel sayfa (site_uret.py), MCP sunucusu (mcp_sunucu.py) ve guncelle.py bu kataloğu kullanır.
Python'un kendi kütüphanesinden başka bağımlılığı yoktur.

Kavramlar:
  liste   <!-- liste: kimlik --> satırı olan md; maddeleri numaralı satır ya da ilk sütunu "#" olan tablo satırıdır
  madde   her maddenin değişmeyen kimliği vardır: listede satır sonunda, tabloda "#" hücresinde <!-- id: ... -->
  öğe     rehber md'lerindeki tablo satırları (araç, servis, stil, komut...)
  atıf    md'lerde {{no:kimlik}} yazılır, maddenin o anki numarasına çevrilir

Komut satırı:
  python uygulama/katalog.py dogrula        kimlik, atıf ve rapor sorunlarını listeler (sorun yoksa çıkış kodu 0)
  python uygulama/katalog.py ara <sorgu>    maddelerde, rehber öğelerinde ve repolarda arar
  python uygulama/katalog.py json           kataloğun tamamını JSON olarak yazar
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "icerik"
REPOS = ROOT / "veri" / "repolar.json"
REPORTS = ROOT / "veri" / "raporlar"
STATUS_SYMBOLS = ["✅", "⚠", "❌", "➖"]
ID_PATTERN = r"[a-z0-9]+(?:-[a-z0-9]+)+"
REF = re.compile(r"\{\{no:([^}]*)\}\}")
ITEM_ID = re.compile(r"\s*<!--\s*id:\s*(\S*)\s*-->")
SETUP_TARGETS = ("proje", "uygulama", "kaynak")


def directive(text, key):
    m = re.search(rf"<!--\s*{key}:\s*(.+?)\s*-->", text)
    return m.group(1) if m else None


def plain(s):
    """Md hücresini düz metne çevirir: link, kod ve vurgu işaretleri atılır, HTML etiketleri silinir."""
    s = re.sub(r"<!--.*?-->", "", s)
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)
    s = re.sub(r"<[^>]+>", "", s)
    return re.sub(r"\s+", " ", s.replace("`", "").replace("**", "")).strip()


def cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def is_separator(line):
    return bool(re.match(r"^\|?\s*:?-{3,}", line.strip()))


def lead(text):
    """Başlıktan sonraki ilk paragraf (direktif satırları hariç)."""
    body = re.sub(r"^#\s+.*$", "", text, count=1, flags=re.M)
    for block in re.split(r"\n\s*\n", body):
        lines = [l for l in block.strip().split("\n") if l.strip() and not l.strip().startswith("<!--")]
        if lines and not lines[0].startswith(("#", "|", "```", "-")):
            return plain(" ".join(lines))
    return ""


def parse_doc(path):
    text = path.read_text(encoding="utf-8")
    title = (re.search(r"^#\s+(.+)$", text, re.M) or [None, path.stem])[1].strip()
    return {
        "dosya": path.name, "baslik": title, "kisa": title.split(":")[0].strip(),
        "grup": directive(text, "grup") or "Rehberler", "ikon": directive(text, "ikon") or "file",
        "sira": float(directive(text, "sira") or 99), "liste": directive(text, "liste"),
        "yan_yana": bool(re.search(r"<!--\s*yan-yana\s*-->", text)), "ozet": lead(text), "metin": text,
    }


def sections(text):
    """(bölüm başlığı, satırlar) çiftleri; bölüm başlığındaki "(N)" sayısı atılır."""
    out, title, lines = [], "", []
    for line in text.split("\n"):
        h = re.match(r"^##\s+(.+)$", line)
        if h:
            out.append((title, lines))
            title, lines = re.sub(r"\s*\(\d+\)$", "", h.group(1).strip()), []
        else:
            lines.append(line)
    out.append((title, lines))
    return out


def tables(lines):
    """Bir bölümdeki tabloları (başlıklar, satır hücreleri) olarak verir."""
    heads, rows = None, []
    for line in lines + [""]:
        if line.lstrip().startswith("|"):
            if heads is None:
                heads = cells(line)
            elif not is_separator(line):
                rows.append(cells(line))
            continue
        if heads is not None:
            yield heads, rows
        heads, rows = None, []


def parse_list(doc):
    """Liste md'sinin bölümlerini ve maddelerini çıkarır. Madde: kimlik, numara, başlık, metin ve tablo alanları."""
    out, fmt = [], None
    for title, lines in sections(doc["metin"]):
        items = []
        for line in lines:
            m = re.match(r"^(\d+)\.\s+(.*)$", line)
            if m:
                fmt = fmt or "liste"
                idm = ITEM_ID.search(m.group(2))
                text = plain(ITEM_ID.sub("", m.group(2)))
                items.append({"id": idm.group(1) if idm else None, "no": int(m.group(1)), "baslik": text, "metin": text, "alanlar": {}})
        for heads, rows in tables(lines):
            if heads[0] != "#":
                continue
            fmt = fmt or "tablo"
            for row in rows:
                idm = ITEM_ID.search(row[0])
                num = re.match(r"\d+", plain(row[0]))
                fields = {h: plain(v) for h, v in zip(heads[2:], row[2:])}
                name = plain(row[1]) if len(row) > 1 else ""
                items.append({"id": idm.group(1) if idm else None, "no": int(num.group()) if num else None,
                              "baslik": name, "metin": " ".join([name] + list(fields.values())), "alanlar": fields})
        if items:
            out.append({"baslik": title, "maddeler": items})
    return {"id": doc["liste"], "dosya": doc["dosya"], "baslik": doc["baslik"], "bicim": fmt or "liste", "bolumler": out}


def parse_guide_items(doc):
    """Rehber md'lerindeki tablo satırları: ilk sütun adı, ilk linki url, diğer sütunlar alanlar."""
    out = []
    for title, lines in sections(doc["metin"]):
        for heads, rows in tables(lines):
            for row in rows:
                link = re.search(r"\]\((https?://[^)\s]+)\)", row[0])
                out.append({"ad": plain(row[0]), "url": link.group(1) if link else None, "tur": heads[0],
                            "belge": doc["dosya"], "bolum": title,
                            "alanlar": {h: plain(v) for h, v in zip(heads[1:], row[1:]) if h}})
    return out


def setup_targets(repo):
    k = repo.get("k")
    if k == "ajan":
        return [a for a in repo.get("a") or [] if a in ("claude", "codex")]
    return [k] if k in SETUP_TARGETS else []


def parse_statuses(text, numbers):
    """Rapor tablolarından {madde kimliği: durum simgesi}. "Kimlik" sütunu yoksa "#" sütunu numaralarla eşlenir."""
    out = {}
    for _, lines in sections(text):
        for heads, rows in tables(lines):
            key = "Kimlik" if "Kimlik" in heads else "#" if "#" in heads else None
            if not key or "Durum" not in heads:
                continue
            ki, si = heads.index(key), heads.index("Durum")
            for row in rows:
                if len(row) <= max(ki, si):
                    continue
                ref = plain(row[ki])
                sym = next((s for s in STATUS_SYMBOLS if plain(row[si]).startswith(s)), None)
                item = ref if key == "Kimlik" else numbers.get(int(ref)) if ref.isdigit() else None
                if item and sym:
                    out[item] = sym
    return out


def parse_reports(lists):
    """veri/raporlar/<proje>/<YYYY-MM-DD>[-<liste>].md; tür yoksa yayın öncesi denetimidir."""
    by_list = {l["id"]: {m["no"]: m["id"] for s in l["bolumler"] for m in s["maddeler"]} for l in lists}
    groups = {}
    for p in sorted(REPORTS.glob("*/*.md")) if REPORTS.exists() else []:
        kind = p.stem[11:] or "yayin-oncesi"
        text = p.read_text(encoding="utf-8")
        groups.setdefault((p.parent.name, kind), []).append({
            "dosya": f"veri/raporlar/{p.parent.name}/{p.name}", "tarih": p.stem[:10], "metin": text,
            "durumlar": parse_statuses(text, by_list.get(kind, {}))})
    out = []
    for (project, kind), reports in sorted(groups.items()):
        reports.sort(key=lambda r: r["tarih"], reverse=True)
        title = (re.search(r"^#\s+(.+)$", reports[0]["metin"], re.M) or [None, project])[1]
        out.append({"proje": project, "liste": kind, "baslik": title, "raporlar": reports})
    return out


def compare(newer, older):
    """İki raporun durumlarını karşılaştırır: düzelen, bozulan, değişen ve yeni maddeler."""
    rank = {"❌": 0, "⚠": 1, "✅": 2}
    out = {"duzelen": [], "bozulan": [], "degisen": [], "yeni": []}
    for item, sym in newer.items():
        was = older.get(item)
        if was is None:
            out["yeni"].append(item)
        elif was != sym:
            key = "duzelen" if rank.get(sym, -1) > rank.get(was, -1) >= 0 else "bozulan" if rank.get(was, -1) > rank.get(sym, -1) >= 0 else "degisen"
            out[key].append({"id": item, "once": was, "simdi": sym})
    return out


def resolve(text, numbers):
    """{{no:kimlik}} atıflarını maddenin o anki numarasıyla değiştirir; bilinmeyen kimlik "?" olur."""
    return REF.sub(lambda m: str(numbers.get(m.group(1), "?")), text)


def load():
    docs = sorted((parse_doc(p) for p in CONTENT.glob("*.md")), key=lambda d: (d["sira"], d["dosya"]))
    lists = [parse_list(d) for d in docs if d["liste"]]
    numbers = {m["id"]: m["no"] for l in lists for s in l["bolumler"] for m in s["maddeler"] if m["id"]}
    repos = json.loads(REPOS.read_text(encoding="utf-8")) if REPOS.exists() else {"folders": [], "repos": []}
    for r in repos["repos"]:
        r["kurulum"] = setup_targets(r)
    cat = {
        "belgeler": docs, "listeler": lists, "numaralar": numbers,
        "ogeler": [i for d in docs if not d["liste"] for i in parse_guide_items(d)],
        "repolar": repos, "raporlar": parse_reports(lists),
    }
    cat["sorunlar"] = check(cat)
    return cat


def check(cat):
    problems, seen = [], {}
    for l in cat["listeler"]:
        if not re.fullmatch(r"[a-z0-9-]+", l["id"] or ""):
            problems.append(f"{l['dosya']}: liste kimliği geçersiz: {l['id']!r}")
        prefixes = set()
        expected = 1
        for s in l["bolumler"]:
            for m in s["maddeler"]:
                where = f"{l['dosya']} madde {m['no']}"
                if m["no"] != expected:
                    problems.append(f"{where}: numara sırası bozuk (beklenen {expected})")
                expected = (m["no"] or expected) + 1
                if not m["id"]:
                    problems.append(f"{where}: kimlik yok")
                    continue
                if not re.fullmatch(ID_PATTERN, m["id"]):
                    problems.append(f"{where}: kimlik biçimi geçersiz: {m['id']}")
                prefixes.add(m["id"].split("-")[0])
                if m["id"] in seen:
                    problems.append(f"{where}: kimlik {m['id']} {seen[m['id']]} ile aynı")
                seen[m["id"]] = where
        if len(prefixes) > 1:
            problems.append(f"{l['dosya']}: maddeler farklı önekler kullanıyor: {', '.join(sorted(prefixes))}")
    for d in cat["belgeler"]:
        for ref in REF.findall(d["metin"]):
            if ref not in cat["numaralar"]:
                problems.append(f"{d['dosya']}: bilinmeyen atıf {{{{no:{ref}}}}}")
    known = set(cat["numaralar"])
    for g in cat["raporlar"]:
        for r in g["raporlar"]:
            unknown = sorted(set(r["durumlar"]) - known)
            if unknown:
                problems.append(f"{r['dosya']}: listede olmayan kimlikler: {', '.join(unknown)}")
    return problems


def _fold(s):
    return (s or "").translate(str.maketrans("çğıöşüÇĞİÖŞÜÂÎÛâîû", "cgiosuCGIOSUAIUaiu")).lower()


def search(cat, query, limit=20):
    """Basit anahtar kelime araması; her sonuç tür, kimlik ya da ad, belge ve kısa metin taşır."""
    terms = [t for t in re.findall(r"[a-z0-9]+", _fold(query)) if len(t) > 1]
    if not terms:
        return []
    hits = []

    def score(*parts):
        text = _fold(" ".join(p for p in parts if p))
        return sum(text.count(t) for t in terms) if all(t in text for t in terms) else 0

    for l in cat["listeler"]:
        for s in l["bolumler"]:
            for m in s["maddeler"]:
                n = score(m["id"], m["metin"], s["baslik"])
                if n:
                    hits.append((n + 2, {"tur": "madde", "id": m["id"], "no": m["no"], "liste": l["id"], "bolum": s["baslik"], "metin": m["metin"]}))
    for i in cat["ogeler"]:
        n = score(i["ad"], i["bolum"], *i["alanlar"].values())
        if n:
            hits.append((n + 1, {"tur": "oge", "ad": i["ad"], "url": i["url"], "belge": i["belge"], "bolum": i["bolum"],
                                  "metin": " · ".join(v for v in i["alanlar"].values() if v)[:300]}))
    for r in cat["repolar"]["repos"]:
        n = score(r["r"], r.get("tr"), r.get("d"), r.get("w"), " ".join(r["kurulum"]))
        if n:
            hits.append((n, {"tur": "repo", "ad": r["r"], "url": f"https://github.com/{r['r']}", "klasor": r.get("f"),
                             "kurulum": r["kurulum"], "metin": r.get("tr") or r.get("d") or ""}))
    hits.sort(key=lambda h: -h[0])
    return [h[1] for h in hits[:limit]]


def main(argv):
    sys.stdout.reconfigure(encoding="utf-8")
    cmd = argv[1] if len(argv) > 1 else "dogrula"
    cat = load()
    if cmd == "dogrula":
        n = sum(len(s["maddeler"]) for l in cat["listeler"] for s in l["bolumler"])
        print(f"{len(cat['listeler'])} liste, {n} madde, {len(cat['ogeler'])} rehber öğesi, {len(cat['repolar']['repos'])} repo, "
              f"{sum(len(g['raporlar']) for g in cat['raporlar'])} rapor")
        for p in cat["sorunlar"]:
            print("SORUN:", p)
        return 1 if cat["sorunlar"] else 0
    if cmd == "ara":
        for h in search(cat, " ".join(argv[2:])):
            ref = h.get("id") or h.get("ad")
            print(f"[{h['tur']}] {ref}: {h['metin'][:140]}")
        return 0
    if cmd == "json":
        for d in cat["belgeler"]:
            d.pop("metin")
        print(json.dumps(cat, ensure_ascii=False, indent=1))
        return 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
