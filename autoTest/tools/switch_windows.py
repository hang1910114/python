
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
"""
切换到iframe里
"""
class SwitchWindow:
    def __init__(self,driver,iframeId="000"):
        self.iframeId=iframeId
        self.driver = driver
    def switchWindow(self):
        driver = self.driver
        frameB = driver.find_element(By.CSS_SELECTOR, self.iframeId)
        driver.switch_to.frame(frameB)


