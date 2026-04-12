from dataclasses import dataclass


@dataclass(frozen=True)
class BrowserWindowResult:
    url: str
    heading: str


EXPECTED_SAMPLE_HEADING = "This is a sample page"
EXPECTED_SAMPLE_URL = "https://demoqa.com/sample"
