from dataclasses import dataclass


@dataclass(frozen=True)
class SortableResult:
    original_order: list[str]
    final_order: list[str]
