import smtplib,os,email,time
from email.header import Header
from email.mime.multipart import MIMEMultipart  #带附件
from email.mime.text import MIMEText
import unittest
import sys
sys.path.append('../')
print(sys.path)
from  HTMLTestRunner import HTMLTestRunner

# sys.path.append('E:\\AutoTestProject')
#
# print(sys.path)


def all_case():
    # 待执行用例的目录
    #case_dir = "C:\\Users\\DELL\\PycharmProjects\\honggetest\\case"
    case_dir = os.path.join(os.getcwd(), "case")
    testcase = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_dir,
                                                   pattern="test*.py",
                                                   top_level_dir=None)
    #discover方法筛选出用例，循环添加到测试套件中
    # for test_suit in discover:
    #     for test_case in test_suit:
    #         #添加用力到testcase
    #         testcase.addTests(test_case)
    # print(testcase)
    testcase.addTests(discover)  # 直接加载 discover    可以兼容python2和3
    print(testcase)
    return testcase
# ==============定义发送邮件==========
def send_mail(file_new):
    #-----------1.跟发件相关的参数------
    smtpserver = 'smtp.qq.com'                #发件服务器
    username = '183180767@qq.com'         #发件箱用户名
    password = 'ppxxlfwlpfmdcaff'        #发件箱密码
    sender = '183180767@qq.com'    #发件人邮箱
    receiver = '2139134870@qq.com' #收件人邮箱
    # ----------2.编辑邮件的内容------
    #读文件
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    # 邮件正文是MIMEText
    body = MIMEText(mail_body, 'html', 'utf-8')
    # 邮件对象
    msg = MIMEMultipart()
    msg['Subject'] = Header("自动化测试报告", 'utf-8').encode()#主题
    msg['From'] = sender              #发件人
    msg['To'] = receiver          #收件人
    # msg['To'] = ';'.join(receiver)
    msg['date'] = time.strftime("%a,%d %b %Y %H:%M:%S %z")
    msg.attach(body)
    # 附件
    att = MIMEText(mail_body, "base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment; filename="test_report.html"'
    msg.attach(att)
    # ----------3.发送邮件------
    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)  # 连服务器
        smtp.login(username, password)
    except:
        smtp = smtplib.SMTP_SSL(smtpserver, 465)
        smtp.login(username, password)  # 登录
    smtp.sendmail(sender, receiver, msg.as_string())  # 发送
    smtp.quit()
    # #发送邮件
    # smtp = smtplib.SMTP()
    # smtp.connect('smtp.mxhichina.com')  # 邮箱服务器
    # smtp.login(username, password)  # 登录邮箱
    # smtp.sendmail(sender, receiver, msg.as_string())  # 发送者和接收者
    # smtp.quit()
    print("邮件已发出！注意查收。")
# ======查找测试目录，找到最新生成的测试报告文件======
def new_report(test_report):
    lists = os.listdir(test_report)  # 列出目录的下所有文件和文件夹保存到lists
    lists.sort(key=lambda fn: os.path.getmtime(test_report + "\\" + fn))  # 按时间排序
    file_new = os.path.join(test_report, lists[-1])  # 获取最新的文件保存到file_new
    print(file_new)
    return file_new
if __name__ == "__main__":
    # 返回实例
    runner = unittest.TextTestRunner()
    # 获取当前时间，这样便于下面的使用。
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    #保存生成报告的路径
    report_path = "E:\\AutoTestProject\\report\\"+now+"_result.html"
    fp = open(report_path,'wb')
    runner = HTMLTestRunner(stream=fp,
                                           title=u"登录自动化测试用例",
                                           description=u"用例执行情况",
                                           verbosity = 2
                                           )
    # run 所有用例
    runner.run(all_case())
    #关闭文件，记住用open()打开文件后一定要记得关闭它，否则会占用系统的可打开文件句柄数。
    fp.close()
    #测试报告文件夹
    test_path = "E:\\AutoTestProject\\report"
    new_report = new_report(test_path)
    send_mail(new_report)  # 发送测试报告