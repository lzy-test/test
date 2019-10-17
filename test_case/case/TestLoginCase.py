from test_case.models import myunit
from test_case.models.function import Function

from test_case.page import loginPage
import time
import unittest
from  HTMLTestRunner import HTMLTestRunner

class LoginTest(myunit.MyTest):
    """ 登录测试 """

    def test_login1(self):
        """ 用户名为空、密码为空 """
        loginPage.Login(self.driver).user_login("", "")
        error = loginPage.Login(self.driver).fail_text()
        self.assertEqual(error, "请您输入手机/邮箱/用户名")
        Function.insert_img(self.driver, "Login_name_pass_empty.png")

    def test_login2(self):
        """ 用户名为空、密码错误 """
        loginPage.Login(self.driver).user_login("", "123")
        self.assertEqual(loginPage.Login(self.driver).fail_text(), "请您输入手机/邮箱/用户名")
        Function.insert_img(self.driver, "Login_name_empty.png")

if __name__ == '__main__':
    test_dir = 'E:\\AutoTestProject\\test_case'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    test_report_dir = 'E:\\AutoTestProject\\report'
    filename = test_report_dir + '\\' + now + 'result.html'
    fv = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fv, title='登录功能测试报告', description='用例执行情况')
    runner.run(discover)
    fv.close()