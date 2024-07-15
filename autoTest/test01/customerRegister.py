
from time import sleep

from selenium import webdriver
from selenium.webdriver.edge.service import Service

from autoTest.test01.admin_login import AdminLogin
from autoTest.test01.coustomer_login import Customer
from autoTest.tools.switch_windows import SwitchWindow

from selenium.webdriver.common.by import By

class CustomerRegister:
    def __init__(self,driver):
        self.driver = driver

    def customerRegister(self, username, password, login_Code, code):
        driver = self.driver
        driver.get("http://121.43.169.97:8081/common/member/reg")
        driver.find_element(By.CSS_SELECTOR, "#phone").send_keys(username)
        driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
        driver.find_element(By.CSS_SELECTOR, "#verifycode").send_keys(login_Code)
        driver.find_element(By.CSS_SELECTOR,"#get_phone_code").click()
        sleep(3)
        driver.find_element(By.CSS_SELECTOR, "#phone_code").send_keys(code)
        driver.find_element(By.CSS_SELECTOR, ".lg-btn").click()
        # sleep(3)
#
# server = Service("msedgedriver.exe")
# driver = webdriver.Edge(service = server)
# customerRegister = CustomerRegister(driver)
# number = "15711112250"
# password = "abcd1234"
# login_Code = "8888"
# code = "666666"
# customerRegister.customerRegister(number, password, login_Code, code)
