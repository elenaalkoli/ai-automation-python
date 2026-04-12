from dataclasses import dataclass


@dataclass(frozen=True)
class DragPosition:
    x: float
    y: float


@dataclass(frozen=True)
class DragResult:
    before: DragPosition
    after: DragPosition

    @property
    def x_changed(self) -> bool:
        return abs(self.before.x - self.after.x) > 2

    @property
    def y_changed(self) -> bool:
        return abs(self.before.y - self.after.y) > 2

    @property
    def moved(self) -> bool:
        return self.x_changed or self.y_changed
