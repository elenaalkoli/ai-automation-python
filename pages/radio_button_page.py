from selenium.webdriver.common.by import By

from core.base_page import BasePage


class RadioButtonPage(BasePage):
    PATH = "/radio-button"

    YES_RADIO = (By.CSS_SELECTOR, "label[for='yesRadio']")
    IMPRESSIVE_RADIO = (By.CSS_SELECTOR, "label[for='impressiveRadio']")
    RESULT = (By.CSS_SELECTOR, ".mt-3 span.text-success")

    def open_page(self) -> None:
        self.open(self.PATH)

    def select_yes(self) -> None:
        self.click(self.YES_RADIO)

    def select_impressive(self) -> None:
        self.click(self.IMPRESSIVE_RADIO)

    def get_result_text(self) -> str:
        return self.get_text(self.RESULT)
