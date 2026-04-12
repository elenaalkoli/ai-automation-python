from collections.abc import Callable

from selenium.webdriver.remote.webdriver import WebDriver

from data.modal_dialogs_data import ModalResult
from pages.modal_dialogs_page import ModalDialogsPage
from services.base_service import BaseService


class ModalDialogsService(BaseService):
    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self._page = ModalDialogsPage(driver)

    def open_small_modal_and_collect(self) -> ModalResult:
        return self._collect_modal(
            open_fn=self._page.open_small_modal,
            close_fn=self._page.close_small_modal,
        )

    def open_large_modal_and_collect(self) -> ModalResult:
        return self._collect_modal(
            open_fn=self._page.open_large_modal,
            close_fn=self._page.close_large_modal,
        )

    def _collect_modal(
        self,
        open_fn: Callable[[], None],
        close_fn: Callable[[], None],
    ) -> ModalResult:
        open_fn()
        visible = self._page.is_modal_visible()
        title = self._page.get_modal_title()
        body = self._page.get_modal_body()
        close_fn()
        was_closed = self._page.is_modal_closed()
        return ModalResult(
            title=title,
            body=body,
            is_visible=visible,
            was_closed=was_closed,
        )
