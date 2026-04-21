from abc import ABC, abstractmethod

from data.book_store_data import BookData


class SearchStrategy(ABC):
    @abstractmethod
    def get_query(self, book: BookData) -> str: ...


class SearchByTitle(SearchStrategy):
    def get_query(self, book: BookData) -> str:
        return book.title


class SearchByAuthor(SearchStrategy):
    def get_query(self, book: BookData) -> str:
        return book.author
