import os

from dotenv import load_dotenv

load_dotenv()

BASE_URL: str = os.getenv("DEMOQA_BASE_URL", "https://demoqa.com")
BROWSER: str = os.getenv("BROWSER", "chrome")
HEADLESS: bool = os.getenv("HEADLESS", "true").lower() == "true"
WINDOW_SIZE: str = os.getenv("WINDOW_SIZE", "1920,1080")


class Timeouts:
    DEFAULT: int = int(os.getenv("DEFAULT_WAIT", "10"))
    ELEMENT_VISIBLE: int = int(os.getenv("ELEMENT_VISIBLE_WAIT", "10"))
    PAGE_LOAD: int = int(os.getenv("PAGE_LOAD_WAIT", "30"))
