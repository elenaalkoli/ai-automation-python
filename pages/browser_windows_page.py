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
