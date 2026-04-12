import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from core.driver_factory import DriverFactory


@pytest.fixture(scope="function")
def driver() -> WebDriver:
    web_driver = DriverFactory.create_driver()
    yield web_driver
    web_driver.quit()
