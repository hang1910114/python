

from time import sleep

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

from autoTest.test01.coustomer_login import Coustomer


# 2、开通资金托管账户
class OpenAccount:
    def __init__(self):
        self.service = Service("msedgedriver.exe")
        self.driver = webdriver.Edge(service=self.service)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
    def open_Account(self):
        driver = self.driver
        driver.find_element(By.CSS_SELECTOR, ".new-tips > a:nth-child(1)").click()
        driver.find_element(By.CSS_SELECTOR, ".ng-valid-realname").send_keys("小鬼头呀")
        driver.find_element(By.CSS_SELECTOR, ".ng-valid-card_id").send_keys("450202199106285013")
        sleep(2)
        driver.find_element(By.CSS_SELECTOR, ".btn").click()
        # 点击立刻开通
        sleep(2)
        driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div/form/input").click()

        sleep(3)
        # 断言资金托管账户开通
        UserRegister = driver.find_element(By.CSS_SELECTOR, "body").text
        print("\nUserRegister:", UserRegister)
        assert "操作已完成" in UserRegister, "资金托管账户开通失败"
        sleep(3)
        driver.close()
customer = Coustomer()
customer.test_Login()
openAccount = OpenAccount()
openAccount.open_Account()
