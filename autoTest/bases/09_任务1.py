from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.maximize_window()
# 打开首页
driver.get("https://hmshop-test.itheima.net/")

driver.implicitly_wait(5)
# 登录操作
# 进入登录页面
driver.find_element(By.LINK_TEXT,"登录").click()
# 填写
driver.find_element(By.CSS_SELECTOR,"#username").send_keys("15700001111")
driver.find_element(By.CSS_SELECTOR,"#password").send_keys("123456")
driver.find_element(By.CSS_SELECTOR,"#verify_code").send_keys("8888")
driver.find_element(By.CSS_SELECTOR,".login_bnt").click()

#登录断言
username=driver.find_element(By.CSS_SELECTOR,".userinfo").text
assert  "15700001111" in username ,"用户名错误"

# 4、点击logo回到首页
driver.find_element(By.CSS_SELECTOR,".ecsc-logo").click()
# 5、搜索商品gkd001
#输入
driver.find_element(By.CSS_SELECTOR,"#q").send_keys("gkd001")
#点击
driver.find_element(By.CSS_SELECTOR,".ecsc-search-button").click()
# 6、添加购物车
driver.find_element(By.LINK_TEXT,"加入购物车").click()

# 切换iframe 获取添加购物车结果
frame1=driver.find_element(By.CSS_SELECTOR,"#layui-layer-iframe1")
driver.switch_to.frame(frame1)
#断言
result=driver.find_element(By.CSS_SELECTOR,".conect-title > span:nth-child(1)").text
print("result:",result)
assert "添加成功" in result
driver.switch_to.default_content()
#关闭窗口
driver.find_element(By.CSS_SELECTOR,".layui-layer-ico").click()
sleep(3)
# 7、点击购物车
driver.find_element(By.CSS_SELECTOR,".c-n > span:nth-child(2)").click()
sleep(3)
# 8、点击去结算
# frame1=driver.find_element(By.CSS_SELECTOR,"#layui-layer-iframe1")
# driver.switch_to.frame(frame1)
driver.find_element(By.LINK_TEXT,"去结算").click()
# driver.switch_to.default_content()
sleep(3)
# # 添加地址
# driver.find_element(By.CSS_SELECTOR,"div.ui-switchable-panel:nth-child(2) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)").send_keys("hhh")
# driver.find_element(By.CSS_SELECTOR,"div.ui-switchable-panel:nth-child(2) > div:nth-child(2) > div:nth-child(2) > input:nth-child(1)").send_keys("15700001111")
# driver.find_element(By.CSS_SELECTOR,"#province > option:nth-child(2)").click()
# driver.find_element(By.CSS_SELECTOR,"#city > option:nth-child(2)").click()
# driver.find_element(By.CSS_SELECTOR,"#district > option:nth-child(2)").click()
# driver.find_element(By.CSS_SELECTOR,"#twon > option:nth-child(4)").click()
# driver.find_element(By.CSS_SELECTOR,"div.invoice_title:nth-child(4) > div:nth-child(3) > input:nth-child(1)").send_keys("北京某小院")
# driver.find_element(By.CSS_SELECTOR,"div.invoice_title:nth-child(5) > div:nth-child(2) > input:nth-child(1)").send_keys("541000")
# driver.find_element(By.LINK_TEXT,"保存").click()

# 提交订单
driver.find_element(By.CSS_SELECTOR,"#submit_order").click()
sleep(3)
#断言提交成功

book_text=driver.find_element(By.CSS_SELECTOR,".erhuh > h3:nth-child(2)").text
assert "提交成功" in book_text
print("订单状态：",book_text)
sleep(3)
driver.quit()