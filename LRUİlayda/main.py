from __future__ import annotations

import argparse
from typing import Sequence


def simulate_lru(pages: Sequence[int], frame_count: int) -> tuple[list[dict[str, object]], int]:
    """Simulate LRU page replacement and return the state after each page."""
    if frame_count <= 0:
        raise ValueError("Çerçeve sayısı 1 veya daha büyük olmalı.")

    frames: list[int | None] = [None] * frame_count
    last_used: dict[int, int] = {}
    page_faults = 0
    steps: list[dict[str, object]] = []

    for time, page in enumerate(pages):
        if page in frames:
            result = "İsabet"
        else:
            result = "Hata"
            page_faults += 1
            if None in frames:
                frames[frames.index(None)] = page
            else:
                least_recently_used = min(frames, key=lambda item: last_used[item])
                frames[frames.index(least_recently_used)] = page

        last_used[page] = time
        steps.append({
            "step": time + 1,
            "page": page,
            "frames": frames.copy(),
            "result": result,
            "faults": page_faults,
        })

    return steps, page_faults


def main() -> None:
    parser = argparse.ArgumentParser(description="LRU sayfa değiştirme algoritması")
    parser.add_argument(
        "--pages",
        default="6 7 8 9 6 7 2 6 7 8 9 2",
        help='Boşlukla ayrılmış sayfa dizisi (varsayılan: "6 7 8 9 6 7 2 6 7 8 9 2")',
    )
    parser.add_argument("--frames", type=int, default=3, help="Çerçeve sayısı (varsayılan: 3)")
    args = parser.parse_args()

    try:
        pages = [int(value) for value in args.pages.replace(",", " ").split()]
        steps, total_faults = simulate_lru(pages, args.frames)
    except ValueError as error:
        parser.error(str(error))

    print(f"Sayfa dizisi: {' '.join(map(str, pages))}")
    print(f"Çerçeve sayısı: {args.frames}\n")
    print(f"{'Adım':<6}{'Sayfa':<8}{'Çerçeveler':<22}{'Sonuç':<10}{'Toplam hata'}")
    print("-" * 60)
    for step in steps:
        frame_text = "[" + ", ".join("-" if page is None else str(page) for page in step["frames"]) + "]"
        print(
            f"{step['step']:<6}{step['page']:<8}{frame_text:<22}"
            f"{step['result']:<10}{step['faults']}"
        )
    print(f"\nToplam sayfa hatası: {total_faults}")


if __name__ == "__main__":
    main()

