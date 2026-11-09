sayfalar = [1, 2, 3, 1, 4, 2, 1]
cerceve_sayisi = 3
bellek = []
hata_sayisi = 0

for sayfa in sayfalar:
    cikan_sayfa = "-"
    if sayfa in bellek:
        sonuc = "İsabet"
    else:
        sonuc = "Sayfa hatası"
        hata_sayisi += 1
        if len(bellek) == cerceve_sayisi:
            cikan_sayfa = bellek.pop(0)  # İlk yüklenen sayfayı çıkar.
        bellek.append(sayfa)

    print("Sayfa:", sayfa, "|", sonuc, "| Bellek:", bellek, "| Çıkan:", cikan_sayfa)

print()
print("Sayfa hatası:", hata_sayisi, "| İsabet:", len(sayfalar) - hata_sayisi)
