from selenium.webdriver.common.by import By

from core.base_page import BasePage


class CheckBoxPage(BasePage):
    PATH = "/checkbox"

    TREENODE     = (By.CSS_SELECTOR, ".rc-tree-treenode")
    NODE_SWITCHER = ".rc-tree-switcher"
    RESULT        = (By.ID, "result")
    RESULT_ITEMS  = (By.CSS_SELECTOR, "#result span.text-success")

    _NODE_TITLE_TPL    = "span[title='{}']"
    _NODE_CHECKBOX_TPL = "span.rc-tree-checkbox[aria-label='Select {}']"

    def expand_node(self, node_name: str) -> None:
        nodes = self.find_all(self.TREENODE)
        for node in nodes:
            if node.find_elements(By.CSS_SELECTOR, self._NODE_TITLE_TPL.format(node_name)):
                node.find_element(By.CSS_SELECTOR, self.NODE_SWITCHER).click()
                return
        raise ValueError(f"Checkbox node '{node_name}' not found in tree")

    def select_checkbox(self, node_name: str) -> None:
        locator = (By.CSS_SELECTOR, self._NODE_CHECKBOX_TPL.format(node_name))
        self.js_click(locator)

    def is_result_visible(self) -> bool:
        return self.is_visible(self.RESULT)

    def get_checked_items(self) -> list[str]:
        return [el.text for el in self.find_all(self.RESULT_ITEMS)]
