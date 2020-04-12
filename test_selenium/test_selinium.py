"""

author: whiteP

modified time: 2020/4/12 11:18

"""

from selenium import webdriver


def test_selenium():
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com/")
