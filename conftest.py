import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from core.driver_factory import DriverFactory
from pages.browser_windows_page import BrowserWindowsPage
from pages.check_box_page import CheckBoxPage
from pages.modal_dialogs_page import ModalDialogsPage
from pages.sortable_page import SortablePage
from pages.text_box_page import TextBoxPage
from pages.web_tables_page import WebTablesPage
from services.browser_windows_service import BrowserWindowsService
from services.check_box_service import CheckBoxService
from services.modal_dialogs_service import ModalDialogsService
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
