from selenium.webdriver.remote.webdriver import WebDriver

from data.web_tables_data import WebTableCrudResult, WebTableRecord
from pages.web_tables_page import WebTablesPage
from services.base_service import BaseService


class WebTablesService(BaseService):
    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self._page = WebTablesPage(driver)

    def create_read_update_delete(
        self,
        created_record: WebTableRecord,
        updated_record: WebTableRecord,
    ) -> WebTableCrudResult:
        self._page.click_add()
        self._page.fill_record_form(created_record)
        self._page.submit_record_form()
        created_row = self._page.get_row_values_by_email(created_record.email)

        self._page.click_edit_by_email(created_record.email)
        self._page.fill_record_form(updated_record)
        self._page.submit_record_form()
        updated_row = self._page.get_row_values_by_email(updated_record.email)

        self._page.click_delete_by_email(updated_record.email)
        deleted = not self._page.record_exists(updated_record.email)

        return WebTableCrudResult(
            created_row=created_row,
            updated_row=updated_row,
            deleted=deleted,
        )
