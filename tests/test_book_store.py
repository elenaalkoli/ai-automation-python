import pytest

from data.book_store_data import SetupContext
from services.book_store_service import BookStoreService
from services.search_strategy import SearchByAuthor, SearchByTitle


@pytest.mark.describe("[UI] [BookStore] [Regression]")
class TestBookStore:
    @pytest.mark.ui
    @pytest.mark.regression
    def test_login_redirects_to_profile(
        self,
        book_store_ctx: SetupContext,
        book_store_service: BookStoreService,
    ) -> None:
        url = book_store_service.login(book_store_ctx)

        assert "/profile" in url, f"Expected redirect to /profile, got: {url}"

    @pytest.mark.ui
    @pytest.mark.regression
    def test_profile_shows_added_book(
        self,
        book_store_ctx: SetupContext,
        book_store_service: BookStoreService,
    ) -> None:
        book_store_service.login(book_store_ctx)
        username, titles = book_store_service.get_profile_state(book_store_ctx)

        assert username == book_store_ctx.credentials.username, (
            f"Expected username '{book_store_ctx.credentials.username}', got '{username}'"
        )
        assert book_store_ctx.book.title in titles, (
            f"Book '{book_store_ctx.book.title}' not found in profile. Titles: {titles}"
        )

    @pytest.mark.ui
    @pytest.mark.regression
    def test_catalog_search_by_title(
        self,
        book_store_ctx: SetupContext,
        book_store_service: BookStoreService,
    ) -> None:
        book_store_service.login(book_store_ctx)
        results = book_store_service.search_in_catalog(book_store_ctx, SearchByTitle())

        assert len(results) > 0, "Search by title returned no results"
        assert all(
            book_store_ctx.book.title.lower() in r.lower() for r in results
        ), f"Unexpected results for title search: {results}"

    @pytest.mark.ui
    @pytest.mark.regression
    def test_catalog_search_by_author(
        self,
        book_store_ctx: SetupContext,
        book_store_service: BookStoreService,
    ) -> None:
        book_store_service.login(book_store_ctx)
        results = book_store_service.search_in_catalog(book_store_ctx, SearchByAuthor())

        assert len(results) > 0, "Search by author returned no results"

    @pytest.mark.ui
    @pytest.mark.regression
    def test_delete_book_removes_it_from_profile(
        self,
        book_store_ctx: SetupContext,
        book_store_service: BookStoreService,
    ) -> None:
        book_store_service.login(book_store_ctx)
        deleted = book_store_service.delete_book_from_profile(book_store_ctx)

        assert deleted, (
            f"Book '{book_store_ctx.book.title}' still present in profile after deletion"
        )
