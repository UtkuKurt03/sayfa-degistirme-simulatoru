from models import Result

def show(result: Result, capacity: int) -> None:
    print(f"Algoritma: {result.algorithm} | Çerçeve: {capacity}")
    print("Adım | Sayfa | Bellek çerçeveleri | Sonuç")
    for index, step in enumerate(result.steps, 1):
        cells = [str(page) for page in step.frames] + ["-"] * (capacity-len(step.frames))
        status = "HATA" if step.fault else "İSABET"
        print(f"{index:>4} | {step.page:>5} | {' '.join(cells):<18} | {status}")
    total = len(result.steps)
    print(f"Toplam erişim: {total}")
    print(f"Sayfa hatası: {result.faults}")
    print(f"İsabet: {total-result.faults}")
    print(f"Sayfa hatası oranı: %{100*result.faults/total:.2f}" if total else "Sayfa hatası oranı: %0.00")
