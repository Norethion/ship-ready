---
name: yayin-oncesi-denetim
description: Projeyi yayına almadan önce kontrol listesine (güvenlik, kimlik doğrulama, girdi doğrulama, başlıklar, ödeme, operasyon, tedarik zinciri, mobil, SEO, içerik, KVKK, alan adı ve e-posta) göre denetler ve ship-ready'ye rapor yazar. Kullanıcı "yayın öncesi denetim", "yayına hazır mı", "pre-launch audit", "ship-ready denetimi" dediğinde kullan.
---

# Yayın öncesi denetim

Bu projeyi yayın öncesi kontrol listesine göre denetle ve sonucu rapor olarak yaz.
Denetim sırasında kodu değiştirme; sadece incele ve raporu kaydet.

## Adımlar

1. Bu skill'in klasöründeki `kontrol-listesi.md` dosyasını oku; bölümler `##` başlıkları, maddeler numaralı satırlardır; her maddenin kimliği satır sonundaki `<!-- id: ... -->` yorumundadır.
2. Projeyi incele: kaynak kod, yapılandırma, ortam değişkeni örnekleri, bağımlılık dosyaları, sunucu ve barındırma ayarları, şablonlar.
   Her madde için kanıta dayan; tahmin etme. Kanıt bulamıyorsan ⚠️ ver ve neyin kontrol edilemediğini yaz.
3. Proje türüne uymayan maddeler (ör. ödeme yoksa ödeme maddeleri, statik sitede oturum maddeleri) ➖ olur.
4. Raporu aşağıdaki biçimde yaz ve kaydet, sonra kullanıcıya en kritik ❌ maddeleri kısaca özetle ve düzeltmeyi öner.

## Rapor biçimi

```
# <Proje adı>

- Proje: <klasör yolu ya da repo>
- Kontrol tarihi: <YYYY-MM-DD>

## <kontrol listesindeki bölüm adı, aynen>

| Kimlik | Madde | Durum | Bulgu |
|---|---|---|---|
| yo-secret-koddan-cikar | <maddenin kısa adı> | ✅ tamam | <kısa açıklama ve dosya:satır> |
```

- `Kimlik` sütununa maddenin kalıcı kimliğini yaz (kontrol listesinde `<!-- id: ... -->` yorumunda); sayfa önceki raporla bu kimlikler üzerinden karşılaştırır. Madde numaraları liste değiştikçe kayar, kimlikler değişmez.
- `Durum` şu simgelerden biriyle başlar: ✅ tamam, ⚠️ kısmen, ❌ eksik, ➖ uygulanmaz.
- Listedeki her bölümü, sırasıyla ve hepsini yaz.

## Nereye kaydedilir

- `~/.ship-ready.json` dosyasını oku (Windows'ta `%USERPROFILE%\.ship-ready.json`); içindeki `klasor` ship-ready'nin yoludur.
- Raporu `<klasor>/veri/raporlar/<proje-adi>/<YYYY-MM-DD>.md` olarak kaydet. Proje adı küçük harf, boşluk yerine `-`, Türkçe karakterler sadeleştirilmiş olsun (ör. `benim-uygulamam`).
- Aynı gün ikinci kez denetliyorsan dosyanın üzerine yaz.
- Sonra `python "<klasor>/uygulama/guncelle.py"` çalıştır; rapor ship-ready'nin "Proje raporları" sekmesinde görünür.
- `~/.ship-ready.json` yoksa raporu projenin kök klasörüne `ship-ready-raporu-<YYYY-MM-DD>.md` olarak kaydet ve kullanıcıya ship-ready'de bir kez `python uygulama/guncelle.py` çalıştırmasını söyle.
