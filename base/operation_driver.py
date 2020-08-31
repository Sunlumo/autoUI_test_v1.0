import logging
import conf.com_config
import utilities.time_util

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, ErrorInResponseException, NoSuchFrameException, \
    NoSuchWindowException, InvalidSwitchToTargetException, InvalidElementStateException, WebDriverException, \
    NoAlertPresentException, StaleElementReferenceException, TimeoutException


class WebTools(object):

    def __init__(self, driver, logger, timeout, case_id, num):
        self.driver = driver
        self.timeout = timeout
        self.logging = logger
        self.case_id = case_id
        self.num = num

    '''元素定位方法'''

    def get_element(self, key, value):
        try:
            self.logging.info("开始通过方法:{}，值:{}获取元素对象".format(key, value))
            if key == "js_script":
                element = 0

            elif key == "id":
                element = self.driver.find_element(by=By.ID, value=value)

            elif key == "ids":
                element = self.driver.find_elements(by=By.ID, value=value)

            elif key == "xpath":
                element = self.driver.find_elements(by=By.XPATH, value=value)

            elif key == "xpaths":
                element = self.driver.find_elements(by=By.XPATH, value=value)

            elif key == "link_text":
                element = self.driver.find_elements(by=By.LINK_TEXT, value=value)

            elif key == "link_texts":
                element = self.driver.find_elements(by=By.LINK_TEXT, value=value)

            elif key == "partial_link_text":
                element = self.driver.find_elements(by=By.PARTIAL_LINK_TEXT, value=value)

            elif key == "partial_link_texts":
                element = self.driver.find_elements(by=By.PARTIAL_LINK_TEXT, value=value)

            elif key == "name":
                element = self.driver.find_elements(by=By.NAME, value=value)

            elif key == "names":
                element = self.driver.find_elements(by=By.NAME, value=value)

            elif key == "tag_name":
                element = self.driver.find_elements(by=By.TAG_NAME, value=value)

            elif key == "tag_names":
                element = self.driver.find_elements(by=By.TAG_NAME, value=value)

            elif key == "class_name":
                element = self.driver.find_elements(by=By.CLASS_NAME, value=value)

            elif key == "class_names":
                element = self.driver.find_elements(by=By.CLASS_NAME, value=value)

            elif key == "css_selector":
                element = self.driver.find_elements(by=By.CSS_SELECTOR, value=value)

            elif key == "css_selectors":
                element = self.driver.find_elements(by=By.CSS_SELECTOR, value=value)

            else:
                self.logging.error("{}定位方式不存在！".format(key))
                self._get_windows_img()
                raise ValueError
            self.logging.info("获取元素对象成功")
            return element

        except NoSuchElementException as e:
            self._get_windows_img()
            self.logging.error("\"{}\"定位元素失败！详细信息：{}".format(value, e))
            raise NoSuchElementException

    '''窗口操作方法'''

    # 打开页面
    def get_web_page(self, url):
        try:
            self.logging.info("开始打开页面：{}".format(url))
            self.driver.get(url)
            self.logging.info("打开页面成功!")
        except ErrorInResponseException as e:
            self.logging.error("页面打开失败，请检查连接：{}！错误详情：{}".format(url, e))
            raise ErrorInResponseException

    # 跳转页面
    def jump_web_page(self, page):
        try:
            logging.info("开始打开页面：{}".format(page))
            self.driver.get(self.get_web_page(page))
            self.driver.maximize_window()
            self.logging.info("打开页面成功!")
        except ErrorInResponseException as e:
            self.logging.error("页面打开失败，请检查连接：{}！错误详情：{}".format(page, e))
            raise ErrorInResponseException

    # 这时切换到新窗口
    def current_handel(self):
        try:
            self.logging.info("开始执行切换新窗口操作")
            all_handles = self.driver.window_handles
            for handle in all_handles:
                self.driver.switch_to.window(handle)
                self.logging.info("切换新窗口操作成功")
        except NoSuchWindowException as e:
            self.logging.error("切换新窗口错误！错误详情：{}".format(e))
            raise NoSuchWindowException

    # 窗口最大化
    def max_windows(self):
        return self.driver.maximize_window()

    # 浏览器前进操作
    def forward(self):
        self.driver.forward()

    # 浏览器后退操作
    def back(self):
        self.driver.back()

    # 隐式等待
    def _wait(self, seconds):
        return self.driver.implicitly_wait(seconds)

    # 显性等待时间
    def _web_driver_wait(self, element_method):
        return WebDriverWait(self.driver, self.timeout).until(element_method)

    # 保存图片
    def _get_windows_img(self):
        file_path = conf.com_config.PICTURE_PATH
        screen_name = file_path + str(self.case_id) + "_" + str(
            self.num) + "_" + utilities.time_util.get_time() + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
        except NameError as e:
            self.logging.error("截图失败！".format(e))

    '''元素操作方法'''

    # 输入内容
    def input(self, key, value, input_value):
        try:
            self.logging.info("元素开始输入，方法：{}，值：{}，内容：{}".format(key, value, input_value))
            self.get_element(key, value).send_keys(input_value)
            self.logging.info("元素开始输入内容结束")
        except InvalidElementStateException as e:
            self._get_windows_img()
            self.logging.error("元素状态异常，不能进行操作！错误详情：{}".format(e))
            raise InvalidElementStateException

    # 鼠标点击
    def click(self, key, value):
        try:
            self.logging.info("元素执行点击操作，方法：{}，值：{}".format(key, value))
            self.get_element(key, value).click()
            self.logging.info("执行点击操作结束")
        except InvalidElementStateException as e:
            self._get_windows_img()
            self.logging.error("元素状态异常，不能进行操作！错误详情：{}".format(e))
            raise InvalidElementStateException

    # 清除内容
    def clear(self, key, value):
        try:
            self.logging.info("元素执行清除操作，方法：{}，值：{}".format(key, value))
            self.get_element(key, value).clear()
            self.logging.info("执行清除操作结束")
        except InvalidElementStateException as e:
            self._get_windows_img()
            self.logging.error("元素状态异常，不能进行操作！错误详情：{}".format(e))
            raise InvalidElementStateException

    # 获取子元素
    def select_child_elements(self, key, value1, value2):
        try:
            self.logging.info("获取元素子元素，方法：{}，值1：{}，值2：{}".format(key, value1, value2))
            return Select(self.get_element(key, value1)).select_by_visible_text(value2)
        except InvalidElementStateException as e:
            self._get_windows_img()
            self.logging.error("元素状态异常，不能进行操作！错误详情：{}".format(e))
            raise InvalidElementStateException

    # 获取输入框的值
    def get_attribute(self, key, value1, value2):
        try:
            self.logging.info("获取输入框值，方法：{}，值1：{}，值2：{}".format(key, value1, value2))
            attribute_value = self.get_element(key, value1).get_attribute(value2)
            self.logging.info("获取输入框值成功")
            return attribute_value
        except InvalidElementStateException as e:
            self._get_windows_img()
            self.logging.error("元素状态异常，不能进行操作！错误详情：{}".format(e))
            raise InvalidElementStateException

    # 获取文本的文本的值
    def get_text(self, key, value):
        try:
            self.logging.info("获取元素文本值，方法：{}，值：{}".format(key, value))
            text = self.get_element(key, value).text
            self.logging.info("获取元素文本值成功")
            return text
        except InvalidElementStateException as e:
            self._get_windows_img()
            self.logging.error("元素状态异常，不能进行操作！错误详情：{}".format(e))
            raise InvalidElementStateException

    # 鼠标移动点击机制
    def move_action(self, key, value):
        try:
            self.logging.info("移动鼠标点击，方法：{}，值：{}".format(key, value))
            xm = self.get_element(key, value)
            self._web_driver_wait(xm)
            webdriver.ActionChains(self.driver).click(xm).perform()
            self.logging.info("移动鼠标点击结束")
        except WebDriverException as e:
            self._get_windows_img()
            self.logging.error("移动鼠标点击失败！错误详情：{}".format(e))
            raise WebDriverException

    def frame(self, key, value):
        try:
            self.logging.info("开始切换frame方法{}，value={}".format(key, value))
            if key == "in":
                frame = self.driver.switch_to(value)
                self.logging.info("frame切换成功！")
                return frame
            elif key == "out":
                frame = self.driver.switch_to.default_content()
                self.logging.info("frame切换成功！")
                return frame
            elif key == "back":
                frame = self.driver.switch_to.parent_frame()
                self.logging.info("frame切换成功！")
                return frame
            else:
                self.logging.error("frame中不存在{}方法！".format(key))
                raise ValueError
        except NoSuchFrameException as e:
            self._get_windows_img()
            self.logging.error("frame执行{}失败，value={}".format(key, value))
            self.logging.error("错误详情：{}".format(e))
            raise NoSuchFrameException

        except InvalidSwitchToTargetException as e:
            self._get_windows_img()
            self.logging.error("{}切换到frame失败，请检查".format(key))
            self.logging.error("错误详情：{}".format(e))
            raise InvalidSwitchToTargetException

    '''
    断言方法
        方法	    说明
        title_is	判断当前页面的 title 是否完全等于（==）预期字符串，返回布尔值
        title_contains	判断当前页面的 title 是否包含预期字符串，返回布尔值
        presence_of_element_located	判断某个元素是否被加到了 dom 树里，并不代表该元素一定可见
        visibility_of_element_located	判断元素是否可见（可见代表元素非隐藏，并且元素宽和高都不等于 0）
        visibility_of	同上一方法，只是上一方法参数为locator，这个方法参数是 定位后的元素
        presence_of_all_elements_located	判断是否至少有 1 个元素存在于 dom 树中。举例：如果页面上有 n 个元素的 class 都是’wp’，那么只要有 1 个元素存在，这个方法就返回 True
        text_to_be_present_in_element	判断某个元素中的 text 是否 包含 了预期的字符串
        text_to_be_present_in_element_value	判断某个元素中的 value 属性是否包含 了预期的字符串
        frame_to_be_available_and_switch_to_it	判断该 frame 是否可以 switch进去，如果可以的话，返回 True 并且 switch 进去，否则返回 False
        invisibility_of_element_located	判断某个元素中是否不存在于dom树或不可见
        element_to_be_clickable	判断某个元素中是否可见并且可点击
        staleness_of	等某个元素从 dom 树中移除，注意，这个方法也是返回 True或 False
        element_to_be_selected	判断某个元素是否被选中了,一般用在下拉列表
        element_selection_state_to_be	判断某个元素的选中状态是否符合预期
        element_located_selection_state_to_be	跟上面的方法作用一样，只是上面的方法传入定位到的 element，而这个方法传入 locator
        alert_is_present	判断页面上是否存在 alert
    '''

    # 校验按钮是否为选中状态
    def is_selected(self, key, value):
        self.logging.info("校验按钮是否为选中状态开始")
        if self.get_element(key, value).is_selected():
            self.logging.info("校验按钮是否为选中状态结束")
        else:
            self._get_windows_img()
            self.logging.info("校验按钮是否为选中状态失败！")
            raise InvalidElementStateException

    def is_element_exist(self, key, value):
        self.logging.info("校验元素是否存在开始")
        self.get_element(key, value)
        self.logging.info("校验元素是否存在结束")

    def is_elements_exist(self, key, value):
        self.logging.info("校验元素列表是否存在开始")
        elements_list = self.get_element(key, value)
        n = len(elements_list)
        if n == 0:
            self.logging.info("校验元素列表为空！")
            raise ValueError
        elif n >= 1:
            self.logging.info("校验元素列表是否存在结束，元素个数：{}".format(n))

    '''返回bool值'''

    def is_title(self, title):
        try:
            self.logging.info("校验页面title是否为:{}".format(title))
            if WebDriverWait(self.driver, self.timeout).until(EC.title_is(title)):
                self.logging.info("校验通过！")
        except TimeoutException as e:
            self._get_windows_img()
            self.logging.info("校验失败！错误详情：{}".format(e))
            raise TimeoutException

    '''返回bool值'''

    def is_title_contains(self, title):
        self.logging.info("校验页面title_contains是否为:{}".format(title))
        if WebDriverWait(self.driver, self.timeout).until(EC.title_contains(title)):
            self.logging.info("校验通过！")
        else:
            self._get_windows_img()
            self.logging.info("校验失败！")
            raise WebDriverException

    '''返回bool值'''

    def is_text_in_element(self, key, value, text):
        try:
            self.logging.info("校验元素text值是否为:{}".format(text))
            if WebDriverWait(self.driver, self.timeout).until(
                    EC.text_to_be_present_in_element(self.get_element(key, value), text)):
                self.logging.info("校验通过！")
        except StaleElementReferenceException as e:
            self._get_windows_img()
            self.logging.info("校验失败！错误详情：{}".format(e))
            raise StaleElementReferenceException

    '''返回bool值, value为空字符串，返回Fasle'''

    def is_value_in_element(self, key, value, value1):
        self.logging.info("校验元素value值是否为:{}".format(value1))
        if WebDriverWait(self.driver, self.timeout).until(
                EC.text_to_be_present_in_element_value(self.get_element(key, value), value1)):
            self.logging.info("校验通过！")
        else:
            self._get_windows_img()
            self.logging.info("校验失败！")
            raise StaleElementReferenceException

    '''判断弹窗是否弹出'''

    def is_alert(self):
        self.logging.info("判断弹窗是否弹出")
        try:
            if WebDriverWait(self.driver, self.timeout).until(EC.alert_is_present()):
                self.logging.info("弹窗已弹出")
                EC.alert_is_present()(self.driver).accept()
                self.logging.info("弹窗已关闭")
        except NoAlertPresentException as e:
            self._get_windows_img()
            self.logging.info("弹窗不存在，错误详情：{}".format(e))
            raise NoAlertPresentException
