from selenium.webdriver.remote.webdriver import WebDriver


class BaseService:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
