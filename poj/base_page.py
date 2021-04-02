import inspect
import json
import re

import yaml
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from .wrapper import black_list


class BasePage:
    params = {}
    _driver = None
    re_value = []

    def __init__(self, driver: WebDriver = None):
        if driver is None:
            options = Options()
            options.debugger_address = '127.0.0.1:9222'
            self._driver = webdriver.Chrome(options=options)
            # self._driver = webdriver.Remote(
            #     command_executor='http://192.168.254.128:5001/wd/hub',
            #     desired_capabilities=DesiredCapabilities.CHROME)
            self._driver.get('http://open.ctrl.link/member/#/login/login-account')
            self._driver.implicitly_wait(3)
        else:
            self._driver = driver

    def stop(self):
        self._driver.quit()

    @black_list
    def find(self, locator, value) -> WebElement:
        if isinstance(locator, tuple):
            element = self._driver.find_element(*locator)
        else:
            element = self._driver.find_element(locator, value)
        return element

    def finds(self, locator, value) -> [WebElement]:
        if isinstance(locator, tuple):
            elements = self._driver.find_elements(*locator)
        else:
            print('dirver:', self._driver)
            elements = self._driver.find_elements(locator, value)
        return elements

    def steps(self, path):
        with open(path, encoding='utf-8') as f:
            def_name = inspect.stack()[1].function
            steps = yaml.safe_load(f)[def_name]
        raw = json.dumps(steps)
        for key, value in self.params.items():
            raw = raw.replace('${' + key + '}', value)
        steps = json.loads(raw)
        for step in steps:
            if 'action' in step.keys():
                action = step['action']
                if 'send_keys' == action:
                    self.find(step['by'], step['locator']).send_keys(step['value'])
                if 'click' == action:
                    self.find(step['by'], step['locator']).click()
                if 're' == action:
                    text = self.find(step['by'], step['locator']).text
                    value_re = self.re_code(step['pattern'], text)
                    self.re_value.append(value_re)

    def re_code(self, pattern, value):
        re.compile(pattern).findall(value)
