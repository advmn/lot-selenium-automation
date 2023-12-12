import pytest

from pages.landing.login import LoginPage


@pytest.mark.order(1)
def test_log_in(page_factory, ui_config):
    login_page = LoginPage()
    login_page.log_in(email=ui_config.user_email, password=ui_config.user_password)
    print("Test")