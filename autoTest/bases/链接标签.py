from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

driver.get("file:///F:/360MoveData/Users/Documents/WeChat%20Files/wxid_n44hcg9mrsqc22/FileStorage/File/2024-07/web%E7%B4%A0%E6%9D%90/web%E7%B4%A0%E6%9D%90cai/%E6%B3%A8%E5%86%8CA.html")

"""
LINK_TEXT：需要全部文本
PARTIAL_LINK_TEXT:支持模糊匹配
"""
# driver.find_element(By.LINK_TEXT,"访问 新浪 网站").click()

driver.find_element(By.PARTIAL_LINK_TEXT,"访问").click()
sleep(3)


