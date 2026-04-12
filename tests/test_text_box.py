import pytest

from data.text_box_data import generate_text_box_data
from pages.text_box_page import TextBoxPage


@pytest.mark.ui
@pytest.mark.smoke
class TestTextBox:
    def test_fill_form_and_verify_output(self, driver) -> None:
        data = generate_text_box_data()
        page = TextBoxPage(driver)
        page.open_page()

        page.fill_form(
            name=data.full_name,
            email=data.email,
            current=data.current_address,
            permanent=data.permanent_address,
        )
        page.submit()

        output = page.get_output()

        assert data.full_name in output["name"]
        assert data.email in output["email"]
        assert data.current_address in output["current"]
        assert data.permanent_address in output["permanent"]
