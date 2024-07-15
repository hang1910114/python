from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service


# 3、提交额度申请
class SubApplication:
    def __init__(self):
        self.service = Service("msedgedriver.exe")
        self.driver = webdriver.Edge(service=self.service)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
    def subApplication(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT,"申请额度").click()
        sleep(5)
        driver.find_element(By.CSS_SELECTOR,"#amount_account").send_keys("1000")
        driver.find_element(By.CSS_SELECTOR,".lg-area").send_keys("买车呀")
        driver.find_element(By.CSS_SELECTOR,"#verifycode").send_keys("8888")
        sleep(5)
        driver.find_element(By.CSS_SELECTOR, ".btn-submit").click()
        sleep(3)
        # 添加提交审核成功断言
        applicate = driver.find_element(By.CSS_SELECTOR,"#amount_list > tr:nth-child(1) > td:nth-child(6)").text
        print("\n提交审核状态：",applicate)
        assert "待审核" in applicate, "提交审核失败"
subApplication = SubApplication()
subApplication.subApplication()

