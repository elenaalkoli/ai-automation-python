from selenium.webdriver.remote.webdriver import WebDriver

from data.check_box_data import CheckBoxData, CheckBoxResult
from pages.check_box_page import CheckBoxPage
from services.base_service import BaseService


class CheckBoxService(BaseService):
    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self._page = CheckBoxPage(driver)

    def expand_and_select(self, data: CheckBoxData) -> CheckBoxResult:
        for node_name in data.expand_path:
            self._page.expand_node(node_name)
        self._page.select_checkbox(data.target_node)
        return CheckBoxResult(
            visible=self._page.is_result_visible(),
            checked_items=self._page.get_checked_items(),
        )
