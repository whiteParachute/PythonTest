"""

author: whiteP

modified time: 2020/4/19 21:04

"""
from selenium_2.page.index import Index


class TestRegister:
    def setup(self):
        # 初始化index
        self.index = Index()

    def test_register(self):
        # 从index进入到注册页，完成输入
        self.index.goto_register().register()
