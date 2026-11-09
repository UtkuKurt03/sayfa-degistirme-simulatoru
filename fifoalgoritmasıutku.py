sayfalar = [7 , 0 , 1 , 2 , 0 , 3 , 0 , 4 , 2 , 3 , 0 , 3 , 2]

for cerceve_sayisi in [3 , 6]:
  bellek = []
  hata_sayisi = 0
  print (cerceve_sayisi , "çerçeve")

  for sayfa in sayfalar: 
     cikan_sayfa = "yok"
     if sayfa in bellek :
        sonuc = "İsabet"
     else:
        sonuc = "Sayfa hatasi"
        hata_sayisi +=1
        if len (bellek) == cerceve_sayisi:
          cikan_sayfa = bellek.pop(0)
        bellek.append(sayfa)

     print ("Sayfa : " , sayfa " -- " sonuc , "-- Bellek:" , bellek "--Çıkan : " , cikan_sayfa)

   print("Sayfa hatasi : " hata_sayisi " -- İsabet : ")
   print()