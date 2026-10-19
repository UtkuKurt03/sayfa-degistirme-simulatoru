import argparse
from algorithms.fifo import simulate
from display import show
from inputs import parse_pages, read_pages, validate_capacity

def main() -> None:
    parser = argparse.ArgumentParser(description="Sayfa Değiştirme Simülatörü - Sprint 1 FIFO")
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--file", help="Sayfa dizisi içeren UTF-8 metin dosyası")
    source.add_argument("--pages", help="Boşluk veya virgülle ayrılmış sayfa numaraları")
    parser.add_argument("--frames", type=int, required=True, help="Pozitif çerçeve sayısı")
    args = parser.parse_args()
    try:
        validate_capacity(args.frames)
        pages = read_pages(args.file) if args.file else parse_pages(args.pages)
    except (ValueError, OSError, UnicodeError) as exc:
        parser.error(str(exc))
    show(simulate(pages, args.frames), args.frames)

if __name__ == "__main__":
    main()
