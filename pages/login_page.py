from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from core.base_page import BasePage


class LoginPage(BasePage):
    PATH = "/login"

    USERNAME = (By.ID, "userName")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login")

    def login(self, username: str, password: str) -> None:
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.js_click(self.LOGIN_BTN)

    def wait_for_redirect(self) -> str:
        self.wait.until(EC.url_contains("/profile"))
        return self.get_current_url()
