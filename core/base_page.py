from typing import Tuple

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from core.config import BASE_URL, Timeouts

Locator = Tuple[str, str]


class BasePage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, Timeouts.DEFAULT)
        self.base_url = BASE_URL

    def navigate_to(self, path: str = "") -> None:
        self.driver.get(f"{self.base_url}{path}")

    def open(self) -> None:
        path = getattr(self, "PATH", None)
        if path is None:
            raise NotImplementedError(f"{self.__class__.__name__} must define a PATH attribute")
        self.navigate_to(path)

    def find(self, locator: Locator) -> WebElement:
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_all(self, locator: Locator) -> list[WebElement]:
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click(self, locator: Locator) -> None:
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def js_click(self, locator: Locator) -> None:
        """Restricted use: only when native click is not possible (e.g. ad overlay blocks element)."""
        self.driver.execute_script("arguments[0].click();", self.find(locator))

    def type(self, locator: Locator, text: str) -> None:
        field = self.find(locator)
        field.clear()
        field.send_keys(text)

    def get_text(self, locator: Locator) -> str:
        return self.find(locator).text

    def is_visible(self, locator: Locator) -> bool:
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except Exception:
            return False

    def wait_until_invisible(self, locator: Locator) -> bool:
        try:
            return bool(self.wait.until(EC.invisibility_of_element_located(locator)))
        except Exception:
            return False

    def scroll_to(self, locator: Locator) -> WebElement:
        element = self.find(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        return element

    def get_title(self) -> str:
        return self.driver.title

    def get_current_url(self) -> str:
        return self.driver.current_url

    def get_window_handles(self) -> list[str]:
        return self.driver.window_handles

    def get_current_window_handle(self) -> str:
        return self.driver.current_window_handle

    def wait_for_new_window(self, previous_handles: list[str]) -> str:
        self.wait.until(lambda driver: len(driver.window_handles) > len(previous_handles))
        for handle in self.driver.window_handles:
            if handle not in previous_handles:
                return handle
        raise ValueError("New browser window was expected but no new handle was found")

    def switch_to_window(self, handle: str) -> None:
        self.driver.switch_to.window(handle)

    def close_current_window(self) -> None:
        self.driver.close()
