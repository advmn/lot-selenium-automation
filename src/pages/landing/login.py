from functools import cached_property

from components.button.base import Button
from components.input.base import Input


class LoginForm:
    @cached_property
    def email_input(self) -> Input:
        return Input.from_id("email")

    @cached_property
    def password_input(self) -> Input:
        return Input.from_id("password")

    @cached_property
    def continue_btn(self) -> Button:
        return Button.from_span_text("continue")

    @cached_property
    def login_input(self) -> Input:
        return Input.from_id("loginButtonheader-2b154c5db5")
