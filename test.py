import time

from selenium import webdriver

driver = webdriver.Chrome()
# driver.implicitly_wait(10)
driver.maximize_window()
# driver.get("http://www.baidu.com")
# driver.find_element_by_id("kw").send_keys("自动化测试")
# driver.find_element_by_id("su").click()
# texts = driver.find_elements_by_xpath('//div/h3/a')

# 遍历搜索结果的每条标题
# for i in texts:
#     print(i.text)
driver.get("https://mail.163.com/")
time.sleep(3)


#密码登录
driver.find_element_by_id('switchAccountLogin').click()
# #遇到元素定位不到，采用绝对路径
# #iframe id动态变化，元素定位id不适用
frame = driver.find_element_by_xpath("//iframe[contains(@id, 'x-URS-iframe')]")
driver.switch_to.frame(frame)
# time.sleep(3)

#输入用户名、密码登录
driver.find_element_by_name('email').send_keys('18810848342')
driver.find_element_by_name('password').send_keys('135460146zy')
time.sleep(3)
driver.find_element_by_id('dologin').click()
driver.close()

