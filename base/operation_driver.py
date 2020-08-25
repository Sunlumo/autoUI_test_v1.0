import os
import sys
import time
import unittest

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from base import get_web_driver

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(ROOT_DIR)


class WebTools(object):

    def __init__(self, driver):
        self.driver = driver

    # 打开页面
    def get_web_page(self, url):
        self.driver.get(url)

    # 跳转页面
    def jump_web_page(self, driver, page, time_wait=1):
        driver.get(self.get_web_page(page))
        driver.maximize_window()

        if isinstance(time_wait, int):
            time.sleep(time_wait)

    # 这时切换到新窗口
    def current_handel(self, driver):
        all_handles = driver.window_handles
        for handle in all_handles:
            driver.switch_to.window(handle)

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
    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)

    # 显性等待时间
    def web_driver_wait(self, timeout, value):
        element = self.driver.find_element(By.ID, value)
        WebDriverWait(self.driver,timeout).until(EC.presence_of_element_located(element))

    # 保存图片
    def get_windows_img(self, driver):
        """
        在这里我们把file_path这个参数写死，直接保存到我们项目根目录的一个文件夹.\Screenshots下
        """
        file_path = os.path.dirname(os.path.abspath('.')) + '/screenshots/'
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            driver.get_screenshot_as_file(screen_name)
        except NameError as e:
            self.get_windows_img()

    # 输入内容方法
    def input(self, type, value, input_value):
        if type == "xpath":
            self.driver.find_element_by_xpath(value).send_keys(input_value)
        elif type == "class_name":
            self.driver.find_element_by_class_name(value).send_keys(input_value)
        elif type == "id":
            self.driver.find_element_by_id(value).send_keys(input_value)
        elif type == "name":
            self.driver.find_element_by_name(value).send_keys(input_value)
        elif type == "link_text":
            self.driver.find_element_by_link_text(value).send_keys(input_value)
        elif type == "partial_link_text":
            self.driver.find_element_by_partial_link_text(value).send_keys(input_value)

    # 鼠标事件方法一
    def click(self, type, value):
        if type == "xpath":
            self.driver.find_element_by_xpath(value).click()
        elif type == "class_name":
            self.driver.find_element_by_class_name(value).click()
        elif type == "id":
            self.driver.find_element_by_id(value).click()
        elif type == "name":
            self.driver.find_element_by_name(value).click()
        elif type == "link_text":
            self.driver.find_element_by_link_text(value).click()
        elif type == "partial_link_text":
            self.driver.find_element_by_partial_link_text(value).click()

    # 鼠标事件方法二
    def clear(self, type, value):
        if type == "xpath":
            self.driver.find_element_by_xpath(value).clear()
        elif type == "id":
            self.driver.find_element_by_id(value).clear()
        elif type == "name":
            self.driver.find_element_by_name(value).clear()
        elif type == "link_text":
            self.driver.find_element_by_link_text(value).clear()
        elif type == "partial_link_text":
            self.driver.find_element_by_partial_link_text(value).clear()

    # 验证元素是否存在
    def check_element(self, key_type, value):
        if key_type == "xpath":
            self.driver.find_element_by_xpath(value)
        elif key_type == "id":
            self.driver.find_element_by_id(value)
        elif key_type == "name":
            self.driver.find_element_by_name(value)
        elif key_type == "link_text":
            self.driver.find_element_by_link_text(value)
        elif key_type == "partial_link_text":
            self.driver.find_element_by_partial_link_text(value)

    # 获取子元素
    def select_child_elements(self, type, value1, value2):
        if type == "xpath":
            Select(self.driver.find_element_by_xpath(value1)).select_by_visible_text(value2)
        elif type == "id":
            Select(self.driver.find_element_by_id(value1)).select_by_visible_text(value2)
        elif type == "name":
            Select(self.driver.find_element_by_name(value1)).select_by_visible_text(value2)
        elif type == "link_text":
            Select(self.driver.find_element_by_link_text(value1)).select_by_visible_text(value2)
        elif type == "partial_link_text":
            Select(self.driver.find_element_by_partial_link_text(value1)).select_by_visible_text(value2)

    # 获取输入框的值
    def get_attribute(self, type, value1, value2):
        if type == "xpath":
            Value = self.driver.find_element_by_xpath(value1).get_attribute(value2)
            return Value
        elif type == "name":
            Value = self.driver.find_element_by_name(value1).get_attribute(value2)
            return Value
        elif type == "link_text":
            Value = self.driver.find_element_by_link_text(value1).get_attribute(value2)
            return Value
        elif type == "class_name":
            Value = self.driver.find_element_by_class_name(value1).get_attribute(value2)
            return Value
        elif type == "id":
            Value = self.driver.find_element_by_id(value1).get_attribute(value2)
            return Value

    # 获取下拉框的文本的值
    def get_text(self, type, value):
        if type == "xpath":
            text = self.driver.find_element_by_xpath(value).text
            return text
        elif type == "name":
            text = self.driver.find_element_by_name(value).text
            return text
        elif type == "link_text":
            text = self.driver.find_element_by_link_text(value).text
            return text
        elif type == "class_name":
            text = self.driver.find_element_by_class_name(value).text
            return text
        elif type == "id":
            text = self.driver.find_element_by_id(value).text
            return text

    # # 鼠标移动点击机制
    def move_action(self, type, value):
        if type == "xpath":
            xm = self.driver.find_element_by_xpath(value)
            webdriver.ActionChains(self.driver).click(xm).perform()
        elif type == "id":
            xm = self.driver.find_element_by_id(value)
            webdriver.ActionChains(self.driver).click(xm).perform()
        elif type == "name":
            xm = self.driver.find_element_by_name(value)
            webdriver.ActionChains(self.driver).click(xm).perform()
        elif type == "link_text":
            xm = self.driver.find_element_by_link_text(value)
            webdriver.ActionChains(self.driver).click(xm).perform()

    # 校验按钮是否为选中状态
    def is_selected(self, type, value):
        if type == "id":
            self.driver.find_element_by_id(value).is_selected()
        elif type == "xpath":
            self.driver.find_element_by_xpath(value).is_selected()
        elif type == "class_name":
            self.driver.find_element_by_class_name(value).is_selected()
        elif type == "name":
            self.driver.find_element_by_name(value).is_selected()
        elif type == "link_text":
            self.driver.find_element_by_link_text(value).is_selected()

    def isElementExist(self, locator):
        try:
            self.findElement(locator)
            return True
        except:
            return False

    def isElementExist2(self, locator):
        eles = self.findElements(locator)
        n = len(eles)
        if n == 0:
            return False
        elif n == 1:
            return True
        else:
            print("定位到元素的个数：%s"%n)
            return True

    def is_title(self, title):
        '''返回bool值'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_is(title))
            return result
        except:
            return False

    def is_title_contains(self, title):
        '''返回bool值'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_contains(title))
            return result
        except:
            return False

    def is_text_in_element(self, locator, _text):
        '''返回bool值'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element(locator, _text))
            return result
        except:
            return False

    def is_value_in_element(self, locator, _value):
        '''返回bool值, value为空字符串，返回Fasle'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element_value(locator, _value))
            return result
        except:
            return False

    def is_alert(self):
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.alert_is_present())
            return result
        except:
            return False
