import time

from pageobject.app import App


class Testcase1:
    def setup(self):
        self.app = App()
    def teardown(self):
        self.app.stop()
    def test_case_login(self):
        self.app.start().main().login()

    def test_case_login2(self):
        self.app.start().main().login()