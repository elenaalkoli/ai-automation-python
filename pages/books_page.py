from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from core.base_page import BasePage


class BooksPage(BasePage):
    PATH = "/books"

    SEARCH_BOX = (By.ID, "searchBox")

    def wait_for_books(self) -> None:
        self.wait.until(EC.visibility_of_element_located(self.SEARCH_BOX))

    def _parse_titles_from_body(self) -> list[str]:
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        start = body_text.find("Publisher\n")
        end = body_text.find("\nPrevious")
        if start == -1:
            return []
        block = body_text[start + len("Publisher\n"):]
        if end != -1:
            block = body_text[start + len("Publisher\n"):end]
        titles = []
        for line in block.splitlines():
            line = line.strip()
            if line:
                titles.append(line)
        return titles[::2]

    def get_book_titles(self) -> list[str]:
        self.wait_for_books()
        return self._parse_titles_from_body()

    def search(self, query: str) -> None:
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_BOX))
        field = self.find(self.SEARCH_BOX)
        field.clear()
        field.send_keys(query)
        self.wait.until(EC.text_to_be_present_in_element_value(self.SEARCH_BOX, query))

    def get_search_results(self) -> list[str]:
        return self._parse_titles_from_body()
