from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC

from core.base_page import BasePage
from data.draggable_data import DragPosition, DragResult


class DraggablePage(BasePage):
    PATH = "/dragabble"

    TAB_SIMPLE    = (By.ID, "draggableExample-tab-simple")
    TAB_AXIS      = (By.ID, "draggableExample-tab-axisRestriction")
    TAB_CONTAINER = (By.ID, "draggableExample-tab-containerRestriction")
    TAB_CURSOR    = (By.ID, "draggableExample-tab-cursorStyle")

    SIMPLE_BOX    = (By.ID, "dragBox")
    AXIS_X        = (By.ID, "restrictedX")
    AXIS_Y        = (By.ID, "restrictedY")
    CONTAINER_BOX = (By.CSS_SELECTOR, "#containmentWrapper .draggable")
    CURSOR_CENTER = (By.ID, "cursorCenter")

    def activate_simple_tab(self) -> None:
        self.click(self.TAB_SIMPLE)

    def activate_axis_tab(self) -> None:
        self.click(self.TAB_AXIS)

    def activate_container_tab(self) -> None:
        self.click(self.TAB_CONTAINER)

    def activate_cursor_tab(self) -> None:
        self.click(self.TAB_CURSOR)

    def drag_simple(self, offset_x: int, offset_y: int) -> DragResult:
        return self._drag_element(self.SIMPLE_BOX, offset_x, offset_y)

    def drag_axis_x(self, offset_x: int, offset_y: int) -> DragResult:
        return self._drag_element(self.AXIS_X, offset_x, offset_y)

    def drag_axis_y(self, offset_x: int, offset_y: int) -> DragResult:
        return self._drag_element(self.AXIS_Y, offset_x, offset_y)

    def drag_container(self, offset_x: int, offset_y: int) -> DragResult:
        return self._drag_element(self.CONTAINER_BOX, offset_x, offset_y)

    def drag_cursor_center(self, offset_x: int, offset_y: int) -> DragResult:
        return self._drag_element(self.CURSOR_CENTER, offset_x, offset_y)

    def _drag_element(self, locator: tuple, offset_x: int, offset_y: int) -> DragResult:
        element = self.wait.until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)
        before = self._get_position(element)
        self._perform_drag(element, offset_x, offset_y)
        element = self.find(locator)
        after = self._get_position(element)
        return DragResult(before=before, after=after)

    def _get_position(self, element: WebElement) -> DragPosition:
        """Read position from inline style if set (after drag), else from getBoundingClientRect."""
        x, y = self.driver.execute_script("""
            const s = arguments[0].style;
            const left = parseFloat(s.left);
            const top  = parseFloat(s.top);
            if (!isNaN(left) || !isNaN(top)) {
                return [isNaN(left) ? 0 : left, isNaN(top) ? 0 : top];
            }
            const r = arguments[0].getBoundingClientRect();
            return [Math.round(r.x), Math.round(r.y)];
        """, element)
        return DragPosition(x=x, y=y)

    def _perform_drag(self, element: WebElement, offset_x: int, offset_y: int) -> None:
        ActionChains(self.driver)\
            .click_and_hold(element)\
            .pause(0.2)\
            .move_by_offset(offset_x, offset_y)\
            .pause(0.1)\
            .release()\
            .perform()
