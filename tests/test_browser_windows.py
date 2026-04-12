import pytest

from data.browser_windows_data import EXPECTED_SAMPLE_HEADING, EXPECTED_SAMPLE_URL
from pages.browser_windows_page import BrowserWindowsPage
from services.browser_windows_service import BrowserWindowsService


@pytest.mark.describe("[UI] [Browser Windows] [Regression]")
class TestBrowserWindows:
    @pytest.mark.ui
    @pytest.mark.regression
    def test_new_tab_and_new_window_open_sample_page(
        self,
        browser_windows_page: BrowserWindowsPage,
        browser_windows_service: BrowserWindowsService,
    ) -> None:
        browser_windows_page.open()

        tab_result = browser_windows_service.open_new_tab_and_collect()
        window_result = browser_windows_service.open_new_window_and_collect()

        assert tab_result.url == EXPECTED_SAMPLE_URL
        assert tab_result.heading == EXPECTED_SAMPLE_HEADING
        assert window_result.url == EXPECTED_SAMPLE_URL
        assert window_result.heading == EXPECTED_SAMPLE_HEADING
