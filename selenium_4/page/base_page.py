"""

author: whiteP

modified time: 2020/4/19 21:18

"""
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    # 把driver提取出来
    _driver = ""
    base_url = ""

    def __init__(self, reuse=False):
        if reuse:
            # 如果发现driver是空，就服用已有的浏览器
            opts = webdriver.ChromeOptions()
            opts.debugger_address = "127.0.0.1:9222"
            self._driver = webdriver.Chrome(options=opts)
        else:
            # new chrome
            self._driver = webdriver.Chrome()
        if self.base_url != "":
            self._driver.get(self.base_url)
        # 隐式等待，解决元素加载过慢问题
        self._driver.implicitly_wait(3)

    # using to find element
    def find(self, by, locator):
        return self._driver.find_element(by, locator)

    def finds(self, by, locator):
        return self._driver.find_elements(by, locator)

    # 显式等待
    def wait_for(self, fun):
        # 如果fun返回了true，那么就退出显式等待
        WebDriverWait(self._driver, 10).until(fun)
