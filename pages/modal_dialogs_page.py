from selenium.webdriver.common.by import By

from core.base_page import BasePage


class ModalDialogsPage(BasePage):
    PATH = "/modal-dialogs"

    OPEN_SMALL_MODAL  = (By.ID, "showSmallModal")
    OPEN_LARGE_MODAL  = (By.ID, "showLargeModal")
    CLOSE_SMALL_MODAL = (By.ID, "closeSmallModal")
    CLOSE_LARGE_MODAL = (By.ID, "closeLargeModal")
    ACTIVE_MODAL      = (By.CSS_SELECTOR, ".modal.show")
    MODAL_TITLE       = (By.CSS_SELECTOR, ".modal.show .modal-title")
    MODAL_BODY        = (By.CSS_SELECTOR, ".modal.show .modal-body")

    def open_small_modal(self) -> None:
        self.click(self.OPEN_SMALL_MODAL)

    def open_large_modal(self) -> None:
        self.click(self.OPEN_LARGE_MODAL)

    def close_small_modal(self) -> None:
        self.click(self.CLOSE_SMALL_MODAL)

    def close_large_modal(self) -> None:
        self.click(self.CLOSE_LARGE_MODAL)

    def is_modal_visible(self) -> bool:
        return self.is_visible(self.ACTIVE_MODAL)

    def is_modal_closed(self) -> bool:
        return self.wait_until_invisible(self.ACTIVE_MODAL)

    def get_modal_title(self) -> str:
        return self.get_text(self.MODAL_TITLE)

    def get_modal_body(self) -> str:
        return self.get_text(self.MODAL_BODY)
