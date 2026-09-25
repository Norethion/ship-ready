---
name: app-store-denetim
description: iOS uygulamasını App Store incelemesine göndermeden önce en sık red sebeplerine (paywall linkleri, fiyat, restore, dış ödeme linki, hesap silme, izin gerekçesi, App Tracking Transparency, gizlilik etiketi, gizlilik politikası linki, eşdeğer giriş seçeneği, demo hesap, destek linki, yaş derecelendirmesi, gizli özellik, ekran görüntüsü, web görünümü, kullanıcı içeriği, sağlık iddiası vb.) göre denetler ve ship-ready'ye rapor yazar. Kullanıcı "App Store denetimi", "App Store'a göndermeden kontrol", "Apple reddeder mi", "app review check" dediğinde kullan.
---

# App Store denetimi

Bu iOS uygulamasını App Store incelemesine göndermeden önce en sık red sebeplerine göre denetle ve sonucu rapor olarak yaz.
Denetim sırasında kodu değiştirme; sadece incele ve raporu kaydet.
Projede iOS uygulaması yoksa bunu söyle ve dur.

## Adımlar

1. Bu skill'in klasöründeki `kontrol-listesi.md` dosyasını oku; bölümler `##` başlıkları, maddeler tablolardaki numaralı satırlardır (kimliği `#` hücresindeki `<!-- id: ... -->` yorumunda), "Kural" sütunu Apple'ın ilgili kuralıdır.
2. Projeyi incele: satın alma ve abonelik ekranları, StoreKit ya da RevenueCat/Superwall kodu, `Info.plist` izin metinleri (`NS...UsageDescription`), App Tracking Transparency kullanımı, eklenen SDK'lar, hesap silme akışı, kullanıcı içeriği özellikleri, uygulama içi web görünümleri.
   Her madde için kanıta dayan; tahmin etme. Koddan anlaşılamayan maddeler (ekran görüntüleri, App Store Connect'teki gizlilik bilgileri, inceleme notları, demo hesap) için ⚠️ ver ve kullanıcının neyi kontrol etmesi gerektiğini yaz.
3. Uygulamaya uymayan maddeler (ör. abonelik yoksa abonelik maddeleri, kullanıcı içeriği yoksa as-kullanici-icerigi maddesi) ➖ olur.
4. Raporu aşağıdaki biçimde yaz ve kaydet. Sonunda inceleme notlarına (App Review Notes) yazılacak metnin ve demo hesap bilgisinin taslağını ekle, kullanıcıya en kritik ❌ maddeleri kısaca özetle.

## Rapor biçimi

```
# <Uygulama adı>

- Proje: <klasör yolu ya da repo>
- Kontrol tarihi: <YYYY-MM-DD>

## <kontrol listesindeki bölüm adı, aynen>

| Kimlik | Madde | Durum | Bulgu |
|---|---|---|---|
| as-paywall-linkleri | <maddenin kısa adı> | ❌ eksik | <kısa açıklama ve dosya:satır> |
```

- `Kimlik` sütununa maddenin kalıcı kimliğini yaz (kontrol listesinde `<!-- id: ... -->` yorumunda); sayfa önceki raporla bu kimlikler üzerinden karşılaştırır. Madde numaraları liste değiştikçe kayar, kimlikler değişmez.
- `Durum` şu simgelerden biriyle başlar: ✅ tamam, ⚠️ kısmen, ❌ eksik, ➖ uygulanmaz.

## Nereye kaydedilir

- `~/.ship-ready.json` dosyasını oku (Windows'ta `%USERPROFILE%\.ship-ready.json`); içindeki `klasor` ship-ready'nin yoludur.
- Raporu `<klasor>/veri/raporlar/<proje-adi>/<YYYY-MM-DD>-app-store.md` olarak kaydet. Proje adı küçük harf, boşluk yerine `-`, Türkçe karakterler sadeleştirilmiş olsun.
- Aynı gün ikinci kez denetliyorsan dosyanın üzerine yaz.
- Sonra `python "<klasor>/uygulama/guncelle.py"` çalıştır; rapor ship-ready'nin "Proje raporları" sekmesinde görünür.
- `~/.ship-ready.json` yoksa raporu projenin kök klasörüne `ship-ready-app-store-<YYYY-MM-DD>.md` olarak kaydet ve kullanıcıya ship-ready'de bir kez `python uygulama/guncelle.py` çalıştırmasını söyle.
