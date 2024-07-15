
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
class Test02:
    def setup_class(self):

        print("setup_method执行成功")
    def setup_method(self):
        self.service = Service("msedgedriver.exe")
        self.driver = webdriver.Edge(service=self.service)

        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown_method(self):
        sleep(3)
        self.driver.quit()
    def test_Login(self):
        driver=self.driver
        driver.get("https://hmshop-test.itheima.net/Home/user/login.html")
        driver.find_element(By.CSS_SELECTOR, "#username").send_keys("15700001111")
        driver.find_element(By.CSS_SELECTOR, "#password").send_keys("123456")
        driver.find_element(By.CSS_SELECTOR, "#verify_code").send_keys("8888")
        driver.find_element(By.CSS_SELECTOR, ".login_bnt").click()
        username = driver.find_element(By.CSS_SELECTOR, ".userinfo").text

        assert "15700001111" in username, "用户名错误"
