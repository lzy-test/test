

class Page(object):

    """  页面基础类，用于所有页面的继承 """

    # url = "http://192.168.20.12:56366/rdms/login.jsp"
    url = "https://pan.baidu.com/"

    def __init__(self, driver, url=url):
        self.url = url
        self.driver = driver
        self.timeout = 30

    def open(self):
        self.driver.get(self.url)

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

