import pytest

from pages.radio_button_page import RadioButtonPage


@pytest.mark.ui
@pytest.mark.smoke
class TestRadioButton:
    def test_select_yes(self, driver) -> None:
        page = RadioButtonPage(driver)
        page.open_page()
        page.select_yes()

        assert page.get_result_text() == "Yes"

    def test_select_impressive(self, driver) -> None:
        page = RadioButtonPage(driver)
        page.open_page()
        page.select_impressive()

        assert page.get_result_text() == "Impressive"
