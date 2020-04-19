"""

author: whiteP

modified time: 2020/4/19 20:56

"""
from selenium_2.page.base_page import BasePage


class Register(BasePage):
    # 填写表单
    def register(self):
        # 填写输入框
        self.driver.find_element_by_id("corp_name").send_keys("hello")
        # 填写输入框
        self.driver.find_element_by_id("manager_name").send_keys("abcde")
