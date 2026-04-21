import uuid
from dataclasses import dataclass, field


@dataclass(frozen=True)
class UserCredentials:
    username: str
    password: str


@dataclass(frozen=True)
class BookData:
    isbn: str
    title: str
    author: str
    publisher: str


@dataclass(frozen=True)
class SetupContext:
    credentials: UserCredentials
    user_id: str
    token: str
    book: BookData


@dataclass(frozen=True)
class BookStoreResult:
    username_displayed: str
    profile_book_titles: list[str]
    search_results: list[str]
    book_deleted: bool


def generate_user_credentials() -> UserCredentials:
    uid = uuid.uuid4().hex[:8]
    return UserCredentials(username=f"tst_{uid}", password="Test@12345!")
