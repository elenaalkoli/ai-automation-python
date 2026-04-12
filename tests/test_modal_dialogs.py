import pytest

from pages.modal_dialogs_page import ModalDialogsPage
from services.modal_dialogs_service import ModalDialogsService


@pytest.mark.describe("[UI] [Modal Dialogs] [Regression]")
class TestModalDialogs:
    @pytest.mark.ui
    @pytest.mark.regression
    def test_small_modal_opens_and_closes(
        self,
        modal_dialogs_page: ModalDialogsPage,
        modal_dialogs_service: ModalDialogsService,
    ) -> None:
        modal_dialogs_page.open()

        result = modal_dialogs_service.open_small_modal_and_collect()

        assert result.is_visible, "Small modal was not visible after opening"
        assert result.title == "Small Modal", \
            f"Expected title 'Small Modal', got '{result.title}'"
        assert "small modal" in result.body.lower(), \
            f"Expected body to contain 'small modal', got '{result.body}'"
        assert result.was_closed, "Small modal was not closed after clicking Close"

    @pytest.mark.ui
    @pytest.mark.regression
    def test_large_modal_opens_and_closes(
        self,
        modal_dialogs_page: ModalDialogsPage,
        modal_dialogs_service: ModalDialogsService,
    ) -> None:
        modal_dialogs_page.open()

        result = modal_dialogs_service.open_large_modal_and_collect()

        assert result.is_visible, "Large modal was not visible after opening"
        assert result.title == "Large Modal", \
            f"Expected title 'Large Modal', got '{result.title}'"
        assert len(result.body) > 0, "Large modal body was empty"
        assert result.was_closed, "Large modal was not closed after clicking Close"
