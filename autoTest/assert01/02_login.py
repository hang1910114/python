from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

service=Service("../../day03/msedgedriver.exe")
driver = webdriver.Edge(service=service)
driver.get("https://hmshop-test.itheima.net/Home/user/login.html")
driver.find_element(By.CSS_SELECTOR,"#username").send_keys("15700001111")
driver.find_element(By.CSS_SELECTOR,"#password").send_keys("123456")
driver.find_element(By.CSS_SELECTOR,"#verify_code").send_keys("8888")
driver.find_element(By.CSS_SELECTOR,".login_bnt").click()
sleep(3)
#password