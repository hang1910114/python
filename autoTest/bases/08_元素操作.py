from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

# "msedgedriver.exe"
service=Service("../../day03/msedgedriver.exe")
#启动浏览器
driver = webdriver.Edge(service=service)

driver.get("file:///F:/360MoveData/Users/Documents/WeChat%20Files/wxid_n44hcg9mrsqc22/FileStorage/File/2024-07/%E6%B3%A8%E5%86%8CB.html")
#ZCA
"""
元素操作
    1、点击元素 .click
    2、获取文本 .text
    3、获取属性 元素.get_attribute("属性名")
"""
username=driver.find_element(By.CSS_SELECTOR,"#userB")
print("用户名文本框大小：",username.size)
print("用户名文本框是否启用：",username.is_enabled())
sleep(2)


