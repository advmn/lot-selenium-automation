from functools import cached_property

from components.button.base import Button
from components.input.base import Input


class NewsletterForm:
    @cached_property
    def name_input(self) -> Input:
        return Input.from_id("mat-input-0")

    @cached_property
    def consents_btn(self) -> Button:
        return Button.from_span_text("Zgody")

    @cached_property
    def consents_types_btn(self) -> Button:
        return Button.from_id("mat-checkbox-2-input")

    @cached_property
    def sign_to_newsletter_btn(self) -> Button:
        return Button.from_span_text("Zapisz się")

    @cached_property
    def email_input(self) -> Input:
        return Input.from_classname("mat-form-field-flex ng-tns-c24-7")
    ##przejrzec div

    def sign_to_newsletter(self, name: str, email: str) -> None:
        self.name_input.fill(name)
        self.email_input.fill(email)
        self.consents_btn.click()
        self.consents_types_btn.click()
        self.sign_to_newsletter_btn.click()
