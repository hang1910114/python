from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get("https://hmshop-test.itheima.net/Admin/Admin/login")
driver.find_element(By.CSS_SELECTOR,"div.formText:nth-child(1) > input:nth-child(2)").send_keys("admin")
driver.find_element(By.CSS_SELECTOR,"div.formText:nth-child(2) > input:nth-child(2)").send_keys("HM_2023_test")
driver.find_element(By.CSS_SELECTOR,"#vertify").send_keys("8888")
driver.find_element(By.CSS_SELECTOR,".sub").click()
# driver.find_element(By.CSS_SELECTOR,".forget_pwd").click()
sleep(5)
driver.quit()
