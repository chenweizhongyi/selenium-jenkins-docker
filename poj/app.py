from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver

from .base_page import BasePage
from .main import Main


class App(BasePage):
    def start(self):
        return self
    def main(self) -> Main:
        # print('driver app :',self._driver)
        return Main(self._driver)