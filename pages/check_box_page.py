from selenium.webdriver.common.by import By

from core.base_page import BasePage


class CheckBoxPage(BasePage):
    PATH = "/checkbox"

    EXPAND_ALL_BTN = (By.CSS_SELECTOR, "button[title='Expand all']")
    HOME_CHECKBOX = (By.CSS_SELECTOR, "label[for='tree-node-home'] span.rct-checkbox")
    RESULT = (By.ID, "result")

    def open_page(self) -> None:
        self.open(self.PATH)

    def expand_all(self) -> None:
        self.click(self.EXPAND_ALL_BTN)

    def select_home(self) -> None:
        self.js_click(self.HOME_CHECKBOX)

    def get_result_text(self) -> str:
        return self.get_text(self.RESULT)
