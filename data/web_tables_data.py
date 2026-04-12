from dataclasses import dataclass

from faker import Faker

_fake = Faker()


@dataclass(frozen=True)
class WebTableRecord:
    first_name: str
    last_name: str
    email: str
    age: str
    salary: str
    department: str


@dataclass(frozen=True)
class WebTableCrudResult:
    created_row: list[str]
    updated_row: list[str]
    deleted: bool


def generate_web_table_record() -> WebTableRecord:
    return WebTableRecord(
        first_name=_fake.first_name(),
        last_name=_fake.last_name(),
        email=_fake.email(),
        age=str(_fake.random_int(min=21, max=60)),
        salary=str(_fake.random_int(min=30000, max=150000)),
        department=_fake.job().split()[0],
    )


def build_updated_web_table_record(source: WebTableRecord) -> WebTableRecord:
    return WebTableRecord(
        first_name=f"Updated{source.first_name}",
        last_name=f"Updated{source.last_name}",
        email=f"updated.{source.email}",
        age=str(min(int(source.age) + 1, 99)),
        salary=str(int(source.salary) + 5000),
        department=f"{source.department}Ops",
    )
