import pytest
from pages.landing.newsletter import Newsletter

@pytest.mark.order(0)
def test_sign_to_newsletter(page_factory, ui_config) -> None:
    newsletter_page = Newsletter()
    newsletter_page
    return