import locators.common as CL

from selenium.webdriver.remote.webelement import WebElement

from selenium_wrapper.utils import wait_until_clickable


class Input:
    def __init__(self, element: WebElement):
        self._element = element

    @classmethod
    def from_id(cls, element_id: str) -> 'Input':
        element = wait_until_clickable(
            locator=CL.find_element_by_id(element_id),
            delay=30
        )
        return cls(element)

    @classmethod
    def from_class_name(cls, class_name: str) -> 'Input':
        element = wait_until_clickable(
            locator=CL.find_element_by_class_name(class_name),
            delay=30
        )
        return cls(element)

    def fill(self, text: str) -> None:
        self._element.send_keys(text)
