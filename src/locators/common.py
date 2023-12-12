from selenium.webdriver.common.by import By


def find_span_by_text(text: str) -> tuple[str, str]:
    return By.XPATH, f'//span[text()=\'{text}\']'


def find_element_by_id(element_id: str) -> tuple[str, str]:
    return By.ID, f'{element_id}'


def find_element_by_class_name(class_name: str) -> tuple[str, str]:
    return By.CLASS_NAME, f'{class_name}'
