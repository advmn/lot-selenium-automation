from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import locators.common as CL
from selenium_wrapper.utils import wait_until


class Notification:
    def __init__(self, element: WebElement):
        self._element = element

    @property
    def text(self) -> str:
        p_element = self._element.find_element(By.TAG_NAME, "p")
        return p_element.text

    @classmethod
    def from_class_name(cls, class_name: str) -> 'Notification':
        element = wait_until(
            locator=CL.find_element_by_class_name(class_name),
            delay=30
        )
        return cls(element)

    def close(self) -> None:
        close_btn = self._element.find_element(By.TAG_NAME, "button")
        close_btn.click()
