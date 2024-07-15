from time import sleep

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

from autoTest.tools.switch_windows import SwitchWindow


class AdminLogin:
    def __init__(self, driver):
        self.driver = driver
        # self.driver.maximize_window()
        self.driver.implicitly_wait(5)
    def admin_Login(self, number, password, login_Code):
        driver = self.driver
        driver.get("http://121.43.169.97:8082/")
        # 1、登录
        driver.find_element(By.CSS_SELECTOR, "#username").send_keys(number)
        driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
        driver.find_element(By.CSS_SELECTOR, "#valicode").send_keys(login_Code)
        driver.find_element(By.CSS_SELECTOR, ".login-button").click()

    # 审核借款单
    def examineLoan(self, number):
        # 切换到借款管理/初审标
        driver = self.driver
        # sleep(3)
        driver.find_element(By.LINK_TEXT, "借款管理").click()
        # sleep(3)
        driver.find_element(By.CSS_SELECTOR, ".nav-list > li:nth-child(2) > a:nth-child(1)").click()
        # sleep(3)
        driver.find_element(By.CSS_SELECTOR, ".open > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1)").click()
        # sleep(2)
        # 切换iframe
        iframe1 = SwitchWindow(driver, "#iframe_box")
        iframe1.switchWindow()
        # 搜索审核标
        sleep(2)
        driver.find_element(By.CSS_SELECTOR, ".form-horizontal > ul:nth-child(1) > li:nth-child(1) > div:nth-child(1) > input:nth-child(2)").send_keys(number)
        driver.find_element(By.CSS_SELECTOR, ".srcbtn_box").click()
        # 选中标
        driver.find_element(By.CSS_SELECTOR, "tr.ng-scope").click()
        sleep(2)
        # 点击审核
        driver.find_element(By.CSS_SELECTOR, ".ui_dygrid_tool > li:nth-child(2) > a:nth-child(1)").click()
        # 再次切换iframe #xubox_iframe1
        iframe1 = SwitchWindow(driver, "#xubox_iframe1")
        iframe1.switchWindow()
        sleep(2)
        # 选择通过
        driver.find_element(By.CSS_SELECTOR, "label.ng-scope:nth-child(1) > input:nth-child(1)").click()
        driver.find_element(By.CSS_SELECTOR, ".ng-isolate-scope").send_keys("买车标")
        driver.find_element(By.CSS_SELECTOR, "textarea.ng-pristine").send_keys("买车标审核备注")
        driver.find_element(By.CSS_SELECTOR, ".mright-5").send_keys("8888")
        # 点击保存
        sleep(2)
        driver.find_element(By.CSS_SELECTOR, "input.dybtn:nth-child(1)").click()


