from selenium.webdriver.common.by import By

from core.base_page import BasePage


class TextBoxPage(BasePage):
    PATH = "/text-box"

    # ── Form inputs ───────────────────────────────────────────────────────────
    FULL_NAME         = (By.ID, "userName")
    EMAIL             = (By.ID, "userEmail")
    CURRENT_ADDRESS   = (By.ID, "currentAddress")
    PERMANENT_ADDRESS = (By.ID, "permanentAddress")

    # Scoped to #userForm to avoid matching any other #submit on the page
    SUBMIT_BTN = (By.CSS_SELECTOR, "#userForm #submit")

    # ── Output block ─────────────────────────────────────────────────────────
    # Scoped to #output: currentAddress / permanentAddress IDs are shared
    # with input fields above — without scope the wrong element would be matched.
    # Bootstrap utility classes (.mb-1) intentionally avoided — they change with lib updates.
    OUTPUT_NAME      = (By.CSS_SELECTOR, "#output #name")
    OUTPUT_EMAIL     = (By.CSS_SELECTOR, "#output #email")
    OUTPUT_CURRENT   = (By.CSS_SELECTOR, "#output #currentAddress")
    OUTPUT_PERMANENT = (By.CSS_SELECTOR, "#output #permanentAddress")

    def open_page(self) -> None:
        self.open(self.PATH)

    def fill_form(self, name: str, email: str, current: str, permanent: str) -> None:
        self.type(self.FULL_NAME, name)
        self.type(self.EMAIL, email)
        self.type(self.CURRENT_ADDRESS, current)
        self.type(self.PERMANENT_ADDRESS, permanent)

    def submit(self) -> None:
        self.js_click(self.SUBMIT_BTN)

    def get_output(self) -> dict[str, str]:
        return {
            "name": self.get_text(self.OUTPUT_NAME),
            "email": self.get_text(self.OUTPUT_EMAIL),
            "current": self.get_text(self.OUTPUT_CURRENT),
            "permanent": self.get_text(self.OUTPUT_PERMANENT),
        }
