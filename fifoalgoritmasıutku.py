sayfalar = [1, 2, 3, 1, 4, 2, 1]
cerceve_sayisi = 3
bellek = []
hata_sayisi = 0

for sayfa in sayfalar:
    if sayfa in bellek:
        print(sayfa, "İsabet", bellek)
        continue

    hata_sayisi += 1
    if len(bellek) == cerceve_sayisi:
        cikan_sayfa = bellek.pop(0)  # İlk yüklenen sayfayı çıkar.
        print("Çıkan sayfa:", cikan_sayfa)
    bellek.append(sayfa)
    print(sayfa, "Sayfa hatası", bellek)

print("Sayfa hatası:", hata_sayisi, "| İsabet:", len(sayfalar) - hata_sayisi)
