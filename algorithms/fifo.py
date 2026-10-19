from inputs import validate_capacity
from models import Result, Step

def simulate(pages: list[int], capacity: int) -> Result:
    """Dolu bellekte en önce yüklenen sayfayı değiştirir; isabette sıra değişmez."""
    validate_capacity(capacity)
    frames: list[int] = []
    next_victim = 0
    steps: list[Step] = []
    for page in pages:
        fault = page not in frames
        if fault:
            if len(frames) < capacity:
                frames.append(page)
            else:
                frames[next_victim] = page
                next_victim = (next_victim + 1) % capacity
        steps.append(Step(page, tuple(frames), fault))
    return Result("FIFO", tuple(steps))
