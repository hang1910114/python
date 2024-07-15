from time import sleep

from selenium import webdriver
from selenium.webdriver.edge.service import Service

from autoTest.test01.admin_login import AdminLogin
from autoTest.test01.coustomer_login import Customer
from autoTest.test01.customerRegister import CustomerRegister
from autoTest.tools.switch_windows import SwitchWindow

from selenium.webdriver.common.by import By


class Test:

    number = "15711112136"
    password = "abcd1234"
    admin_number = "admin"
    admin_passwd = "HM_2023_test"
    login_Code = "8888"
    code = "666666"
    id = "130104198909285214"
    def setup_class(self):

        print("setup_method执行成功")
    def setup_method(self):
        self.service = Service("msedgedriver.exe")
        self.driver = webdriver.Edge(service=self.service)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown_method(self):
        self.driver.quit()

    # 用户注册
    def test_customerRegister(self):
        customerRegister = CustomerRegister(self.driver)
        customerRegister.customerRegister(self.number, self.password, self.login_Code, self.code)

    def test_Login(self):
        driver = self.driver

        customer = Customer(driver)
        customer.test_Login(self.number, self.password)
        # 2、开通资金托管账户
        driver.find_element(By.CSS_SELECTOR, ".new-tips > a:nth-child(1)").click()
        driver.find_element(By.CSS_SELECTOR, ".ng-valid-realname").send_keys("小鬼头呀")
        driver.find_element(By.CSS_SELECTOR, ".ng-valid-card_id").send_keys(self.id)
        # sleep(2)
        driver.find_element(By.CSS_SELECTOR, ".btn").click()
        # 点击立刻开通
        # sleep(2)
        driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div/form/input").click()
        # driver.find_element(By.LINK_TEXT,"请点击，进入第三方完成操作").click()
        sleep(2)
        # 断言资金托管账户开通
        # 切换句柄
        handle = driver.window_handles
        print("\nhandle:", handle)
        print("driver.current_window_handle",driver.current_window_handle)
        driver.switch_to.window(handle[1])

        UserRegister = driver.find_element(By.XPATH, "/html/body").text
        print("\nUserRegister:", UserRegister)
        assert "UserRegister OK" in UserRegister, "资金托管账户开通失败"
        # sleep(2)
        driver.close()



    def test_login1(self):
        # 重新登录
        driver = self.driver

        customer = Customer(driver)
        customer.test_Login(self.number, self.password)
        # 切换账户类型
        sleep(2)
        driver.find_element(By.CSS_SELECTOR, ".change-role > a:nth-child(2)").click()
        # sleep(3)
        # 3、提交额度申请
        driver.find_element(By.LINK_TEXT, "申请额度").click()
        sleep(2)
        driver.find_element(By.CSS_SELECTOR, "#amount_account").send_keys("1000")
        driver.find_element(By.CSS_SELECTOR, ".lg-area").send_keys("买车呀")
        driver.find_element(By.CSS_SELECTOR, "#verifycode").send_keys("8888")
        sleep(2)
        driver.find_element(By.CSS_SELECTOR, ".btn-submit").click()
        sleep(2)
        # 添加提交审核成功断言
        applicate = driver.find_element(By.CSS_SELECTOR, "#amount_list > tr:nth-child(1) > td:nth-child(6)").text
        print("\n提交审核状态：",applicate)
        assert "待审核" in applicate, "提交审核失败"

    # 4、额度审批

    def test_login_admin(self):
        print("\ntest_login_admin执行成功")
        driver = self.driver

        adminLogin = AdminLogin(driver)
        adminLogin.admin_Login(self.admin_number, self.admin_passwd, self.login_Code)

        driver.find_element(By.LINK_TEXT,"借款管理").click()
        sleep(2)
        # 额度管理
        driver.find_element(By.CSS_SELECTOR, ".nav-list > li:nth-child(5) > a:nth-child(1)").click()

        # 审核列表
        driver.find_element(By.CSS_SELECTOR, ".open > ul:nth-child(2) > li:nth-child(2) > a:nth-child(1)").click()
        sleep(3)
        # 切换窗口到iframe模块
        print("开始调用")
        switch01 = SwitchWindow(driver, "#iframe_box")
        switch01.switchWindow()

        # 根据手机号搜索审核单
        driver.find_element(By.CSS_SELECTOR, "input.ng-pristine:nth-child(2)").send_keys(self.number)
        driver.find_element(By.CSS_SELECTOR, "select.ng-pristine > option:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, ".srcbtn").click()
        sleep(2)
        # 选中
        driver.find_element(By.CSS_SELECTOR, "tr.ng-scope").click()
        # 点击审核
        driver.find_element(By.CSS_SELECTOR, ".ui_dygrid_tool > li:nth-child(1) > a:nth-child(1)").click()
        sleep(3)
        # 切换到审核填写iframe
        switch02 = SwitchWindow(driver, "#xubox_iframe1")
        switch02.switchWindow()
        #
        driver.find_element(By.CSS_SELECTOR, "label.ng-scope:nth-child(1) > input:nth-child(1)").click()
        driver.find_element(By.CSS_SELECTOR, "textarea.ng-pristine").send_keys("审核通过")
        driver.find_element(By.CSS_SELECTOR, ".mright-5").send_keys(self.login_Code)
        # sleep(2)
        driver.find_element(By.CSS_SELECTOR, "input.dybtn:nth-child(1)").click()
        # sleep(3)

        # 添加审核通过断言
    def test_login2(self):
        # 重新登录
        driver = self.driver

        customerlogin = Customer(driver)
        customerlogin.test_Login(self.number,self.password)
        # 切换账户类型
        driver.find_element(By.CSS_SELECTOR,".change-role > a:nth-child(2)").click()
        sleep(3)
        # 3、提交额度申请
        driver.find_element(By.LINK_TEXT,"申请额度").click()
        sleep(2)
        text_application = driver.find_element(By.CSS_SELECTOR,"td.ng-scope").text
        assert "审核通过" in text_application, "审核失败"
        print("\n审核状态：", text_application)

    # 5、提交借款单
    def test_submit(self):
        # 重新登录
        driver = self.driver
        customer = Customer(driver)
        customer.test_Login(self.number, self.password)
        # 点击个人借款
        driver.find_element(By.CSS_SELECTOR, "li.ui-nav-item:nth-child(3) > a:nth-child(1)").click()
        sleep(3)
        # 选择个人借款
        driver.find_element(By.CSS_SELECTOR,"li.ng-scope:nth-child(1) > dl:nth-child(3) > dd:nth-child(5) > a:nth-child(2)").click()
        sleep(3)
        # 填写借款信息
        driver.find_element(By.CSS_SELECTOR, ".w200").send_keys("用于买车")
        driver.find_element(By.CSS_SELECTOR, ".ng-valid-use > option:nth-child(3)").click()
        driver.find_element(By.CSS_SELECTOR, ".ng-valid-amount").send_keys("500")
        driver.find_element(By.CSS_SELECTOR, ".ng-valid-apr").send_keys("3.0")
        # 还款方式
        driver.find_element(By.CSS_SELECTOR, "div.u-item:nth-child(10) > select:nth-child(2) > option:nth-child(2)").click()
        # 筹标期限
        driver.find_element(By.CSS_SELECTOR, ".ng-valid-validate > option:nth-child(4)").click()
        # 最低投资金额100
        driver.find_element(By.CSS_SELECTOR, "#tender_amount_min > option:nth-child(3)").click()
        # 最高投资金额1000
        driver.find_element(By.CSS_SELECTOR, "#tender_amount_max > option:nth-child(4)").click()
        # 借款投资密码
        driver.find_element(By.CSS_SELECTOR, "input.ss-input:nth-child(3)").send_keys("abcd1234")
        # 借款描述
        driver.find_element(By.CSS_SELECTOR, "#borrow_contents").send_keys("我需要借款呀")
        # 验证码
        driver.find_element(By.CSS_SELECTOR, ".w80").send_keys("8888")
        # 提交
        # sleep(3)
        driver.find_element(By.CSS_SELECTOR, "#borrowForm").click()
        sleep(3)
        # 提交借款单成功断言
        # 切换账户到借款账户
        driver.find_element(By.CSS_SELECTOR, ".change-role > a:nth-child(2)").click()
        # sleep(3)
        #
        driver.find_element(By.LINK_TEXT, "我的借款").click()
        sleep(3)
        applicate_money = driver.find_element(By.CSS_SELECTOR,"span.ng-scope:nth-child(1)").text
        print("\n借款单状态：",applicate_money)
        assert "发标待审" in applicate_money, "提交借款单失败"
    # 审核借款单
    def test_loan(self):
        # 登录后端
        admin = AdminLogin(self.driver)
        admin.admin_Login(self.admin_number, self.admin_passwd, self.login_Code)
        # 审核借款单
        admin.examineLoan(self.number)
