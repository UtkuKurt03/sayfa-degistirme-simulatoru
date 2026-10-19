# İlk görüşme rehberi

21 Ekim 2026 Çarşamba, 11.00–12.30: grup olarak hazır bulunma.
Bu paket yalnızca sayfa değiştirme projesi önerisi içindir; konu onayı henüz alınmadı.

## Önce tamamlanacak alanlar
Proje_Oneri_Formu.docx içindeki öğrenci numaraları, diğer üç üyenin adı, e-posta,
bölüm/sınıf ve grup bilgilerini doldurun. Görev atamalarını ekipçe kabul edin.
Gerçek ortak depo bağlantısını form ve README'ye yazın. Teslim yönteminin çıktı mı
dijital mi olduğu mesajda belirtilmedi; düzenlenebilir formu ve çalışan projeyi yanınızda bulundurun.
Öğretim elemanı onay alanlarını doldurmayın.

## Dört zorunlu maddeyi gösterme
1. Kod deposu: gerçek ortak depo bağlantısını ve README'yi açın.
2. Veri yapıları/iskelelet: models.py, inputs.py ve algorithms klasörünü gösterin.
3. Mini demo: README'deki örnek komutu çalıştırın. 13 erişimde 10 hata, 3 isabet beklenir.
4. Görev paylaşımı: doldurduğunuz gerçek kişi bazında ilerleme kaydını gösterin.

## Yaklaşık iki dakikalık anlatım sırası
- Amaç: FIFO, LRU ve Optimal algoritmalarını aynı girdide karşılaştırmak.
- Şu an çalışan: giriş, doğrulama, FIFO ve terminal çıktısı.
- Örneği çalıştırın. Bellek dolduğunda FIFO'nun önce yüklenen sayfayı çıkardığını açıklayın.
- LRU ve Optimal'in bu aşamada yalnızca iskelet olduğunu belirtin.
- Her üye kendi gerçek katkısını ve sonraki teslimini anlatsın.

## Bilmeniz gerekenler
Sayfa: erişilen veri parçasının simülasyondaki numarası.
Çerçeve: bellekte bir sayfanın tutulabildiği yer.
Sayfa hatası: istenen sayfanın bellekte bulunmaması; boş çerçeve varsa yüklenir,
yoksa bir sayfa değiştirilir. İlk yüklemeler de sayfa hatası sayılır.
FIFO: en önce yüklenen çıkar; isabet sıralamayı değiştirmez.
LRU: en uzun süredir erişilmeyen çıkar.
Optimal: gelecekte en geç kullanılacak veya hiç kullanılmayacak sayfa çıkar.

AI desteğini dersin kurallarına uygun şekilde belirtin. Kodun neden çalıştığını
anlamadan bireysel katkı olarak sunmayın; katkı kaydında yaptığınız gerçek işleri yazın.
