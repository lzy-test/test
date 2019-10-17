import smtplib
from email.header import Header
from email.mime.text import MIMEText


def send_email(subject, text):
 smtpserver = 'smtp.qq.com'
 username = '183180767@qq.com'
 password = 'ppxxlfwlpfmdcaff'  #授权码
 sender = '183180767@qq.com'  #发送者邮箱
 receiver = '2139134870@qq.com ' #接收者邮箱
 subject="loginTest"
 text = "11"
 msg = MIMEText(text,'plain', 'utf-8') #构造MIMEText对象时，第一个参数是邮件正文，第二个参数是MIME的subtype，最后一定要用utf-8编码保证多语言兼容性。
 msg["Subject"] = Header(subject, "utf-8")
 msg["from"] = sender
 msg["to"] =  receiver
# 发送邮件

 smtp = smtplib.SMTP_SSL()  #实例化smtp()
 smtp.connect(smtpserver,465) #连接邮箱服务器、端口
 smtp.login(username, password)  #登录邮箱用户名、密码
 smtp.sendmail(sender, receiver,msg.as_string()) #邮件发送者、接收者 msg：发送消息：邮件内容。一般是msg.as_string():as_string()是将msg(MIMEText对象或者MIMEMultipart对象)变为str。
 smtp.quit()

