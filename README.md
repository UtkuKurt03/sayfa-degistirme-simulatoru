# Sayfa Değiştirme Algoritmaları Simülatörü

BİM 361 İşletim Sistemleri — ilk ara değerlendirme (21 Ekim 2026).
Konu ve Python tercihi ekibin ve öğretim elemanının onayına sunulacaktır.

## Kurulum ve çalıştırma
Python 3.10 veya üstü gerekir. Harici paket veya derleme gerekmez.
ZIP dosyasını çıkarın. Terminali bu README ve main.py dosyasının bulunduğu klasörde açın.
Windows'ta:
```powershell
py -3 main.py --file data/ornek.txt --frames 3
```
Linux/macOS'ta:
```bash
python3 main.py --file data/ornek.txt --frames 3
```
Doğrudan veri girişi:
```powershell
py -3 main.py --pages "1 2 1 3" --frames 2
```
Windows'ta py bulunamazsa ve Python kuruluysa `python` komutunu deneyin.

## Sprint 1 kapsamı
Çalışır: dosyadan veya komut satırından giriş, giriş kontrolleri, FIFO,
adım adım çerçeve içeriği, hata/isabet sayıları ve hata oranı.
LRU ve Optimal dosyaları yalnızca iskelettir; çalıştıkları iddia edilmez.
Gerçek işletim sistemi belleği değiştirilmez, sayfa erişimleri simüle edilir.
Optimal, gelecekteki erişimleri bildiği varsayılan bir karşılaştırma algoritması olacaktır.

## Beklenen demo
`data/ornek.txt`, 3 çerçeve: 13 erişim, 10 sayfa hatası, 3 isabet, %76.92 hata oranı.
`1 2 1 3`, 2 çerçeve: 3 hata; son bellek [3, 2]. İsabette FIFO sırası değişmez.

## Kod düzeni
- models.py: ortak Step ve Result veri sınıfları
- inputs.py: veri okuma ve doğrulama
- algorithms/fifo.py: çalışan FIFO
- algorithms/lru.py, optimal.py: sonraki aşamanın iskeletleri
- display.py: terminal çıktısı
- main.py: komut satırı ve birleştirme
- tests/: FIFO davranışı ve giriş kontrolleri

## Kontrol
```powershell
py -3 -m unittest discover -s tests -v
```
Linux/macOS'ta `py -3` yerine `python3` kullanın.

## Ortak Git deposu
Gerçek depo bağlantısı: https://github.com/UtkuKurt03/sayfa-degistirme-simulatoru
GitHub/GitLab hesabında boş bir ortak depo açın ve dört üyeyi ekleyin.
Bu klasörde Git kurulu terminalde sırayla:
```bash
git init
git add .
git commit -m "Sprint 1: FIFO demosu ve proje iskeleti"
git branch -M main
git remote add origin GERCEK_DEPO_ADRESI
git push -u origin main
```
GERCEK_DEPO_ADRESI yerine oluşturduğunuz deponun adresini yazın.
Formdaki depo alanını da aynı bağlantıyla tamamlayın. Depo bu paketle otomatik açılmaz.
Ekip üyeleri kendi gerçek katkılarını kendi hesaplarıyla commit etmelidir.

## Görevler ve ilerleme
GOREV_VE_ILERLEME.md dosyasındaki önerilen rolleri isimlerle kesinleştirin.
Hazır kod AI desteğiyle oluşturulmuştur; bireysel yazarlık/katkı kaydı değildir.
Her üye kendi bölümünü inceleyip çalıştırmalı, açıklayabilmeli ve gerçek katkısını kaydetmelidir.
