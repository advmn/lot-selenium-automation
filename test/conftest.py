import os

import pytest
from selenium import webdriver
from dataclasses import dataclass
from selenium.webdriver.chrome.service import Service

from selenium_wrapper.driver import DriverRegistry


@dataclass
class UITestConfig:
    frontend_base_url: str
    user_email: str
    user_password: str

    @classmethod
    def from_env(cls) -> 'UITestConfig':
        return cls(
            frontend_base_url=os.environ.get("BASE_URL", "https://www.lot.com/pl/pl"),
            user_email=os.environ.get("USER_EMAIL", "adam.adach@wp.pl"),
            user_password=os.environ.get("USER_PASSWORD", "Test123")

        )


@pytest.fixture(scope="session")
def ui_config() -> UITestConfig:
    return UITestConfig.from_env()


@pytest.fixture(scope='session')
def page_factory(ui_config) -> None:
    chrome_options = webdriver.ChromeOptions()

    driver = webdriver.Chrome(
        service=Service(),
        options=chrome_options
    )
    driver.get(ui_config.frontend_base_url)
    DriverRegistry.set_driver(driver)
    yield
    driver.quit()
