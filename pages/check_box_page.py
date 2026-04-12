from selenium.webdriver.common.by import By

from core.base_page import BasePage


class CheckBoxPage(BasePage):
    PATH = "/checkbox"

    RESULT = (By.ID, "result")

    _COLLAPSED_SWITCHER = ".rc-tree-switcher.rc-tree-switcher_close"
    _NODE_CHECKBOX_TPL  = "span.rc-tree-checkbox[aria-label='Select {}']"

    def select_checkbox(self, node_name: str) -> None:
        self._reveal_node(node_name)
        locator = (By.CSS_SELECTOR, self._NODE_CHECKBOX_TPL.format(node_name))
        self.js_click(locator)

    def get_result_text(self) -> str:
        return self.get_text(self.RESULT)

    def _reveal_node(self, node_name: str) -> None:
        target_css = self._NODE_CHECKBOX_TPL.format(node_name)
        for _ in range(10):
            if self.driver.find_elements(By.CSS_SELECTOR, target_css):
                return
            collapsed = self.driver.find_elements(By.CSS_SELECTOR, self._COLLAPSED_SWITCHER)
            if not collapsed:
                raise ValueError(f"Cannot reveal node '{node_name}': tree fully expanded but node not found")
            prev_count = len(collapsed)
            collapsed[0].click()
            self.wait.until(
                lambda d: d.find_elements(By.CSS_SELECTOR, target_css)
                or len(d.find_elements(By.CSS_SELECTOR, self._COLLAPSED_SWITCHER)) != prev_count
            )
        raise ValueError(f"Checkbox node '{node_name}' not found after maximum expansion attempts")
