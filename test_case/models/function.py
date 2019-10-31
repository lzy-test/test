
import os
import time

from selenium import webdriver
# 截图函数
class Function:
    def insert_img(driver, file_name):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        base_dir = str(base_dir)
        print(base_dir)
        base_dir = base_dir.replace('\\', '/')
        print(base_dir)
        base = base_dir.split('test_case')[0]
        now = time.strftime("%m-%d %H-%M")
        print(base)
        file_path = base + "/report/image/" + now + "_" + file_name
        print(file_path)
        driver.get_screenshot_as_file(file_path)

#测试截图
if __name__ == '__main__':
        driver = webdriver.Chrome()
        driver.get("https://pan.baidu.com/")
        Function.insert_img(driver, 'mail.png')
        driver.quit()


