"""

author: whiteP

modified time: {DATE} {TIME}

"""
import pytest

from python.calc import Calc


# 整个文件只执行一次
def setup_module():
    print("setup_module")


class TestCalc:
    # 类开始执行
    @classmethod
    def setup_class(cls):
        print("setup_class")

    # 每个函数开始执行
    def setup_method(self):
        print("setup_method")

    def setup(self):
        print("setup")
        self.calc = Calc()

    # 每个函数结束执行
    def teardown(self):
        print("teardown")

    def teardown_method(self):
        print("teardown_method")

    @pytest.mark.run(order=-1)
    def test_add(self):
        assert self.calc.add(1, 2) == 3

    @pytest.mark.run(order=2)
    def test_div(self):
        assert self.calc.div(1, 2) == 0.5

    def test_params(self):
        data = (1, 2)
        self.calc.add2(data)
        self.calc.add(*data)

    # 作业 除法
    def test_dev1(self):
        assert self.calc.div(4, 2) == 2

    def test_dev2(self):
        assert self.calc.div(1, 3) == 0.5

    def test_dev3(self):
        assert self.calc.div(0, 1) == 0

    def test_dev4(self):
        assert self.calc.div(1, 0) == 0.5

    def test_dev5(self):
        assert self.calc.div(0, 0) == 0

    def test_dev6(self):
        assert self.calc.div(-4, -2) == 2

    def test_dev7(self):
        assert self.calc.div(1, -2) == -0.5

    def test_dev8(self):
        assert self.calc.div(-4, 2) == -2

    def test_dev9(self):
        assert self.calc.div(-1, 0) == -0.5

    def test_dev10(self):
        assert self.calc.div(0, -2) == 0

    def test_add1(self):
        assert self.calc.add(1, 2) == 3

    def test_add2(self):
        assert self.calc.add(-1, 2) == 1

    def test_add3(self):
        assert self.calc.add(1, -2) == -1

    def test_add4(self):
        assert self.calc.add(-1, -2) == -0.3

    # 参数化
    @pytest.mark.demo
    @pytest.mark.parametrize("a, b", [
        (1, 2), (2, 3), (3, 4)
    ])
    def test_params(self, a, b):
        print("params")
        data = (a, b)
        self.calc.add2(data)
        self.calc.add(*data)
