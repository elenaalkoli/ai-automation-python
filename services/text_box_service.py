from data.text_box_data import TextBoxData
from pages.text_box_page import TextBoxPage


class TextBoxService:
    def __init__(self, page: TextBoxPage) -> None:
        self.page = page

    def fill_and_submit(self, data: TextBoxData) -> dict[str, str]:
        self.page.open_page()
        self.page.fill_form(
            name=data.full_name,
            email=data.email,
            current=data.current_address,
            permanent=data.permanent_address,
        )
        self.page.submit()
        return self.page.get_output()
