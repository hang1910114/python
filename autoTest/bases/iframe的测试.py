from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

#主页面
driver = webdriver.Edge()
driver.get("file:///F:/360MoveData/Users/Documents/WeChat%20Files/wxid_n44hcg9mrsqc22/FileStorage/File/2024-07/web%E7%B4%A0%E6%9D%90/web%E7%B4%A0%E6%9D%90cai/%E6%B3%A8%E5%86%8C%E5%AE%9E%E4%BE%8B.html")
driver.find_element(By.CSS_SELECTOR,"#user").send_keys("lhc")
driver.find_element(By.CSS_SELECTOR,"#password").send_keys("123456")
driver.find_element(By.CSS_SELECTOR,"#tel").send_keys("15766600000")
driver.find_element(By.CSS_SELECTOR,"#email").send_keys("lhc@163.com")
sleep(3)

"""
切换iframe：driver.switch_to.frame(iframe页面元素)
回到主页面：driver.switch_to.default_content()
"""
frameA = driver.find_element(By.CSS_SELECTOR,"#idframe1")
driver.switch_to.frame(frameA)

# 页面A
driver.find_element(By.CSS_SELECTOR,"#userA").send_keys("lhc")
driver.find_element(By.CSS_SELECTOR,"#passwordA").send_keys("123456")
driver.find_element(By.CSS_SELECTOR,"#telA").send_keys("15766600000")
driver.find_element(By.CSS_SELECTOR,"#emailA").send_keys("lhc@163.com")
sleep(3)
driver.switch_to.default_content()

frameB = driver.find_element(By.CSS_SELECTOR,"body > s:nth-child(2) > iframe:nth-child(8)")
driver.switch_to.frame(frameB)

# 页面B
driver.find_element(By.CSS_SELECTOR,"#userB").send_keys("lhc")
driver.find_element(By.CSS_SELECTOR,"#passwordB").send_keys("123456")
driver.find_element(By.CSS_SELECTOR,"#telB").send_keys("15766600000")
driver.find_element(By.CSS_SELECTOR,"#emailB").send_keys("lhc@163.com")
sleep(3)
driver.switch_to.default_content()