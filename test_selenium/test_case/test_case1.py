import time
import re
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.options import Options


class TestCase:

    def setup(self):
        # options = Options()
        # options.debugger_address ="127.0.0.1:9222"
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def teardown(self):
        time.sleep(20)
        self.driver.quit()

    # def test_case1(self):
    #     WebDriverWait(self.driver,5).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,".btn-login")))
    #     self.driver.find_element(By.CSS_SELECTOR,".btn-login").click()
    #     self.driver.find_element(By.CSS_SELECTOR,'.ivu-input-type-text>input').send_keys('15228845998')
    #     self.driver.find_element(By.CSS_SELECTOR,'.ivu-input-type-password>input').send_keys('123456')
    #     self.driver.find_element(By.CSS_SELECTOR,'.ivu-form-item-content>button').click()
    #
    #     time.sleep(5)

    def test_logon(self):
        self.driver.get('http://www.ctrl.link/')
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "span.btn-register")))
        self.driver.find_element(By.CSS_SELECTOR,"span.btn-register").click()
        self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='建议使用企业简称']").send_keys('有丰富哈密')
        self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='请输入手机号']").send_keys('15624812384')
        self.driver.find_element(By.CSS_SELECTOR, "span[class='primaryColor']").click()
        text = self.driver.find_element(By.CSS_SELECTOR,"div[class='ivu-modal-confirm-body']>div").text
        time.sleep(2)
        yzm = re.search('\\d{6}',text).group()
        self.driver.find_element(By.CSS_SELECTOR,"div.ivu-modal-confirm-footer>button>span").click()
        self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='请输入验证码']").send_keys(yzm)
        self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='请输入6-20位登录密码']").send_keys(yzm)
        self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='请再次输入密码']").send_keys(yzm)
        self.driver.find_element(By.CSS_SELECTOR, "div.ivu-select").click()
        self.driver.find_element(By.CSS_SELECTOR, "div.ivu-select>div:nth-child(2)>ul:nth-child(2)>li:nth-child(2)").click()
        self.driver.find_element(By.CSS_SELECTOR,"button.xx-btn").click()
        print(self.driver.switch_to.alert().text)

    # def test_renzheng(self):
    #     # self.driver.get('http://www.ctrl.link/')
    #     self.driver.find_element(By.CSS_SELECTOR,"a.xx-btn-text").click()
    #     windows = self.driver.window_handles
    #     self.driver.switch_to.window(windows[-1])
    #     self.driver.find_element(By.CSS_SELECTOR,"input[placeholder='请填写营业执照上的企业名称']").click()