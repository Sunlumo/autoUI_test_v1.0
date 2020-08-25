from selenium import webdriver


class GetWebDriver(object):

    def __init__(self,browser_type):
        self.browser_type = browser_type

    # 打开浏览器
    def open_browser(self):
        if self.browser_type == 'Firefox':
            return webdriver.Firefox()
        elif self.browser_type == 'Chrome':
            return webdriver.Chrome()
        elif self.browser_type == 'IE':
            return webdriver.Ie()
        elif self.browser_type == '':
            return webdriver.Chrome()

    # 关闭浏览器
    def close_brower(self):
        self.open_browser().close()

