from functools import cached_property

from components.button.base import Button
from pages.landing.login import LoginForm
from pages.landing.newsletter import NewsletterForm


class LandingPage(LoginForm, NewsletterForm):
    @cached_property
    def cookies_btn(self) -> Button:
        return Button.from_id("onetrust-accept-btn-handler")
