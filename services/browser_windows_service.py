from collections.abc import Callable

from selenium.webdriver.remote.webdriver import WebDriver

from data.browser_windows_data import BrowserWindowResult
from pages.browser_windows_page import BrowserWindowsPage
from services.base_service import BaseService


class BrowserWindowsService(BaseService):
    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self._page = BrowserWindowsPage(driver)

    def open_new_tab_and_collect(self) -> BrowserWindowResult:
        return self._open_secondary_window_and_collect(self._page.click_new_tab)

    def open_new_window_and_collect(self) -> BrowserWindowResult:
        return self._open_secondary_window_and_collect(self._page.click_new_window)

    def _open_secondary_window_and_collect(self, trigger: Callable[[], None]) -> BrowserWindowResult:
        original_handle = self._page.get_current_window_handle()
        previous_handles = self._page.get_window_handles()

        trigger()
        new_handle = self._page.wait_for_new_window(previous_handles)
        self._page.switch_to_window(new_handle)

        result = BrowserWindowResult(
            url=self._page.get_current_url(),
            heading=self._page.get_sample_heading_text(),
        )

        self._page.close_current_window()
        self._page.switch_to_window(original_handle)
        return result
