
from .base_page import BasePage


class Main(BasePage):
    # def login(self):
    #     self.finds(By.CSS_SELECTOR,'input.ivu-input-large')[0].send_keys('我是货主')
    #     self.finds(By.CSS_SELECTOR,'input.ivu-input-large')[1].send_keys('123456')
    #     self.find(By.CSS_SELECTOR,'button.ivu-btn-primary').click()

    def login(self, name, passwd):
        self.params['value'] = name
        self.params['passwd'] = passwd
        self.steps('./poj/main.yml')

