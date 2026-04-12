from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import ElementClickInterceptedException

from core.base_page import BasePage


class WebTablesPage(BasePage):
    PATH = "/webtables"

    ADD_BUTTON = (By.ID, "addNewRecordButton")
    SEARCH_BOX = (By.ID, "searchBox")
    MODAL = (By.ID, "registration-form-modal")
    FORM = (By.ID, "userForm")
    FIRST_NAME = (By.ID, "firstName")
    LAST_NAME = (By.ID, "lastName")
    EMAIL = (By.ID, "userEmail")
    AGE = (By.ID, "age")
    SALARY = (By.ID, "salary")
    DEPARTMENT = (By.ID, "department")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "#userForm #submit")
    TABLE_ROWS = (By.CSS_SELECTOR, "tbody tr")

    _EDIT_IN_ROW = "span[title='Edit']"
    _DELETE_IN_ROW = "span[title='Delete']"
    _ROW_CELLS = "td"

    def click_add(self) -> None:
        self.click(self.ADD_BUTTON)

    def fill_record_form(
        self,
        first_name: str,
        last_name: str,
        email: str,
        age: str,
        salary: str,
        department: str,
    ) -> None:
        self.type(self.FIRST_NAME, first_name)
        self.type(self.LAST_NAME, last_name)
        self.type(self.EMAIL, email)
        self.type(self.AGE, age)
        self.type(self.SALARY, salary)
        self.type(self.DEPARTMENT, department)

    def submit_record_form(self) -> None:
        self.click(self.SUBMIT_BUTTON)

    def search(self, value: str) -> None:
        self.type(self.SEARCH_BOX, value)

    def clear_search(self) -> None:
        self.type(self.SEARCH_BOX, "")

    def get_row_values_by_email(self, email: str) -> list[str]:
        row = self._find_row_by_email(email)
        return [cell.text for cell in row.find_elements(By.CSS_SELECTOR, self._ROW_CELLS)[:6]]

    def click_edit_by_email(self, email: str) -> None:
        row = self._find_row_by_email(email)
        self._click_row_action(row.find_element(By.CSS_SELECTOR, self._EDIT_IN_ROW))

    def click_delete_by_email(self, email: str) -> None:
        row = self._find_row_by_email(email)
        self._click_row_action(row.find_element(By.CSS_SELECTOR, self._DELETE_IN_ROW))

    def record_exists(self, email: str) -> bool:
        self.search(email)
        rows = self.driver.find_elements(By.CSS_SELECTOR, self.TABLE_ROWS[1])
        for row in rows:
            cells = row.find_elements(By.CSS_SELECTOR, self._ROW_CELLS)
            if len(cells) >= 4 and cells[3].text == email:
                return True
        return False

    def _find_row_by_email(self, email: str) -> WebElement:
        self.search(email)
        rows = self.find_all(self.TABLE_ROWS)
        for row in rows:
            cells = row.find_elements(By.CSS_SELECTOR, self._ROW_CELLS)
            if len(cells) >= 4 and cells[3].text == email:
                return row
        raise ValueError(f"Web table record with email '{email}' not found")

    def _click_row_action(self, element: WebElement) -> None:
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});",
            element,
        )
        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)
