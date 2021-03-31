import os

import pytest
import yaml
from selenium.webdriver.common.by import By

from poj.base_page import BasePage


class Main(BasePage):

    # def login(self):
    #     self.finds(By.CSS_SELECTOR,'input.ivu-input-large')[0].send_keys('我是货主')
    #     self.finds(By.CSS_SELECTOR,'input.ivu-input-large')[1].send_keys('123456')
    #     self.find(By.CSS_SELECTOR,'button.ivu-btn-primary').click()

    def login(self):
        # yaml.safe_load('./main.yml')
        # print(os.getcwd())
        # with open(r'.\main.yml',encoding='utf-8') as f:
        #     data = yaml.safe_load(f)
        #     print(data)
