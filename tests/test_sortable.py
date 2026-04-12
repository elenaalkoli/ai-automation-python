import pytest

from pages.sortable_page import SortablePage
from services.sortable_service import SortableService


@pytest.mark.describe("[UI] [Sortable] [Regression]")
class TestSortable:
    @pytest.mark.ui
    @pytest.mark.regression
    def test_list_tab_reversed(
        self,
        sortable_page: SortablePage,
        sortable_service: SortableService,
    ) -> None:
        sortable_page.open()

        result = sortable_service.reverse_list_tab()

        expected = list(reversed(result.original_order))
        assert result.final_order == expected, (
            f"List not reversed.\n"
            f"  Expected : {expected}\n"
            f"  Actual   : {result.final_order}"
        )

    @pytest.mark.ui
    @pytest.mark.regression
    def test_grid_tab_reversed(
        self,
        sortable_page: SortablePage,
        sortable_service: SortableService,
    ) -> None:
        sortable_page.open()

        result = sortable_service.reverse_grid_tab()

        expected = list(reversed(result.original_order))
        assert result.final_order == expected, (
            f"Grid not reversed.\n"
            f"  Expected : {expected}\n"
            f"  Actual   : {result.final_order}"
        )
