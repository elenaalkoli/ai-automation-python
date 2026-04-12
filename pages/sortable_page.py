from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from core.base_page import BasePage


class SortablePage(BasePage):
    PATH = "/sortable"

    LIST_TAB   = (By.ID, "demo-tab-list")
    GRID_TAB   = (By.ID, "demo-tab-grid")
    LIST_ITEMS = (By.CSS_SELECTOR, "#demo-tabpane-list .list-group-item")
    GRID_ITEMS = (By.CSS_SELECTOR, "#demo-tabpane-grid .list-group-item")

    def activate_list_tab(self) -> None:
        self.click(self.LIST_TAB)

    def activate_grid_tab(self) -> None:
        self.click(self.GRID_TAB)

    def get_list_order(self) -> list[str]:
        return [el.text.strip() for el in self.find_all(self.LIST_ITEMS)]

    def get_grid_order(self) -> list[str]:
        return [el.text.strip() for el in self.find_all(self.GRID_ITEMS)]

    def reverse_list(self) -> None:
        self._reverse_items(self.LIST_ITEMS)

    def reverse_grid(self) -> None:
        self._reverse_items(self.GRID_ITEMS)

    def _reverse_items(self, locator: tuple) -> None:
        n = len(self.find_all(locator))
        for i in range(n - 1):
            previous_order = self._get_order(locator)
            items = self.find_all(locator)
            self._drag_item_before(items[-1], items[i])
            self.wait.until(lambda driver: self._get_order(locator) != previous_order)

    def _drag_item_before(self, source: WebElement, target: WebElement) -> None:
        ActionChains(self.driver)\
            .click_and_hold(source)\
            .pause(0.3)\
            .move_to_element(target)\
            .pause(0.1)\
            .release()\
            .perform()

    def _get_order(self, locator: tuple) -> list[str]:
        return [el.text.strip() for el in self.find_all(locator)]
