from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

# "msedgedriver.exe"
service=Service("../../day03/msedgedriver.exe")
driver = webdriver.Edge(service=service)

driver.get("file:///F:/360MoveData/Users/Documents/WeChat%20Files/wxid_n44hcg9mrsqc22/FileStorage/File/2024-07/%E6%B3%A8%E5%86%8CB.html")
#ZCA
"""
浏览器操作

"""
#获取当前页面title
print("当前页面title",driver.title)

#获取当前页面url
print("当前页面url:",driver.current_url)
sleep(3)
driver.maximize_window()
#刷新页面，页面内容清空
driver.find_element(By.CSS_SELECTOR,"#userB").send_keys("15700001111")
sleep(2)
driver.refresh()
sleep(2)


