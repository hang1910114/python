from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

service=Service("msedgedriver.exe")
driver = webdriver.Edge(service=service)
driver.get("http://121.43.169.97:8000/muser/publicRequests")
username=driver.find_element(By.CSS_SELECTOR,"body").text
print("usernaame=",username)
sleep(3)