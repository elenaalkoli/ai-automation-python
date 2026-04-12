from selenium.webdriver.remote.webdriver import WebDriver

from data.text_box_data import TextBoxData
from pages.text_box_page import TextBoxPage
from services.base_service import BaseService


class TextBoxService(BaseService):
    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self._page = TextBoxPage(driver)

    def fill_and_submit(self, data: TextBoxData) -> dict[str, str]:
        self._page.fill_form(
            name=data.full_name,
            email=data.email,
            current=data.current_address,
            permanent=data.permanent_address,
        )
        self._page.submit()
        return self._page.get_output()
