# ship-ready sitesi

Bu klasör ship-ready'nin herkese açık site derlemesidir; Astro Starlight ile üretilir.
İçerik elle yazılmaz: depo kökünden `python uygulama/guncelle.py` (ya da `python uygulama/site_uret.py`) çalıştırıldığında `src/content/docs/`, `src/data/` ve `public/` altındaki dosyalar `icerik/` ve `veri/` klasörlerinden üretilir.
Kurallar üst klasördeki `AGENTS.md`'dedir.

| Komut | Ne yapar |
|---|---|
| `npm run dev` | Geliştirme sunucusunu açar |
| `npm run build` | `dist/` altına statik siteyi ve arama dizinini derler |
| `npm run preview` | Derlenmiş siteyi yerelde gösterir |
