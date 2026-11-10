# Sayfa Değiştirme Algoritmaları: LRU

Bu depo, FIFO, LRU ve Optimal algoritmalarını aynı sayfa dizisi ve çerçeve sayısı üzerinde karşılaştırmayı amaçlayan terminal tabanlı bir Python uygulamasıdır. Bu dosya, İlayda'nın geliştirdiği **LRU (Least Recently Used)** bölümüdür.

## Proje kapsamı

- Python 3.10 veya üzeri gerekir.
- Girdiler sayfa referans dizisi ve bellek çerçevesi sayısıdır.
- Her erişimde çerçeveler, `hit`/`miss` sonucu, çıkarılan sayfa ve o ana kadarki toplam miss gösterilir.
- Çalışma sonunda toplam erişim, miss, hit ve hit oranı gösterilir.
- Varsayılan olarak örnek dizi hem 3 hem 6 çerçeveyle art arda çalıştırılır.

## Çalıştırma

Önce terminali açıp Python sürümünü kontrol edin:

```bash
python --version
```

Ana proje klasörüne girin ve terminale şu kodu yazın:

```bash
python "LRUİlayda/main.py"
```

## Örnek çıktı: 3 çerçeve

```text
Sayfa dizisi: 6 7 8 9 6 7 2 6 7 8 9 2
Çerçeve sayısı: 3

Adım  Sayfa   Çerçeveler          Sonuç     Çıkarılan   Toplam miss
--------------------------------------------------------------------------------
1     6       [6, -, -]           miss      -           1
2     7       [6, 7, -]           miss      -           2
3     8       [6, 7, 8]            miss      -           3
4     9       [9, 7, 8]            miss      6           4
5     6       [9, 6, 8]            miss      7           5
6     7       [9, 6, 7]            miss      8           6
7     2       [2, 6, 7]            miss      9           7
8     6       [2, 6, 7]            hit       -           7
9     7       [2, 6, 7]            hit       -           7
10    8       [8, 6, 7]            miss      2           8
11    9       [8, 9, 7]            miss      6           9
12    2       [8, 9, 2]            miss      7           10

Toplam erişim: 12
Toplam sayfa hatası (miss): 10
Toplam isabet (hit): 2
İsabet oranı: %16.67
```

## Örnek çıktı: 6 çerçeve

```text
Sayfa dizisi: 6 7 8 9 6 7 2 6 7 8 9 2
Çerçeve sayısı: 6

Adım  Sayfa   Çerçeveler          Sonuç     Çıkarılan   Toplam miss
--------------------------------------------------------------------------------
1     6       [6, -, -, -, -, -]  miss      -           1
2     7       [6, 7, -, -, -, -]  miss      -           2
3     8       [6, 7, 8, -, -, -]  miss      -           3
4     9       [6, 7, 8, 9, -, -]  miss      -           4
5     6       [6, 7, 8, 9, -, -]  hit       -           4
6     7       [6, 7, 8, 9, -, -]  hit       -           4
7     2       [6, 7, 8, 9, 2, -]  miss      -           5
8     6       [6, 7, 8, 9, 2, -]  hit       -           5
9     7       [6, 7, 8, 9, 2, -]  hit       -           5
10    8       [6, 7, 8, 9, 2, -]  hit       -           5
11    9       [6, 7, 8, 9, 2, -]  hit       -           5
12    2       [6, 7, 8, 9, 2, -]  hit       -           5

Toplam erişim: 12
Toplam sayfa hatası (miss): 5
Toplam isabet (hit): 7
İsabet oranı: %58.33
```

## Test sonuçlarının özeti

| Çerçeve sayısı | Toplam erişim | Sayfa hatası (miss) | İsabet (hit) | İsabet oranı |
|---:|---:|---:|---:|---:|
| 3 | 12 | 10 | 2 | %16,67 |
| 6 | 12 | 5 | 7 | %58,33 |

Çerçeveler soldan sağa fiziksel çerçeve sırasıyla gösterilir. LRU, bellek dolduğunda en uzun süredir kullanılmamış sayfayı çıkarır.

> Not: LRU kodu ve README hazırlanırken ChatGPT'den destek alınmıştır.

