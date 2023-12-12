import locators.common as CL

from selenium.common import ElementClickInterceptedException
from selenium.webdriver.remote.webelement import WebElement

from selenium_wrapper.utils import wait_until_clickable
from waiting import wait


class Button:
    def __init__(self, element: WebElement):
        self._element = element

    def click(self) -> None:
        wait(
            lambda: self._click(),
            timeout_seconds=10
        )

    def _click(self) -> bool:
        try:
            self._element.click()
        except ElementClickInterceptedException:
            return False
        return True

    @classmethod
    def from_span_text(cls, text: str) -> 'Button':
        element = wait_until_clickable(
            locator=CL.find_span_by_text(text),
            delay=30
        )
        return cls(element)

    @classmethod
    def from_id(cls, text: str) -> 'Button':
        element = wait_until_clickable(
            locator=CL.find_element_by_id(text),
            delay=30
        )
        return cls(element)

