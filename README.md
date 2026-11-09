# Sayfa Değiştirme Simülatörü

BİM361 İşletim Sistemleri dersi dönem projesi.

FIFO, LRU ve Optimal sayfa değiştirme algoritmalarını karşılaştırmayı planlıyoruz.

## Görev Dağılımı

- Sabina: Ortak kod yapısı, proje öneri formu ve birleştirme.
- Utku: FIFO algoritması.
- İlayda: LRU algoritması.
- İlayza: Optimal algoritması.

Python 3.10 veya üzeri kullanılacaktır.
Uygulama cmd üzerinden çalışacaktır.

## Normal FIFO Örneği 
Önce klasör açılıp cmd yazılacak . 
python --version yazarak 3.10 ve üzeri olduğu kontrol edilecek ardından python "fifoalgoritmasıutku.py" yazılacak.
İlk sunumdaki normal olan " 7 0 1 2 0 3 0 4 2 3 0 3 2 " sayfa dizisi 3 ve 6 çerçeveyle çalıştırılır. (Bu örnekteki sayıları ChatGPT ile aldım.)

## BeladyAnomalisi içeren FIFO Örneği
Önce klasör açılıp cmd yazılacak ardından python "fifobeladyutku.py" yazılacak.
python --version yazarak 3.10 ve üzeri olduğu kontrol edilecek.
" 1 2 3 4 1 2 5 1 2 3 4 5 " sayfa dizisinde FIFO, 3 çerçeveyle 9, 4 çerçeveyle 10 sayfa hatası verir. Bu örnekte çerçeve sayısı arttığında sayfa hatası da artar. (Bu örnekteki sayıları ChatGPT ile aldım.)
