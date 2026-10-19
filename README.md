# Sayfa Değiştirme Algoritmaları Simülatörü

BİM361 İşletim Sistemleri dersi dönem projesi.

## Amaç
FIFO, LRU ve Optimal sayfa değiştirme algoritmalarını aynı girdiler üzerinde karşılaştırmak.

## Mevcut Durum
- FIFO algoritması çalışmaktadır.
- Veri girişi, giriş kontrolleri ve adım adım bellek gösterimi hazırdır.
- LRU ve Optimal algoritmaları için kod iskeletleri oluşturulmuştur.

## Gereksinimler
Python 3.10 veya üstü. Ek kütüphane kurulumu gerekmez.

## Çalıştırma
Proje klasöründe terminal açıp şu komutu çalıştırın:

```bash
python main.py --file data/ornek.txt --frames 3
```

Sisteminizde Python komutu `python3` ise `python` yerine `python3` kullanın.

## Örnek Sonuç
Verilen örnek dosya ve 3 çerçeve için:
- Toplam erişim: 13
- Sayfa hatası: 10
- İsabet: 3

## Görev Dağılımı
- Sabina: Ortak kod yapısı, proje öneri formu ve birleştirme.
- Utku: FIFO algoritması ve doğrulama.
- İlayda: LRU algoritması ve doğrulama.
- İlayza: Optimal algoritması ve doğrulama.
