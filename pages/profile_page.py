from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from core.base_page import BasePage


class ProfilePage(BasePage):
    PATH = "/profile"

    USERNAME_VALUE = (By.ID, "userName-value")
    BOOK_TITLE_LINKS = (By.CSS_SELECTOR, ".rt-tbody .rt-td a")
    CONFIRM_OK_BTN = (By.ID, "closeSmallModal-ok")

    _DELETE_BTN_TPL = "#delete-record-{}"

    def get_username(self) -> str:
        return self.find(self.USERNAME_VALUE).text

    def wait_for_book(self, isbn: str) -> None:
        locator = (By.CSS_SELECTOR, self._DELETE_BTN_TPL.format(isbn))
        self.wait.until(EC.presence_of_element_located(locator))
        self.scroll_to(locator)

    def get_book_titles(self) -> list[str]:
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        start = body_text.find("Action\n")
        end = body_text.find("\nPrevious")
        if start == -1 or end == -1:
            return []
        block = body_text[start + len("Action\n"):end].strip()
        titles = []
        for line in block.splitlines():
            line = line.strip()
            if line:
                titles.append(line)
                break
        return titles

    def delete_book(self, isbn: str) -> None:
        locator = (By.CSS_SELECTOR, self._DELETE_BTN_TPL.format(isbn))
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def confirm_delete(self) -> None:
        self.wait.until(EC.element_to_be_clickable(self.CONFIRM_OK_BTN)).click()

    def is_book_present(self, isbn: str) -> bool:
        locator = (By.CSS_SELECTOR, self._DELETE_BTN_TPL.format(isbn))
        els = self.driver.find_elements(*locator)
        return bool(els)
