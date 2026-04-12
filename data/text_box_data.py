from dataclasses import dataclass

from faker import Faker

_fake = Faker()


@dataclass
class TextBoxData:
    full_name: str
    email: str
    current_address: str
    permanent_address: str


def generate_text_box_data() -> TextBoxData:
    return TextBoxData(
        full_name=_fake.name(),
        email=_fake.email(),
        current_address=f"{_fake.city()}, {_fake.state()}",
        permanent_address=f"{_fake.street_address()}, {_fake.city()}, {_fake.country()}",
    )
