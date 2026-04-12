import pytest

from pages.check_box_page import CheckBoxPage
from services.check_box_service import CheckBoxService


@pytest.mark.describe("[UI] [Check-Box] [Smoke]")
class TestCheckBox:
    @pytest.mark.ui
    @pytest.mark.smoke
    def test_select_classified_checkbox_and_verify_result(
        self,
        check_box_page: CheckBoxPage,
        check_box_service: CheckBoxService,
    ) -> None:
        check_box_page.open()

        result = check_box_service.select_and_get_result("Classified")

        assert "classified" in result, \
            f"Expected 'classified' in result text, got: '{result}'"
