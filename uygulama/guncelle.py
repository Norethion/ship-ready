"""ship-ready'nin sitesini ve yerel sayfasını üretir.

Kaynaklar:
  icerik/*.md                                   kontrol listeleri ve rehberler
  veri/repolar.json                             repo kataloğu: klasörler, Türkçe açıklamalar, kurulum yerleri
  veri/raporlar/<proje>/<tarih>[-<liste>].md    proje denetim raporları (liste: app-store, google-play, paywall)
  veri/linkler.json                             son link kontrolünde açılmayan linkler

İçerik uygulama/katalog.py ile okunur (maddeler, kimlikler, {{no:...}} atıfları, raporlar); bulunan sorunlar yazdırılır
ve çıkış kodu 1 olur. Her çalıştırmada ayrıca:
  - CLAUDE.md, AGENTS.md'nin birebir kopyası yapılır
  - skill'lerin kontrol listeleri icerik/'teki güncel hallerinden atıfları çözülerek kopyalanır
  - skill'lerin raporu nereye yazacağını bilmesi için ~/.ship-ready.json'a bu klasörün yolu yazılır
  - sitenin içeriği uygulama/site_uret.py ile site/ altına üretilir
  - yerel sayfa (sitenin raporlu hâli) sayfa/ klasörüne derlenir; index.html oraya yönlendirir, çift tıklamayla açılır

Kullanım:
  python uygulama/guncelle.py            içerik, rapor ya da repo verisi değiştikten sonra
  python uygulama/guncelle.py --github   ayrıca repoların yıldız sayısını, dilini, İngilizce açıklamasını, arşiv durumunu ve
                                         son güncelleme tarihini GitHub'dan tazeler ve içerikteki linkleri kontrol eder
"""
import datetime, json, os, re, shutil, subprocess, sys, urllib.error, urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.dont_write_bytecode = True  # uygulama/ altında __pycache__ bırakmasın
import katalog
import site_uret

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "icerik"
DATA_DIR = ROOT / "veri"
REPOS = DATA_DIR / "repolar.json"
LINKS = DATA_DIR / "linkler.json"
SITE = ROOT / "site"
PAGE = ROOT / "sayfa"
ENTRY = ROOT / "index.html"
ENTRY_HTML = ('<!doctype html>\n<html lang="tr">\n<head>\n<meta charset="utf-8">\n<title>ship-ready</title>\n'
              '<!-- Yerel sayfa sayfa/ klasöründedir; uygulama/guncelle.py derler. -->\n'
              '<meta http-equiv="refresh" content="0; url=sayfa/index.html">\n</head>\n<body>\n'
              '<p><a href="sayfa/index.html">ship-ready</a></p>\n</body>\n</html>\n')
POINTER = Path.home() / ".ship-ready.json"
SKILL_LISTS = {
    "yayin-oncesi-maddeler.md": ROOT / "skills" / "yayin-oncesi-denetim" / "kontrol-listesi.md",
    "app-store-incelemesi.md": ROOT / "skills" / "app-store-denetim" / "kontrol-listesi.md",
    "google-play-incelemesi.md": ROOT / "skills" / "google-play-denetim" / "kontrol-listesi.md",
}
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0 Safari/537.36"


def now_iso():
    return datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def write_text_if_changed(path, text, label):
    if not path.exists() or path.read_text(encoding="utf-8") != text:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8", newline="\n")
        print(label)


def sync_copies(numbers):
    write_text_if_changed(ROOT / "CLAUDE.md", (ROOT / "AGENTS.md").read_text(encoding="utf-8"), "CLAUDE.md, AGENTS.md ile eşitlendi")
    for src, dest in SKILL_LISTS.items():
        text = katalog.resolve((CONTENT / src).read_text(encoding="utf-8"), numbers)
        write_text_if_changed(dest, text, f"{dest.relative_to(ROOT).as_posix()} güncellendi")


def write_pointer():
    # Skill'ler başka bir projede çalışırken raporu bu klasöre yazabilsin diye.
    try:
        current = read_json(POINTER) if POINTER.exists() else {}
    except (OSError, ValueError):
        current = {}
    if current.get("klasor") != str(ROOT):
        write_json(POINTER, {"klasor": str(ROOT)})
        print(f"{POINTER} yazıldı")


def github_token():
    # Girişsiz GitHub API saatte 60 istek verir, katalog bundan büyük; GITHUB_TOKEN ya da gh CLI oturumu kullanılır.
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token:
        return token
    try:
        return subprocess.run(["gh", "auth", "token"], capture_output=True, text=True, timeout=15).stdout.strip() or None
    except (OSError, subprocess.SubprocessError):
        return None


def fetch_repo(name, token):
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "ship-ready"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    try:
        with urllib.request.urlopen(urllib.request.Request(f"https://api.github.com/repos/{name}", headers=headers), timeout=30) as res:
            return json.load(res)
    except urllib.error.HTTPError as e:
        return e.code
    except Exception as e:
        return type(e).__name__


def refresh_repos():
    data = read_json(REPOS)
    token = github_token()
    with ThreadPoolExecutor(8) as ex:
        results = list(ex.map(lambda x: fetch_repo(x["r"], token), data["repos"]))
    missing, moved, failed = [], [], []
    for x, g in zip(data["repos"], results):
        if g == 404:
            missing.append(x["r"])
        elif not isinstance(g, dict):
            failed.append((x["r"], g))
        else:
            # Adı değişen ya da taşınan repo için GitHub yeni adresine yönlendirir; katalogdaki ad elle düzeltilir.
            if g["full_name"].lower() != x["r"].lower():
                moved.append((x["r"], g["full_name"]))
            x["s"] = g["stargazers_count"]
            x["l"] = g.get("language")
            x["d"] = g.get("description") or ""
            x["archived"] = bool(g.get("archived"))
            x["pushed"] = (g.get("pushed_at") or "")[:10]
    if not failed:
        data["syncedAt"] = now_iso()
    write_json(REPOS, data)
    archived = sum(1 for x in data["repos"] if x.get("archived"))
    print(f"GitHub: {len(data['repos']) - len(missing) - len(failed)} repo tazelendi, {archived} arşivlenmiş, "
          f"{len(missing)} bulunamadı, {len(moved)} taşınmış, {len(failed)} okunamadı")
    for r in missing:
        print("  bulunamadı (silinmiş ya da gizli, katalogdan çıkar):", r)
    for old, new in moved:
        print(f"  taşınmış (r alanını düzelt): {old} -> {new}")
    for r, err in failed:
        print(f"  okunamadı ({err}): {r}")
    if failed and not token:
        print("  GitHub istek sınırı: GITHUB_TOKEN tanımla ya da gh auth login ile giriş yap.")


def check_link(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/html,*/*"})
    try:
        with urllib.request.urlopen(req, timeout=20):
            return None
    except urllib.error.HTTPError as e:
        # Yönlendirmeler (3xx) ve bot korumaları (401/403/429 vb.) sitenin kapalı olduğunu göstermez.
        return None if 300 <= e.code < 400 or e.code in (401, 403, 405, 406, 429, 999) else str(e.code)
    except Exception as e:
        return type(e).__name__


def check_links(texts):
    urls = sorted({u for t in texts for u in re.findall(r"\]\((https?://[^)\s]+)\)", t)})
    with ThreadPoolExecutor(8) as ex:
        results = dict(zip(urls, ex.map(check_link, urls)))
    broken = {u: err for u, err in results.items() if err}
    write_json(LINKS, {"checkedAt": now_iso(), "broken": broken})
    print(f"Linkler: {len(urls)} kontrol edildi, {len(broken)} açılmadı")
    for u, err in broken.items():
        print(f"  açılmadı ({err}): {u}")


def build_page():
    """Yerel sayfayı sitenin kendisinden derler (SHIP_YEREL=1: raporlar, raporu kaydettiren prompt, çevrimdışı arama)."""
    node, astro = shutil.which("node"), SITE / "node_modules" / "astro" / "bin" / "astro.mjs"
    if not node or not astro.exists():
        print("SORUN: yerel sayfa derlenemedi; Node.js kurulu olmalı ve site/ klasöründe npm install çalıştırılmalı")
        return False
    if PAGE.exists():
        shutil.rmtree(PAGE)
    r = subprocess.run([node, str(astro), "build"], cwd=SITE, env={**os.environ, "SHIP_YEREL": "1"},
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode:
        print(r.stdout[-3000:], r.stderr[-3000:], sep="\n")
        print("SORUN: yerel sayfa derlenemedi (hata yukarıda)")
        return False
    print(f"sayfa/ derlendi: {sum(1 for _ in PAGE.rglob('index.html'))} sayfa")
    return True


def main():
    if "--github" in sys.argv:
        refresh_repos()
        check_links([p.read_text(encoding="utf-8") for p in sorted(CONTENT.glob("*.md"))])
    cat = katalog.load()
    sync_copies(cat["numaralar"])
    write_pointer()
    site_uret.main(cat)
    built = build_page()
    write_text_if_changed(ENTRY, ENTRY_HTML, "index.html yerel sayfaya yönlendirildi")
    for problem in cat["sorunlar"]:
        print("SORUN:", problem)
    return 1 if cat["sorunlar"] or not built else 0


if __name__ == "__main__":
    sys.exit(main())
