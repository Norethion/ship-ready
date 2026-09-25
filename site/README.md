# ship-ready sitesi

Bu klasör ship-ready'nin herkese açık sitesidir; Astro Starlight ile derlenir.
İçerik elle yazılmaz: `python uygulama/guncelle.py` (ya da `python uygulama/site_uret.py`) `src/content/docs/`, `src/data/` ve `public/` altındaki dosyaları `icerik/` ve `veri/` klasörlerinden üretir.
Kurallar üst klasördeki `AGENTS.md`'dedir.

| Komut | Ne yapar |
|---|---|
| `npm run dev` | Geliştirme sunucusunu açar |
| `npm run build` | `dist/` altına statik siteyi ve arama dizinini derler |
| `npm run preview` | Derlenmiş siteyi yerelde gösterir |
