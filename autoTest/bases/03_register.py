from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get("https://hmshop-test.itheima.net/Home/User/reg.html")
driver.find_element(By.CSS_SELECTOR,"#username").send_keys("15700001111")
driver.find_element(By.CSS_SELECTOR,".imgcode").send_keys("8888")
driver.find_element(By.CSS_SELECTOR,"#password").send_keys("123456")
driver.find_element(By.CSS_SELECTOR,"#password2").send_keys("123456")
driver.find_element(By.CSS_SELECTOR,"div.line:nth-child(5) > div:nth-child(2) > input:nth-child(1)").send_keys("123456")

driver.find_element(By.CSS_SELECTOR,".regbtn").click()
sleep(5)
#password2
