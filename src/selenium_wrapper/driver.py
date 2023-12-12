from selenium.webdriver.chrome.webdriver import WebDriver


class DriverRegistry:
    _DRIVER_INSTANCE: WebDriver = None

    @classmethod
    def get_driver(cls) -> WebDriver:
        return cls._DRIVER_INSTANCE

    @classmethod
    def set_driver(cls, driver: WebDriver) -> None:
        cls._DRIVER_INSTANCE = driver
