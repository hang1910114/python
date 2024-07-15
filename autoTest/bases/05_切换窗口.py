from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

# "msedgedriver.exe"
service=Service("../../day03/msedgedriver.exe")
driver = webdriver.Edge(service=service)

driver.get("file:///F:/360MoveData/Users/Documents/WeChat%20Files/wxid_n44hcg9mrsqc22/FileStorage/File/2024-07/web%E7%B4%A0%E6%9D%90/web%E7%B4%A0%E6%9D%90cai/%E6%B3%A8%E5%86%8C%E5%AE%9E%E4%BE%8B.html")
#ZCA
"""
切换窗口
获取所有窗口句柄：driver.window_handles
获取当前窗口句柄：driver.current_window_handle
切换窗口：driver.switch_to.window(handel[1])
"""
#点击切换窗口链接
driver.find_element(By.CSS_SELECTOR,"#ZCA").click()
sleep(2)
#获取所有句柄
handles=driver.window_handles
print("所有句柄：")
for handle in handles:
    print(handle)

print("当前句柄："+driver.current_window_handle)
#切换句柄
driver.switch_to.window(handles[1])
print("当前句柄："+driver.current_window_handle)
driver.find_element(By.CSS_SELECTOR,"#userA").send_keys("1231456777")
#窗口最大化
driver.maximize_window()
sleep(3)


#alertB
