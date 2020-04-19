"""

author: whiteP

modified time: 2020/4/19 16:49

"""
from selenium import webdriver


class BasePage:
    def __init__(self, driver=None):
        # 如果发现driver没有值，第一次实例化子类
        if driver is None:
            self.driver = webdriver.Chrome()
        # 如果发现有值，说明不是第一次实例化
        else:
            self.driver = driver
