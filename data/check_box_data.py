from dataclasses import dataclass
from typing import List


@dataclass
class CheckBoxData:
    expand_path: List[str]
    target_node: str
    expected_label: str


@dataclass
class CheckBoxResult:
    visible: bool
    checked_items: List[str]


def classified_selection() -> CheckBoxData:
    return CheckBoxData(
        expand_path=["Home", "Documents", "Office"],
        target_node="Classified",
        expected_label="classified",
    )
