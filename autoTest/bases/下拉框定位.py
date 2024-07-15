
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

driver.get("file:///F:/360MoveData/Users/Documents/WeChat%20Files/wxid_n44hcg9mrsqc22/FileStorage/File/2024-07/web%E7%B4%A0%E6%9D%90/web%E7%B4%A0%E6%9D%90cai/%E6%B3%A8%E5%86%8CA.html")

"""
下拉框：css
"""
#暂停3秒点击上海
sleep(3)
driver.find_element(By.CSS_SELECTOR,"#selectA > option:nth-child(2)").click()

sleep(3)
