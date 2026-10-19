from dataclasses import dataclass

@dataclass(frozen=True)
class Step:
    page: int
    frames: tuple[int, ...]
    fault: bool

@dataclass(frozen=True)
class Result:
    algorithm: str
    steps: tuple[Step, ...]

    @property
    def faults(self) -> int:
        return sum(step.fault for step in self.steps)
