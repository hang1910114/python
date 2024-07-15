
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

"""
方法级别：每个test字母开头的方法，执行之前执行setup_method,执行结束执行teardown_method
    初始化：setup_method
    结束：teardown_method
类级别：
    初始化：setup_class
    结束：teardown_class
"""
class Test01:
    def setup_class(self):
        print("\nsetup_class被执行")
    def teardown_method(self):
        print("\nteardown_mothod1被执行")
    def test_Login(self):
        print("\ntest_Login被执行")

