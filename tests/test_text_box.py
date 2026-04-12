import pytest

from data.text_box_data import generate_text_box_data
from pages.text_box_page import TextBoxPage
from services.text_box_service import TextBoxService


@pytest.mark.ui
@pytest.mark.smoke
class TestTextBox:
    def test_fill_form_and_verify_output(self, driver) -> None:
        data = generate_text_box_data()
        service = TextBoxService(TextBoxPage(driver))

        output = service.fill_and_submit(data)

        assert data.full_name in output["name"]
        assert data.email in output["email"]
        assert data.current_address in output["current"]
        assert data.permanent_address in output["permanent"]
