from .base_page import BasePage


class Register(BasePage):

    def input_value(self):
        self.steps('./poj/register.yaml')