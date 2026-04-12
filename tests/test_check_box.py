import pytest

from data.check_box_data import classified_selection
from pages.check_box_page import CheckBoxPage
from services.check_box_service import CheckBoxService


@pytest.mark.describe("[UI] [CheckBox] [Smoke]")
class TestCheckBox:
    @pytest.mark.ui
    @pytest.mark.smoke
    def test_select_classified_node(
        self,
        check_box_page: CheckBoxPage,
        check_box_service: CheckBoxService,
    ) -> None:
        check_box_page.open()
        data = classified_selection()

        result = check_box_service.expand_and_select(data)

        assert result.visible, "Result block is not visible after checkbox selection"
        assert data.expected_label in result.checked_items, \
            f"Expected '{data.expected_label}' in checked items, got: {result.checked_items}"
