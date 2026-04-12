import pytest

from pages.check_box_page import CheckBoxPage


@pytest.mark.ui
@pytest.mark.regression
class TestCheckBox:
    def test_select_home_checkbox(self, driver) -> None:
        page = CheckBoxPage(driver)
        page.open_page()
        page.expand_all()
        page.select_home()

        assert "home" in page.get_result_text().lower()
