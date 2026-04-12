from typing import Tuple

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from core.config import IMPLICIT_WAIT

Locator = Tuple[str, str]


def wait_for_text(driver: WebDriver, locator: Locator, text: str, timeout: int = IMPLICIT_WAIT) -> bool:
    return WebDriverWait(driver, timeout).until(
        EC.text_to_be_present_in_element(locator, text)
    )


def wait_for_url_contains(driver: WebDriver, fragment: str, timeout: int = IMPLICIT_WAIT) -> bool:
    return WebDriverWait(driver, timeout).until(
        EC.url_contains(fragment)
    )
