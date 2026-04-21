from typing import Optional

from api.book_store_api import BookStoreApiClient
from data.book_store_data import BookData, SetupContext, UserCredentials, generate_user_credentials


class BookStoreSetup:
    """Builder: fluent interface for composing test preconditions via API."""

    def __init__(self, api: BookStoreApiClient) -> None:
        self._api = api
        self._credentials: Optional[UserCredentials] = None
        self._user_id: Optional[str] = None
        self._token: Optional[str] = None
        self._book: Optional[BookData] = None

    def with_new_user(self) -> "BookStoreSetup":
        self._credentials = generate_user_credentials()
        self._user_id = self._api.create_user(
            self._credentials.username, self._credentials.password
        )
        self._token = self._api.generate_token(
            self._credentials.username, self._credentials.password
        )
        return self

    def with_book(self, isbn: Optional[str] = None) -> "BookStoreSetup":
        books = self._api.get_books()
        if isbn:
            raw = next(b for b in books if b["isbn"] == isbn)
        else:
            raw = books[0]
        self._book = BookData(
            isbn=raw["isbn"],
            title=raw["title"],
            author=raw["author"],
            publisher=raw["publisher"],
        )
        self._api.add_book(self._user_id, self._book.isbn, self._token)
        return self

    def build(self) -> SetupContext:
        if not all([self._credentials, self._user_id, self._token, self._book]):
            raise RuntimeError("BookStoreSetup: call with_new_user() and with_book() first")
        return SetupContext(
            credentials=self._credentials,
            user_id=self._user_id,
            token=self._token,
            book=self._book,
        )
