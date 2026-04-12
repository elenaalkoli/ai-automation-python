import pytest

from pages.draggable_page import DraggablePage
from services.draggable_service import DraggableService


@pytest.mark.describe("[UI] [Draggable] [Regression]")
class TestDraggable:
    @pytest.mark.ui
    @pytest.mark.regression
    def test_simple_drag_moves_element(
        self,
        draggable_page: DraggablePage,
        draggable_service: DraggableService,
    ) -> None:
        draggable_page.open()

        result = draggable_service.drag_simple_element()

        assert result.moved, (
            f"Simple: element did not move. before={result.before}, after={result.after}"
        )

    @pytest.mark.ui
    @pytest.mark.regression
    def test_axis_x_drag_moves_only_horizontally(
        self,
        draggable_page: DraggablePage,
        draggable_service: DraggableService,
    ) -> None:
        draggable_page.open()

        result = draggable_service.drag_axis_x_element()

        exactly_one_axis = result.x_changed ^ result.y_changed
        assert result.moved, (
            f"AxisX: element did not move at all. before={result.before}, after={result.after}"
        )
        assert exactly_one_axis, (
            f"AxisX: expected exactly one axis to change. before={result.before}, after={result.after}"
        )

    @pytest.mark.ui
    @pytest.mark.regression
    def test_axis_y_drag_moves_only_vertically(
        self,
        draggable_page: DraggablePage,
        draggable_service: DraggableService,
    ) -> None:
        draggable_page.open()

        result = draggable_service.drag_axis_y_element()

        assert result.y_changed, (
            f"AxisY: Y did not change. before={result.before}, after={result.after}"
        )
        assert not result.x_changed, (
            f"AxisY: X should stay fixed. before={result.before}, after={result.after}"
        )

    @pytest.mark.ui
    @pytest.mark.regression
    def test_container_drag_moves_element_within_box(
        self,
        draggable_page: DraggablePage,
        draggable_service: DraggableService,
    ) -> None:
        draggable_page.open()

        result = draggable_service.drag_container_element()

        assert result.moved, (
            f"Container: element did not move. before={result.before}, after={result.after}"
        )

    @pytest.mark.ui
    @pytest.mark.regression
    def test_cursor_style_drag_moves_element(
        self,
        draggable_page: DraggablePage,
        draggable_service: DraggableService,
    ) -> None:
        draggable_page.open()

        result = draggable_service.drag_cursor_center_element()

        assert result.moved, (
            f"CursorStyle: element did not move. before={result.before}, after={result.after}"
        )
