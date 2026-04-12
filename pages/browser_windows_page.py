from selenium.webdriver.common.by import By

from core.base_page import BasePage


class BrowserWindowsPage(BasePage):
    PATH = "/browser-windows"

    NEW_TAB_BUTTON = (By.ID, "tabButton")
    NEW_WINDOW_BUTTON = (By.ID, "windowButton")
    SAMPLE_HEADING = (By.ID, "sampleHeading")

    def click_new_tab(self) -> None:
        self.click(self.NEW_TAB_BUTTON)

    def click_new_window(self) -> None:
        self.click(self.NEW_WINDOW_BUTTON)

    def get_sample_heading_text(self) -> str:
        return self.get_text(self.SAMPLE_HEADING)
