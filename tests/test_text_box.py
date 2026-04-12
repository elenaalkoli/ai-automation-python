import pytest

from data.text_box_data import generate_text_box_data
from pages.text_box_page import TextBoxPage
from services.text_box_service import TextBoxService


@pytest.mark.describe("[UI] [Text-Box Form] [Smoke]")
class TestTextBox:
    @pytest.mark.ui
    @pytest.mark.smoke
    def test_fill_form_and_verify_output(
        self,
        text_box_page: TextBoxPage,
        text_box_service: TextBoxService,
    ) -> None:
        text_box_page.open_page()
        data = generate_text_box_data()

        text_box_service.fill_and_submit(data)

        text_box_service.verify_result(data)
