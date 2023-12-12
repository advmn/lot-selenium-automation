from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_wrapper.driver import DriverRegistry

import locators.common as CL


def wait_until(condition, locator, delay=15):
    return WebDriverWait(DriverRegistry.get_driver(), delay).until(
        condition(locator)
    )


def wait_until_clickable(locator, delay=10):
    return wait_until(EC.element_to_be_clickable, locator, delay)
