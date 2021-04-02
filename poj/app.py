from .base_page import BasePage
from .main import Main


class App(BasePage):
    def start(self):
        # pass
        return self

    def main(self) -> Main:
        # print('driver app :',self._driver)
        return Main(self._driver)
