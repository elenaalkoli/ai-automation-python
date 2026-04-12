from dataclasses import dataclass


@dataclass(frozen=True)
class ModalResult:
    title: str
    body: str
    is_visible: bool
    was_closed: bool
