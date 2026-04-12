import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from core.driver_factory import DriverFactory
from pages.text_box_page import TextBoxPage
from services.text_box_service import TextBoxService


@pytest.fixture(scope="function")
def driver() -> WebDriver:
    web_driver = DriverFactory.create_driver()
    yield web_driver
    web_driver.quit()


# ── Page fixtures ─────────────────────────────────────────────────────────────

@pytest.fixture
def text_box_page(driver: WebDriver) -> TextBoxPage:
    return TextBoxPage(driver)


# ── Service fixtures ──────────────────────────────────────────────────────────

@pytest.fixture
def text_box_service(driver: WebDriver) -> TextBoxService:
    return TextBoxService(driver)
