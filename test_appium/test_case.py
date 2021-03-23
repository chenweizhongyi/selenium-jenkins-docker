import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction


class TestCase:
    def setup(self):
        caps={}
        caps["platformName"] = "Android"
        caps["deviceName"] = "abc"
        caps["appPackage"] = "io.appium.android.apis"
        caps["appActivity"] = ".ApiDemos"
        caps['noReset'] = "true"
        caps['chromedriverExecutable'] = "D:\\android_chrome\\chromedriver.exe"
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_case(self):
        self.driver.find_element(MobileBy.XPATH,"//*[@text='Views']").click()
        window_size_height = self.driver.get_window_size()["height"]
        window_size_width = self.driver.get_window_size()["width"]
        while True:
            TouchAction(self.driver).press(x=window_size_width*1/2,y=window_size_height*3/4)\
                .move_to(x=window_size_width*1/2,y=window_size_height*1/4).release().perform()
            try:
                self.driver.find_element(MobileBy.XPATH,"//*[@text='WebView']").click()
                break
            except:
                continue
        print(self.driver.contexts)
        self.driver.switch_to.context(self.driver.contexts[-1])
        self.driver.find_element_by_id('i_am_a_textbox').send_keys('33333')
        time.sleep(2)