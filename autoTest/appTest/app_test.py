from time import sleep

from selenium import webdriver
from selenium.webdriver.edge.service import Service

from autoTest.test01.admin_login import AdminLogin
from autoTest.test01.coustomer_login import Customer
from autoTest.test01.customerRegister import CustomerRegister
from autoTest.tools.switch_windows import SwitchWindow

from selenium.webdriver.common.by import By

class Test2:
    def setup_class(self):
        self.service = Service("msedgedriver.exe")
        self.driver = webdriver.Edge(service=self.service)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown_method(self):
        self.driver.quit()
    def test_login(self):
        driver = self.driver
        driver.get("http://localhost:5173/#/")
        driver.find_element(By.CSS_SELECTOR, "#username > div > input").send_keys("哈哈哈")
        driver.find_element(By.CSS_SELECTOR, "#number > div > input").send_keys("15700001111")
        driver.find_element(By.CSS_SELECTOR, "#cryptogram > div > input").send_keys("123456")
        driver.find_element(By.CSS_SELECTOR, "#app > uni-app > uni-page > uni-page-wrapper > uni-page-body > uni-view > uni-button").click()
        sleep(3)