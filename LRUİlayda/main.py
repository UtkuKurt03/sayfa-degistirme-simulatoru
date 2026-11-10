from __future__ import annotations

import argparse
from typing import Sequence


def simulate_lru(pages: Sequence[int], frame_count: int) -> tuple[list[dict[str, object]], int]:
    """LRU simülasyonunu çalıştırır; adımları ve toplam sayfa hatasını döndürür."""
    if frame_count <= 0:
        raise ValueError("Çerçeve sayısı 1 veya daha büyük olmalı.")
    if not pages:
        raise ValueError("Sayfa dizisi boş olamaz.")

    frames: list[int | None] = [None] * frame_count
    last_used: dict[int, int] = {}
    page_faults = 0
    steps: list[dict[str, object]] = []

    for time, page in enumerate(pages):
        evicted: int | None = None

        if page in frames:
            result = "hit"
        else:
            result = "miss"
            page_faults += 1

            if None in frames:
                frames[frames.index(None)] = page
            else:
                evicted = min(frames, key=lambda item: last_used[item])
                frames[frames.index(evicted)] = page

        last_used[page] = time
        steps.append({
            "step": time + 1,
            "page": page,
            "frames": frames.copy(),
            "result": result,
            "evicted": evicted,
            "faults": page_faults,
        })

    return steps, page_faults


def print_report(pages: Sequence[int], frame_count: int) -> None:
    steps, total_faults = simulate_lru(pages, frame_count)
    total_accesses = len(pages)
    total_hits = total_accesses - total_faults
    hit_rate = total_hits / total_accesses * 100

    print(f"Sayfa dizisi: {' '.join(map(str, pages))}")
    print(f"Çerçeve sayısı: {frame_count}\n")
    print(
        f"{'Adım':<6}{'Sayfa':<8}{'Çerçeveler':<22}"
        f"{'Sonuç':<10}{'Çıkarılan':<12}{'Toplam miss'}"
    )
    print("-" * 80)

    for step in steps:
        frame_text = "[" + ", ".join(
            "-" if page is None else str(page) for page in step["frames"]
        ) + "]"
        evicted_text = "-" if step["evicted"] is None else str(step["evicted"])
        print(
            f"{step['step']:<6}{step['page']:<8}{frame_text:<22}"
            f"{step['result']:<10}{evicted_text:<12}{step['faults']}"
        )

    print(f"\nToplam erişim: {total_accesses}")
    print(f"Toplam sayfa hatası (miss): {total_faults}")
    print(f"Toplam isabet (hit): {total_hits}")
    print(f"İsabet oranı: %{hit_rate:.2f}")


def main() -> None:
    parser = argparse.ArgumentParser(description="LRU sayfa değiştirme algoritması")
    parser.add_argument(
        "--pages",
        default="6 7 8 9 6 7 2 6 7 8 9 2",
        help='Virgül veya boşlukla ayrılmış sayfa dizisi (varsayılan: "6 7 8 9 6 7 2 6 7 8 9 2")',
    )
    parser.add_argument(
        "--frames",
        type=int,
        nargs="+",
        default=[3, 6],
        help="Bir veya daha fazla çerçeve sayısı (varsayılan: 3 6)",
    )
    args = parser.parse_args()

    try:
        pages = [int(value) for value in args.pages.replace(",", " ").split()]
        if not pages:
            raise ValueError("Sayfa dizisi boş olamaz.")
        for frame_count in args.frames:
            if frame_count <= 0:
                raise ValueError("Çerçeve sayısı 1 veya daha büyük olmalı.")
    except ValueError as error:
        parser.error(str(error))

    for index, frame_count in enumerate(args.frames):
        if index:
            print("\n" + "=" * 80 + "\n")
        print_report(pages, frame_count)


if __name__ == "__main__":
    main()
