"""ship-ready MCP sunucusu: kataloğu (uygulama/katalog.py) Claude Code, Codex gibi ajanlara araç olarak açar.
Stdio üzerinden satır satır JSON-RPC 2.0 konuşur; Python'un kendi kütüphanesinden başka bağımlılığı yoktur.
Katalog her çağrıda dosyalardan yeniden okunur; içerik değişince sunucuyu yeniden başlatmak gerekmez.

Ajana eklemek (kullanıcı kendisi yapar):
  claude mcp add --scope user ship-ready -- python "<klasör>\\uygulama\\mcp_sunucu.py"
  codex mcp add ship-ready -- python "<klasör>\\uygulama\\mcp_sunucu.py"
"""
import datetime, json, re, subprocess, sys
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
import katalog

VERSION = "1.0.0"
PROTOCOLS = ["2025-11-25", "2025-06-18", "2025-03-26", "2024-11-05"]
MAX_REPORT = 300_000
STATUS_HELP = "Durum: ✅ tamam, ⚠️ kısmen, ❌ eksik, ➖ bu projeye uygulanmaz. Bulgu: kısa açıklama ve ilgili dosya:satır."
INSTRUCTIONS = (
    "ship-ready, kişisel projeleri AI ile geliştirip yayına çıkarırken başvurulan Türkçe bir kaynaktır: yayın öncesi, App Store, "
    "Google Play ve paywall kontrol listeleri; UI/UX, gelir, yayına alma ve AI geliştirme rehberleri; doğrulanmış GitHub repoları. "
    "Bir projeyi denetlerken kontrol_listesi ile maddeleri al, kodda kanıta dayanarak değerlendir, raporu rapor_kaydet ile kaydet. "
    "Repolar amaca göre kategorilere ve alt kategorilere ayrılır ; repolar aracı klasor ve alt_klasor ile süzer ve kategorilerin listesini de döndürür. "
    "Araç, kütüphane ya da skill ararken arac_oner ve repolar kullan; her maddenin kalıcı bir kimliği vardır (ör. yo-hesap-silme)."
)


# ---------------- araçlar ----------------

def list_ids(cat):
    return [l["id"] for l in cat["listeler"]]


def get_list(cat, lid):
    for l in cat["listeler"]:
        if l["id"] == lid:
            return l
    raise ValueError(f"Bilinmeyen liste: {lid!r}. Listeler: {', '.join(list_ids(cat))}")


def item_index(cat):
    return {m["id"]: (l["id"], s["baslik"], m) for l in cat["listeler"] for s in l["bolumler"] for m in s["maddeler"]}


def slug(text):
    t = katalog._fold(text)
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")[:60]


def t_ara(cat, sorgu, tur=None, limit=15):
    hits = katalog.search(cat, sorgu, limit=200)
    if tur:
        hits = [h for h in hits if h["tur"] == tur]
    return {"sorgu": sorgu, "sonuclar": hits[:limit]}


def t_kontrol_listesi(cat, liste, bolum=None):
    l = get_list(cat, liste)
    secs = [s for s in l["bolumler"] if not bolum or katalog._fold(bolum) in katalog._fold(s["baslik"])]
    if not secs:
        raise ValueError(f"{liste} listesinde {bolum!r} bölümü yok. Bölümler: {', '.join(s['baslik'] for s in l['bolumler'])}")
    kind = "" if liste == "yayin-oncesi" else f"-{liste}"
    return {
        "liste": l["id"], "baslik": l["baslik"], "dosya": f"icerik/{l['dosya']}",
        "bolumler": [{"baslik": s["baslik"], "maddeler": [{"id": m["id"], "no": m["no"], "madde": m["baslik"], **({"alanlar": m["alanlar"]} if m["alanlar"] else {})}
                                                           for m in s["maddeler"]]} for s in secs],
        "denetim": ("Kodu, yapılandırmayı ve bağımlılıkları incele; tahmin etme, gördüğün kanıta dayan. Rapor Markdown olsun: ilk satır '# <Proje adı>', "
                    "sonra '- Proje: <yol ya da repo>' ve '- Kontrol tarihi: YYYY-MM-DD', ardından her bölüm için '## <bölüm adı>' ve "
                    "'| Kimlik | Madde | Durum | Bulgu |' tablosu. Kimlik sütununa maddenin kimliğini yaz. " + STATUS_HELP +
                    f" Raporu rapor_kaydet aracıyla kaydet (dosya adı <tarih>{kind}.md olur)."),
    }


def t_arac_oner(cat, ihtiyac, altyapi=None, kurulum=None, limit=10):
    hits = [h for h in katalog.search(cat, ihtiyac, limit=300) if h["tur"] in ("oge", "repo")]
    if kurulum:
        hits = [h for h in hits if h["tur"] == "repo" and kurulum in h["kurulum"]]
    if altyapi:
        a = katalog._fold(altyapi)
        hits.sort(key=lambda h: a not in katalog._fold(json.dumps(h, ensure_ascii=False)))
    return {"ihtiyac": ihtiyac, "altyapi": altyapi, "kurulum": kurulum, "oneriler": hits[:limit],
            "not": "Öğeler rehber tablolarından, repolar doğrulanmış GitHub kataloğundandır; kurmadan önce README'yi ve uyarıyı oku."}


def t_repolar(cat, klasor=None, alt_klasor=None, kurulum=None, sorgu=None, limit=30):
    data = cat["repolar"]
    names = {f["id"]: f["name"] for f in data.get("folders", [])}
    alts = {f["id"]: {a["id"]: a["name"] for a in f.get("alt", [])} for f in data.get("folders", [])}
    out = []
    for r in data["repos"]:
        if klasor and r.get("f") != klasor:
            continue
        if alt_klasor and r.get("af") != alt_klasor:
            continue
        if kurulum and kurulum not in r["kurulum"]:
            continue
        if sorgu and not katalog.match_all(sorgu, " ".join(str(r.get(k) or "") for k in ("r", "tr", "d", "w", "kategori", "alt_kategori"))):
            continue
        out.append({"repo": r["r"], "url": f"https://github.com/{r['r']}", "aciklama": r.get("tr") or r.get("d") or "",
                    "uyari": r.get("w") or "", "klasor": names.get(r.get("f"), r.get("f")),
                    "alt_klasor": alts.get(r.get("f"), {}).get(r.get("af"), r.get("af")), "kurulum": r["kurulum"],
                    "yildiz": r.get("s"), "arsiv": bool(r.get("archived")), "son_guncelleme": r.get("pushed")})
    out.sort(key=lambda x: -(x["yildiz"] or 0))
    return {"toplam": len(out), "klasorler": {k: {"ad": v, "alt": alts[k]} for k, v in names.items()}, "repolar": out[:limit]}


def t_belge(cat, dosya=None):
    if not dosya:
        return {"belgeler": [{"dosya": d["dosya"], "baslik": d["baslik"], "grup": d["grup"], "liste": d["liste"], "ozet": d["ozet"]}
                             for d in cat["belgeler"]]}
    for d in cat["belgeler"]:
        if d["dosya"] == dosya or d["dosya"] == dosya + ".md":
            return {"dosya": d["dosya"], "baslik": d["baslik"], "metin": katalog.resolve(d["metin"], cat["numaralar"])}
    raise ValueError(f"Belge yok: {dosya!r}. Belgeler: {', '.join(d['dosya'] for d in cat['belgeler'])}")


def t_rapor_kaydet(cat, proje, liste, rapor, tarih=None, uzerine_yaz=False):
    get_list(cat, liste)
    tarih = tarih or datetime.date.today().isoformat()
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", tarih):
        raise ValueError("tarih YYYY-MM-DD olmalı")
    name = slug(proje)
    if not name:
        raise ValueError("proje adı boş")
    if len(rapor) > MAX_REPORT:
        raise ValueError("rapor çok uzun")
    if not re.match(r"^#\s+\S", rapor.lstrip()):
        raise ValueError("rapor '# <Proje adı>' satırıyla başlamalı")
    statuses = katalog.parse_statuses(rapor, {})
    if not statuses:
        raise ValueError("raporda '| Kimlik | Madde | Durum | Bulgu |' tablosu ya da tanınan durum yok")
    items = item_index(cat)
    wrong = sorted(i for i in statuses if i not in items or items[i][0] != liste)
    if wrong:
        raise ValueError(f"{liste} listesinde olmayan kimlikler: {', '.join(wrong)}")
    path = katalog.REPORTS / name / (tarih + ("" if liste == "yayin-oncesi" else f"-{liste}") + ".md")
    if path.exists() and not uzerine_yaz:
        raise ValueError(f"{path.relative_to(katalog.ROOT).as_posix()} zaten var; aynı gün yeniden kaydetmek için uzerine_yaz: true ver")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(rapor.strip() + "\n", encoding="utf-8", newline="\n")
    # Sayfanın verisini tazele; çıktısı stdout'a (JSON-RPC kanalına) karışmasın diye yakalanır.
    run = subprocess.run([sys.executable, str(Path(__file__).resolve().parent / "guncelle.py")], capture_output=True, text=True,
                         encoding="utf-8", errors="replace", env={**__import__("os").environ, "PYTHONIOENCODING": "utf-8"})
    result = t_rapor_karsilastir(katalog.load(), proje, liste)
    result["kaydedilen"] = path.relative_to(katalog.ROOT).as_posix()
    result["sayfa_guncellendi"] = run.returncode == 0
    return result


def t_rapor_karsilastir(cat, proje, liste="yayin-oncesi"):
    name = slug(proje)
    group = next((g for g in cat["raporlar"] if g["proje"] == name and g["liste"] == liste), None)
    if not group:
        raise ValueError(f"{name!r} projesinin {liste} raporu yok")
    items = item_index(cat)
    newest = group["raporlar"][0]
    counts = {s: sum(1 for v in newest["durumlar"].values() if v == s) for s in katalog.STATUS_SYMBOLS}
    label = lambda i: items[i][2]["baslik"] if i in items else "?"
    out = {"proje": name, "liste": liste, "son": {"tarih": newest["tarih"], "dosya": newest["dosya"], "sayilar": counts},
           "eksikler": [{"id": i, "madde": label(i), "durum": s} for i, s in newest["durumlar"].items() if s in ("❌", "⚠")]}
    if len(group["raporlar"]) > 1:
        older = group["raporlar"][1]
        diff = katalog.compare(newest["durumlar"], older["durumlar"])
        for key in ("duzelen", "bozulan", "degisen"):
            for x in diff[key]:
                x["madde"] = label(x["id"])
        out["onceki"] = {"tarih": older["tarih"], "dosya": older["dosya"]}
        out["fark"] = diff
    return out


def tools(cat):
    lists = list_ids(cat)
    kur = ["proje", "claude", "codex", "uygulama", "kaynak"]
    s = lambda **p: {"type": "object", "properties": p}
    return [
        {"name": "ara", "title": "Katalogda ara",
         "description": "ship-ready'nin kontrol listesi maddelerinde, rehber tablolarında (araç, servis, stil, komut) ve doğrulanmış GitHub repolarında anahtar kelimeyle arar. Bütün kelimeleri içeren sonuçları döndürür.",
         "inputSchema": {**s(sorgu={"type": "string", "description": "Aranacak kelimeler (Türkçe ya da İngilizce)"},
                             tur={"type": "string", "enum": ["madde", "oge", "repo"], "description": "Sadece bu türde ara"},
                             limit={"type": "integer", "minimum": 1, "maximum": 50, "default": 15}), "required": ["sorgu"]}},
        {"name": "kontrol_listesi", "title": "Kontrol listesini al",
         "description": "Bir kontrol listesinin bölümlerini ve maddelerini kalıcı kimlikleriyle, denetim ve rapor biçimi talimatıyla döndürür. Bir projeyi yayın öncesi, App Store, Google Play ya da paywall açısından denetlemek için kullan.",
         "inputSchema": {**s(liste={"type": "string", "enum": lists}, bolum={"type": "string", "description": "Sadece adı bunu içeren bölüm"}), "required": ["liste"]}},
        {"name": "arac_oner", "title": "Araç öner",
         "description": "Bir ihtiyaç için rehberlerdeki araçları ve doğrulanmış GitHub repolarını önerir. altyapi verilirse (ör. react, flutter) ona uyanlar öne alınır; kurulum ile sadece o yere kurulan repolar döner.",
         "inputSchema": {**s(ihtiyac={"type": "string", "description": "Ne aranıyor (ör. grafik, oturum kaydı, skill güvenliği)"},
                             altyapi={"type": "string"}, kurulum={"type": "string", "enum": kur},
                             limit={"type": "integer", "minimum": 1, "maximum": 30, "default": 10}), "required": ["ihtiyac"]}},
        {"name": "repolar", "title": "Repo kataloğunu listele",
         "description": "Repo kataloğundaki doğrulanmış GitHub repolarını klasöre, kurulum yerine (proje, claude, codex, uygulama, kaynak) ve sorguya göre süzerek Türkçe açıklama ve uyarılarıyla döndürür.",
         "inputSchema": s(klasor={"type": "string", "enum": [f["id"] for f in cat["repolar"]["folders"]],
                                  "description": "Kategori: " + "; ".join(f"{f['id']} = {f['name']}" for f in cat["repolar"]["folders"])},
                          alt_klasor={"type": "string", "description": "Alt kategori kimliği; klasor ile birlikte verilir. Kimlikler: " +
                                      "; ".join(f"{f['id']}: " + ", ".join(f"{a['id']} ({a['name']})" for a in f["alt"]) for f in cat["repolar"]["folders"])},
                          kurulum={"type": "string", "enum": kur}, sorgu={"type": "string"},
                          limit={"type": "integer", "minimum": 1, "maximum": 150, "default": 30})},
        {"name": "belge", "title": "Belge oku",
         "description": "dosya verilmezse ship-ready'deki belgeleri özetleriyle listeler; verilirse belgenin Markdown metnini (atıflar çözülmüş) döndürür.",
         "inputSchema": s(dosya={"type": "string", "enum": [d["dosya"] for d in cat["belgeler"]]})},
        {"name": "rapor_kaydet", "title": "Denetim raporunu kaydet",
         "description": "Bir projenin denetim raporunu ship-ready'ye kaydeder, sayfayı günceller ve önceki raporla karşılaştırmayı döndürür. Rapor '| Kimlik | Madde | Durum | Bulgu |' tablolu Markdown olmalı ve sadece o listenin kimliklerini içermeli.",
         "inputSchema": {**s(proje={"type": "string", "description": "Proje adı; klasör adı buradan üretilir"},
                             liste={"type": "string", "enum": lists}, rapor={"type": "string", "description": "Raporun Markdown metni"},
                             tarih={"type": "string", "description": "YYYY-MM-DD, verilmezse bugün"},
                             uzerine_yaz={"type": "boolean", "default": False}), "required": ["proje", "liste", "rapor"]}},
        {"name": "rapor_karsilastir", "title": "Raporları karşılaştır",
         "description": "Bir projenin son denetim raporunu özetler (eksik ve kısmi maddeler) ve varsa bir önceki raporla karşılaştırır: düzelen, bozulan, değişen maddeler.",
         "inputSchema": {**s(proje={"type": "string"}, liste={"type": "string", "enum": lists, "default": "yayin-oncesi"}), "required": ["proje"]}},
    ]


HANDLERS = {"ara": t_ara, "kontrol_listesi": t_kontrol_listesi, "arac_oner": t_arac_oner, "repolar": t_repolar,
            "belge": t_belge, "rapor_kaydet": t_rapor_kaydet, "rapor_karsilastir": t_rapor_karsilastir}


# ---------------- JSON-RPC ----------------

def handle(msg):
    method, mid = msg.get("method"), msg.get("id")
    if mid is None:  # bildirim (ör. notifications/initialized): cevap verilmez
        return None
    try:
        if method == "initialize":
            asked = (msg.get("params") or {}).get("protocolVersion")
            return {"jsonrpc": "2.0", "id": mid, "result": {
                "protocolVersion": asked if asked in PROTOCOLS else PROTOCOLS[0],
                "capabilities": {"tools": {"listChanged": False}},
                "serverInfo": {"name": "ship-ready", "title": "ship-ready", "version": VERSION},
                "instructions": INSTRUCTIONS}}
        if method == "ping":
            return {"jsonrpc": "2.0", "id": mid, "result": {}}
        if method == "tools/list":
            return {"jsonrpc": "2.0", "id": mid, "result": {"tools": tools(katalog.load())}}
        if method == "tools/call":
            params = msg.get("params") or {}
            name, args = params.get("name"), params.get("arguments") or {}
            if name not in HANDLERS:
                return {"jsonrpc": "2.0", "id": mid, "error": {"code": -32602, "message": f"Bilinmeyen araç: {name}"}}
            try:
                data = HANDLERS[name](katalog.load(), **args)
                text, is_error = json.dumps(data, ensure_ascii=False, indent=1), False
            except (ValueError, TypeError) as e:
                text, is_error = f"Hata: {e}", True
            return {"jsonrpc": "2.0", "id": mid, "result": {"content": [{"type": "text", "text": text}], "isError": is_error}}
        return {"jsonrpc": "2.0", "id": mid, "error": {"code": -32601, "message": f"Desteklenmeyen yöntem: {method}"}}
    except Exception as e:  # beklenmeyen hata: sunucu düşmesin, istemciye bildir
        return {"jsonrpc": "2.0", "id": mid, "error": {"code": -32603, "message": f"{type(e).__name__}: {e}"}}


def main():
    out = sys.stdout.buffer
    for raw in sys.stdin.buffer:
        line = raw.decode("utf-8", errors="replace").strip()
        if not line:
            continue
        try:
            msg = json.loads(line)
        except json.JSONDecodeError:
            reply = {"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": "Geçersiz JSON"}}
        else:
            reply = [r for r in map(handle, msg) if r] if isinstance(msg, list) else handle(msg)
        if reply:
            out.write((json.dumps(reply, ensure_ascii=False) + "\n").encode("utf-8"))
            out.flush()


if __name__ == "__main__":
    main()
