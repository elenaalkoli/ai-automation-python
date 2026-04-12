from selenium.webdriver.remote.webdriver import WebDriver

from data.sortable_data import SortableResult
from pages.sortable_page import SortablePage
from services.base_service import BaseService


class SortableService(BaseService):
    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self._page = SortablePage(driver)

    def reverse_list_tab(self) -> SortableResult:
        self._page.activate_list_tab()
        original = self._page.get_list_order()
        self._page.reverse_list()
        final = self._page.get_list_order()
        return SortableResult(original_order=original, final_order=final)

    def reverse_grid_tab(self) -> SortableResult:
        self._page.activate_grid_tab()
        original = self._page.get_grid_order()
        self._page.reverse_grid()
        final = self._page.get_grid_order()
        return SortableResult(original_order=original, final_order=final)
