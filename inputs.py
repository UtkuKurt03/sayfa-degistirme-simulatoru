from pathlib import Path

def parse_pages(text: str) -> list[int]:
    try:
        pages = [int(value) for value in text.replace(",", " ").split()]
    except ValueError as exc:
        raise ValueError("Sayfa dizisi yalnızca tam sayılar içermelidir.") from exc
    if not pages or any(page < 0 for page in pages):
        raise ValueError("En az bir sayfa girin; sayfa numaraları negatif olamaz.")
    return pages

def read_pages(path: str) -> list[int]:
    return parse_pages(Path(path).read_text(encoding="utf-8"))

def validate_capacity(capacity: int) -> None:
    if capacity < 1:
        raise ValueError("Çerçeve sayısı en az 1 olmalıdır.")
