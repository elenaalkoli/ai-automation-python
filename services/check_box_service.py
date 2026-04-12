from selenium.webdriver.remote.webdriver import WebDriver

from pages.check_box_page import CheckBoxPage
from services.base_service import BaseService


class CheckBoxService(BaseService):
    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self._page = CheckBoxPage(driver)

    def select_and_get_result(self, node_name: str) -> str:
        self._page.select_checkbox(node_name)
        return self._page.get_result_text()
