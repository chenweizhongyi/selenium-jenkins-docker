from .base_page import BasePage
from .register import Register


class Main(BasePage):
    # def login(self):
    #     self.finds(By.CSS_SELECTOR,'input.ivu-input-large')[0].send_keys('我是货主')
    #     self.finds(By.CSS_SELECTOR,'input.ivu-input-large')[1].send_keys('123456')
    #     self.find(By.CSS_SELECTOR,'button.ivu-btn-primary').click()

    def login(self, name, passwd):
        self.params['name'] = name
        self.params['passwd'] = passwd
        self.steps('./poj/main.yml')

    def register(self) -> Register:
        self.steps('./poj/main.yml')
        return Register(self._driver)
