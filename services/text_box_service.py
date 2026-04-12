from typing import Optional

from selenium.webdriver.remote.webdriver import WebDriver

from data.text_box_data import TextBoxData, generate_text_box_data
from pages.text_box_page import TextBoxPage
from services.base_service import BaseService


class TextBoxService(BaseService):
    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self._page = TextBoxPage(driver)

    def fill_and_submit(self, data: Optional[TextBoxData] = None) -> TextBoxData:
        form_data = data or generate_text_box_data()
        self._page.open_page()
        self._page.fill_form(
            name=form_data.full_name,
            email=form_data.email,
            current=form_data.current_address,
            permanent=form_data.permanent_address,
        )
        self._page.submit()
        return form_data

    def verify_result(self, expected: TextBoxData) -> None:
        output = self._page.get_output()
        assert expected.full_name in output["name"], \
            f"Name mismatch: expected '{expected.full_name}', got '{output['name']}'"
        assert expected.email in output["email"], \
            f"Email mismatch: expected '{expected.email}', got '{output['email']}'"
        assert expected.current_address in output["current"], \
            f"Current address mismatch: expected '{expected.current_address}', got '{output['current']}'"
        assert expected.permanent_address in output["permanent"], \
            f"Permanent address mismatch: expected '{expected.permanent_address}', got '{output['permanent']}'"
