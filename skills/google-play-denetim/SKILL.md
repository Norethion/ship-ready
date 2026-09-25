---
name: google-play-denetim
description: Android uygulamasını Google Play incelemesine göndermeden önce en sık red ve kaldırma sebeplerine (Veri güvenliği formu, gizlilik politikası, hesap silme, hassas izin beyanları, arka planda konum, ön plan servisleri, hedef API seviyesi, 16 KB sayfa boyutu, Play Faturalandırma, abonelik şartları, mağaza bilgileri, içerik derecelendirmesi, çocuklar, kullanıcı içeriği, reklam, giriş bilgileri, kapalı test şartı vb.) göre denetler ve ship-ready'ye rapor yazar. Kullanıcı "Google Play denetimi", "Play Store'a göndermeden kontrol", "Google reddeder mi", "play review check" dediğinde kullan.
---

# Google Play denetimi

Bu Android uygulamasını Google Play incelemesine göndermeden önce en sık red ve kaldırma sebeplerine göre denetle ve sonucu rapor olarak yaz.
Denetim sırasında kodu değiştirme; sadece incele ve raporu kaydet.
Projede Android uygulaması yoksa bunu söyle ve dur.

## Adımlar

1. Bu skill'in klasöründeki `kontrol-listesi.md` dosyasını oku; bölümler `##` başlıkları, maddeler tablolardaki numaralı satırlardır (kimliği `#` hücresindeki `<!-- id: ... -->` yorumunda), "Politika" sütunu Google'ın ilgili politikasıdır.
   Tarihli maddeleri (hedef API seviyesi, 16 KB, paket kaydı) listedeki tarihe göre değil bugünün tarihine göre değerlendir.
2. Projeyi incele: `AndroidManifest.xml` izinleri ve ön plan servisleri, `build.gradle` (`targetSdk`, `minSdk`, AAB, native kütüphaneler), eklenen SDK'lar, Play Faturalandırma kodu, abonelik ekranları, hesap silme akışı, gizlilik politikası linki, kullanıcı içeriği ve reklam kodu.
   Her madde için kanıta dayan; tahmin etme. Koddan anlaşılamayan maddeler (Veri güvenliği formu, izin beyanları, içerik derecelendirmesi, giriş bilgileri, kapalı test) için ⚠️ ver ve kullanıcının Play Console'da neyi kontrol etmesi gerektiğini yaz.
3. Uygulamaya uymayan maddeler (ör. native kod yoksa 16 KB, abonelik yoksa abonelik maddeleri) ➖ olur.
4. Raporu aşağıdaki biçimde yaz ve kaydet. Sonunda Play Console'da doldurulması ya da güncellenmesi gereken formları listele, kullanıcıya en kritik ❌ maddeleri kısaca özetle.

## Rapor biçimi

```
# <Uygulama adı>

- Proje: <klasör yolu ya da repo>
- Kontrol tarihi: <YYYY-MM-DD>

## <kontrol listesindeki bölüm adı, aynen>

| Kimlik | Madde | Durum | Bulgu |
|---|---|---|---|
| gp-veri-guvenligi-formu | <maddenin kısa adı> | ❌ eksik | <kısa açıklama ve dosya:satır> |
```

- `Kimlik` sütununa maddenin kalıcı kimliğini yaz (kontrol listesinde `<!-- id: ... -->` yorumunda); sayfa önceki raporla bu kimlikler üzerinden karşılaştırır. Madde numaraları liste değiştikçe kayar, kimlikler değişmez.
- `Durum` şu simgelerden biriyle başlar: ✅ tamam, ⚠️ kısmen, ❌ eksik, ➖ uygulanmaz.

## Nereye kaydedilir

- `~/.ship-ready.json` dosyasını oku (Windows'ta `%USERPROFILE%\.ship-ready.json`); içindeki `klasor` ship-ready'nin yoludur.
- Raporu `<klasor>/veri/raporlar/<proje-adi>/<YYYY-MM-DD>-google-play.md` olarak kaydet. Proje adı küçük harf, boşluk yerine `-`, Türkçe karakterler sadeleştirilmiş olsun.
- Aynı gün ikinci kez denetliyorsan dosyanın üzerine yaz.
- Sonra `python "<klasor>/uygulama/guncelle.py"` çalıştır; rapor ship-ready'nin "Proje raporları" sekmesinde görünür.
- `~/.ship-ready.json` yoksa raporu projenin kök klasörüne `ship-ready-google-play-<YYYY-MM-DD>.md` olarak kaydet ve kullanıcıya ship-ready'de bir kez `python uygulama/guncelle.py` çalıştırmasını söyle.
