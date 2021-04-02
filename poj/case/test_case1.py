# import sys
#
# print(sys.path)
import os

import pytest
import yaml
from ..app import App


class Testcase1:
    def setup(self):
        self.app = App()
    def teardown(self):
        self.app.stop()
    print(os.getcwd())

    @pytest.mark.parametrize('name, passwd', yaml.safe_load(open('./poj/case/test_case1.yaml',encoding='UTF-8')))
    def test_case_login(self, name, passwd):
        # print(yaml.safe_load(open('./poj/case/test_case1.yaml', encoding='UTF-8')))
        self.main = self.app.start().main()
        self.main.login(name, passwd)

    # def test_case_login2(self):
    #     self.app.start().main().login()