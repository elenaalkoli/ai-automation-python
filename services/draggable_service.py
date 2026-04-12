from selenium.webdriver.remote.webdriver import WebDriver

from data.draggable_data import DragResult
from pages.draggable_page import DraggablePage
from services.base_service import BaseService


class DraggableService(BaseService):
    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self._page = DraggablePage(driver)

    def drag_simple_element(self) -> DragResult:
        self._page.activate_simple_tab()
        return self._page.drag_simple(offset_x=80, offset_y=80)

    def drag_axis_x_element(self) -> DragResult:
        self._page.activate_axis_tab()
        return self._page.drag_axis_x(offset_x=80, offset_y=0)

    def drag_axis_y_element(self) -> DragResult:
        self._page.activate_axis_tab()
        return self._page.drag_axis_y(offset_x=0, offset_y=80)

    def drag_container_element(self) -> DragResult:
        self._page.activate_container_tab()
        return self._page.drag_container(offset_x=30, offset_y=20)

    def drag_cursor_center_element(self) -> DragResult:
        self._page.activate_cursor_tab()
        return self._page.drag_cursor_center(offset_x=50, offset_y=50)
