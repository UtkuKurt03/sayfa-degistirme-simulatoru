# Sayfa Değiştirme Simülatörü

BİM361 İşletim Sistemleri dersi dönem projesi.

FIFO, LRU ve Optimal sayfa değiştirme algoritmalarını karşılaştırmayı planlıyoruz.

## Görev Dağılımı

- Sabina: Ortak kod yapısı, proje öneri formu ve birleştirme.
- Utku: FIFO algoritması.
- İlayda: LRU algoritması.
- İlayza: Optimal algoritması.

Uygulama , Python 3.10 veya üzeri kullanılacaktır.
Uygulama terminal üzerinden çalışacaktır.

## Normal FIFO Örneği 
Önce proje klasörü açılıp sağ tıklayıp terminal açılacak . 
python --version yazarak 3.10 ve üzeri olduğu kontrol edilecek ardından python "FIFOUtku/fifoalgoritmasıutku.py" yazılacak.
Bu demoda kullanılan "6, 7, 8, 9, 6, 7, 2, 6, 7, 8, 9, 2" sayfa dizisi 3 ve 6 çerçeveyle çalıştırılır. (Bu örnekteki sayıları ChatGPT ile aldım.)

## BeladyAnomalisi içeren FIFO Örneği
Önce proje klasörü açılıp sağ tıklayıp terminal açılacak . 
python --version yazarak 3.10 ve üzeri olduğu kontrol edilecek ardından python "FIFOUtku/fifobeladyutku.py" yazılacak.
"6, 7, 8, 9, 6, 7, 2, 6, 7, 8, 9, 2" sayfa dizisinde FIFO, 3 çerçeveyle 9, 4 çerçeveyle 10 sayfa hatası verir. Bu örnekte çerçeve sayısı arttığında sayfa hatası da artar. (Bu örnekteki sayıları ChatGPT ile aldım.)

## LRU Örneği
Önce proje klasörü açılıp sağ tıklayıp terminal açılacak .
python --version yazarak 3.10 ve üzeri olduğu kontrol edilecek ardından python "LRUİlayda/main.py" yazılacak.
Aynı diziyle 3 çerçevede 10 sayfa hatası oluşur. FIFO ve LRU örnekleri şu anda ayrı ayrı çalışır.

## Güncel Durum 
FIFO örneği , FIFO’da Belady anomalisini gösteren örnek ve LRU algoritmaları şu anda bağımsız olarak çalışmaktadır.
FIFO örneğinde 3 çerçevede 9 sayfa hatası , 6 çerçeve de 5 sayfa hatası bulunuyor.
Belady örneğinde ise 3 çerçevede 9 sayfa hatası , 4 çerçeve de 10 sayfa hatası bulunuyor.
LRU örneğinde ise 3 çerçevede 10 sayfa hatası , 6 çerçeve de 5 sayfa hatası bulunuyor.
