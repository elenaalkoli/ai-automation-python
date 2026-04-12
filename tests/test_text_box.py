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
        text_box_page.open()
        data = generate_text_box_data()

        output = text_box_service.fill_and_submit(data)

        assert data.full_name in output["name"], \
            f"Name mismatch: expected '{data.full_name}' in '{output['name']}'"
        assert data.email in output["email"], \
            f"Email mismatch: expected '{data.email}' in '{output['email']}'"
        assert data.current_address in output["current"], \
            f"Current address mismatch: expected '{data.current_address}' in '{output['current']}'"
        assert data.permanent_address in output["permanent"], \
            f"Permanent address mismatch: expected '{data.permanent_address}' in '{output['permanent']}'"
