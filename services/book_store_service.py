from selenium.webdriver.remote.webdriver import WebDriver

from api.book_store_api import BookStoreApiClient
from data.book_store_data import BookStoreResult, SetupContext
from pages.books_page import BooksPage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from services.base_service import BaseService
from services.search_strategy import SearchStrategy


class BookStoreService(BaseService):
    """Facade: hides the multi-page login → profile → catalog → delete flow."""

    def __init__(self, driver: WebDriver, api: BookStoreApiClient) -> None:
        super().__init__(driver)
        self._api = api
        self._login_page = LoginPage(driver)
        self._books_page = BooksPage(driver)
        self._profile_page = ProfilePage(driver)

    def login(self, ctx: SetupContext) -> str:
        self._login_page.open()
        self._login_page.login(ctx.credentials.username, ctx.credentials.password)
        return self._login_page.wait_for_redirect()

    def get_profile_state(self, ctx: SetupContext) -> tuple[str, list[str]]:
        self._profile_page.open()
        self._profile_page.wait_for_book(ctx.book.isbn)
        username = self._profile_page.get_username()
        titles = self._profile_page.get_book_titles()
        return username, titles

    def search_in_catalog(self, ctx: SetupContext, strategy: SearchStrategy) -> list[str]:
        self._books_page.open()
        self._books_page.wait_for_books()
        query = strategy.get_query(ctx.book)
        self._books_page.search(query)
        import time; time.sleep(1)
        return self._books_page.get_search_results()

    def delete_book_from_profile(self, ctx: SetupContext) -> bool:
        self._profile_page.open()
        self._profile_page.wait_for_book(ctx.book.isbn)
        self._profile_page.delete_book(ctx.book.isbn)
        self._profile_page.confirm_delete()
        self._profile_page.open()
        return not self._profile_page.is_book_present(ctx.book.isbn)
