import os

from dotenv import load_dotenv

load_dotenv()

BASE_URL: str = os.getenv("DEMOQA_BASE_URL", "https://demoqa.com")
BROWSER: str = os.getenv("BROWSER", "chrome")
HEADLESS: bool = os.getenv("HEADLESS", "true").lower() == "true"
IMPLICIT_WAIT: int = int(os.getenv("IMPLICIT_WAIT", "10"))
WINDOW_SIZE: str = os.getenv("WINDOW_SIZE", "1920,1080")
