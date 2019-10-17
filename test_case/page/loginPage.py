from selenium.webdriver.common.by import By
from .base import Page


'''
用户登录页面
'''


class Login(Page):

    loginPass_loc = (By.XPATH, "//*[@id='TANGRAM__PSP_4__footerULoginBtn']")        # 密码登录按钮
    username_input_loc = (By.XPATH, "//*[@id='TANGRAM__PSP_4__userName']")         # 用户名输入框
    password_input_loc = (By.XPATH, "//*[@id='TANGRAM__PSP_4__password']")         # 密码输入框
    button_loc = (By.XPATH, "//*[@id='TANGRAM__PSP_4__submit']")                   # 登录按钮

    fail_loc = (By.XPATH, "//*[@id='TANGRAM__PSP_4__error']")                       # 登录错误提示位置

    def pass_click(self):
        """登录按钮点击"""
        self.find_element(*self.loginPass_loc).click()


    def username_input(self, username):
        """登录用户名文本输入框"""
        self.find_element(*self.username_input_loc).send_keys(username)

    def password_input(self, password):
        """登录密码文本输入框"""
        self.find_element(*self.password_input_loc).send_keys(password)

    def button_click(self):
        """登录按钮点击"""
        self.find_element(*self.button_loc).click()

    def fail_text(self):
        """登录失败-文本获取"""
        return self.find_element(*self.fail_loc).text


    def user_login(self, username, password):
        """定义统一登录登录入口，打开网页→ 点击密码登录→ 输入用户名→ 输入密码→ 点击登陆"""
        self.open()
        self.pass_click()
        self.username_input(username)
        self.password_input(password)
        self.button_click()
