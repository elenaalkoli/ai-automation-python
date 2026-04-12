import pytest

from services.text_box_service import TextBoxService


@pytest.mark.ui
@pytest.mark.smoke
class TestTextBox:
    def test_fill_form_and_verify_output(self, driver) -> None:
        service = TextBoxService(driver)

        data = service.fill_and_submit()

        service.verify_result(data)
