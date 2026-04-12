import pytest

from pages.text_box_page import TextBoxPage


@pytest.mark.ui
@pytest.mark.smoke
class TestTextBox:
    def test_fill_form_and_verify_output(self, driver) -> None:
        page = TextBoxPage(driver)
        page.open_page()

        name = "John Doe"
        email = "johndoe@example.com"
        current = "123 Main St"
        permanent = "456 Elm St"

        page.fill_form(name, email, current, permanent)
        page.submit()

        output = page.get_output()

        assert name in output["name"]
        assert email in output["email"]
        assert current in output["current"]
        assert permanent in output["permanent"]
