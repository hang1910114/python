
from time import sleep

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

class Customer:
    def __init__(self,driver):
        self.driver = driver
        # self.driver.maximize_window()
        self.driver.implicitly_wait(5)
    def test_Login(self,number,password):
        driver = self.driver
        driver.get("http://121.43.169.97:8081/")
        # 1、登录
        driver.find_element(By.LINK_TEXT ,"登录").click()
        driver.find_element(By.CSS_SELECTOR, "#keywords").send_keys(number)
        driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
        driver.find_element(By.CSS_SELECTOR, "#login-btn").click()
        # 添加登录断言
        sleep(3)
        username = driver.find_element(By.XPATH, "//a").text
        print("\n用户名称：", username)
        assert number in username, "用户名错误"
# customer = Customer()
# customer.test_Login()