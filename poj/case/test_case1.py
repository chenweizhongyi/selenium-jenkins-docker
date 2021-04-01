# import sys
#
# print(sys.path)
import pytest

from poj.app import App


class Testcase1:
    def setup(self):
        self.app = App()
    def teardown(self):
        self.app.stop()

    @pytest.mark.parametrize('name, passwd', [('我是货主', '123456'), ('我是经纪人', '123456')])
    def test_case_login(self, name, passwd):
        self.main = self.app.start().main()
        self.main.login(name,passwd)

    # def test_case_login2(self):
    #     self.app.start().main().login()