import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from api.book_store_api import BookStoreApiClient
from core.driver_factory import DriverFactory
from data.book_store_data import SetupContext
from pages.books_page import BooksPage
from pages.browser_windows_page import BrowserWindowsPage
from pages.check_box_page import CheckBoxPage
from pages.login_page import LoginPage
from pages.modal_dialogs_page import ModalDialogsPage
from pages.draggable_page import DraggablePage
from pages.profile_page import ProfilePage
from pages.sortable_page import SortablePage
from pages.text_box_page import TextBoxPage
from pages.web_tables_page import WebTablesPage
from services.book_store_service import BookStoreService
from services.book_store_setup import BookStoreSetup
from services.browser_windows_service import BrowserWindowsService
from services.check_box_service import CheckBoxService
from services.modal_dialogs_service import ModalDialogsService
from services.draggable_service import DraggableService
from services.sortable_service import SortableService
from services.text_box_service import TextBoxService
from services.web_tables_service import WebTablesService


@pytest.fixture(scope="function")
def driver() -> WebDriver:
    web_driver = DriverFactory.create_driver()
    yield web_driver
    web_driver.quit()


@pytest.fixture
def text_box_page(driver: WebDriver) -> TextBoxPage:
    return TextBoxPage(driver)


@pytest.fixture
def browser_windows_page(driver: WebDriver) -> BrowserWindowsPage:
    return BrowserWindowsPage(driver)


@pytest.fixture
def text_box_service(driver: WebDriver) -> TextBoxService:
    return TextBoxService(driver)


@pytest.fixture
def browser_windows_service(driver: WebDriver) -> BrowserWindowsService:
    return BrowserWindowsService(driver)


@pytest.fixture
def check_box_page(driver: WebDriver) -> CheckBoxPage:
    return CheckBoxPage(driver)


@pytest.fixture
def check_box_service(driver: WebDriver) -> CheckBoxService:
    return CheckBoxService(driver)


@pytest.fixture
def web_tables_page(driver: WebDriver) -> WebTablesPage:
    return WebTablesPage(driver)


@pytest.fixture
def web_tables_service(driver: WebDriver) -> WebTablesService:
    return WebTablesService(driver)


@pytest.fixture
def modal_dialogs_page(driver: WebDriver) -> ModalDialogsPage:
    return ModalDialogsPage(driver)


@pytest.fixture
def modal_dialogs_service(driver: WebDriver) -> ModalDialogsService:
    return ModalDialogsService(driver)


@pytest.fixture
def sortable_page(driver: WebDriver) -> SortablePage:
    return SortablePage(driver)


@pytest.fixture
def sortable_service(driver: WebDriver) -> SortableService:
    return SortableService(driver)


@pytest.fixture
def draggable_page(driver: WebDriver) -> DraggablePage:
    return DraggablePage(driver)


@pytest.fixture
def draggable_service(driver: WebDriver) -> DraggableService:
    return DraggableService(driver)


@pytest.fixture(scope="function")
def book_store_api() -> BookStoreApiClient:
    return BookStoreApiClient()


@pytest.fixture(scope="function")
def book_store_ctx(book_store_api: BookStoreApiClient) -> SetupContext:
    ctx = (
        BookStoreSetup(book_store_api)
        .with_new_user()
        .with_book()
        .build()
    )
    yield ctx
    book_store_api.delete_all_books(ctx.user_id, ctx.token)
    book_store_api.delete_user(ctx.user_id, ctx.token)


@pytest.fixture
def login_page(driver: WebDriver) -> LoginPage:
    return LoginPage(driver)


@pytest.fixture
def books_page(driver: WebDriver) -> BooksPage:
    return BooksPage(driver)


@pytest.fixture
def profile_page(driver: WebDriver) -> ProfilePage:
    return ProfilePage(driver)


@pytest.fixture
def book_store_service(driver: WebDriver, book_store_api: BookStoreApiClient) -> BookStoreService:
    return BookStoreService(driver, book_store_api)
