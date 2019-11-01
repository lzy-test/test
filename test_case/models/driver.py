
from selenium import webdriver

# 启动浏览器驱动
def browser():
    driver = webdriver.Chrome(r"C:\Users\Administrator.W8-201610091957\AppData\Local\Google\Chrome\Application\chromedriver.exe")
    return driver

if  __name__ == '__main__':
    dr = browser()
    dr.get("https://pan.baidu.com/")
    dr.quit()
