from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
# "msedgedriver.exe"
driver = webdriver.Edge()

driver.get("file:///F:/360MoveData/Users/Documents/WeChat%20Files/wxid_n44hcg9mrsqc22/FileStorage/File/2024-07/%E6%B3%A8%E5%86%8CB.html")

"""
弹窗
"""

driver.find_element(By.CSS_SELECTOR,"#alertB").click()
sleep(1)
alert=driver.switch_to.alert
alert.accept()
driver.find_element(By.CSS_SELECTOR,"#userB").send_keys("1231456777")
sleep(3)


#alertB
