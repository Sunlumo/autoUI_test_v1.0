import os
import sys
import time
import unittest
import logging

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from base import get_web_driver
import conf.com_config

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(ROOT_DIR)


class WebTools(object):

    def __init__(self, driver, timeout):
        self.driver = driver
        self.timeout = timeout

    def get_element(self, key, value):

        element = None

        try:

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
                logging.error("定位方式不存在！")

            return element

        except Exception as e:
            self._get_windows_img()

    # 打开页面
    def get_web_page(self, url):
        self.driver.get(url)

    # 跳转页面
    def jump_web_page(self, driver, page):
        driver.get(self.get_web_page(page))
        driver.maximize_window()

        if isinstance(self.timeout, int):
            time.sleep(self.timeout)

    # 这时切换到新窗口
    def current_handel(self):
        all_handles = self.driver.window_handles
        for handle in all_handles:
            self.driver.switch_to.window(handle)

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
        """
        在这里我们把file_path这个参数写死，直接保存到我们项目根目录的一个文件夹.\Screenshots下
        """
        file_path = conf.com_config.FILE_PATH + '/screenshots/'
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
        except NameError as e:
            self._get_windows_img()

    # 输入内容
    def input(self, key, value, input_value):
        return self.get_element(key, value).send_keys(input_value)

    # 鼠标点击
    def click(self, key, value):
        return self.get_element(key, value).click()

    # 清除内容
    def clear(self, key, value):
        self._web_driver_wait(self.get_element(key, value).clear())

    # 获取子元素
    def select_child_elements(self, key, value1, value2):
        return Select(self.get_element(key, value1)).select_by_visible_text(value2)

    # 获取输入框的值
    def get_attribute(self, key, value1, value2):
        attribute_value = self.get_element(key, value1).get_attribute(value2)
        return attribute_value

    # 获取下拉框的文本的值
    def get_text(self, key, value):
        text = self.get_element(key, value).text
        return text

    # # 鼠标移动点击机制
    def move_action(self, key, value):
        xm = self.get_element(key, value)
        self._web_driver_wait(xm)
        webdriver.ActionChains(self.driver).click(xm).perform()

    # 校验按钮是否为选中状态
    def is_selected(self, key, value):
        return self.get_element(key, value).is_selected()

    def is_element_exist(self, key, value):
        try:
            self.get_element(key, value)
            return True
        except:
            return False

    def is_elements_exist(self, key, value):
        elements_list = self.get_element(key, value)
        n = len(elements_list)
        if n == 0:
            return False
        elif n == 1:
            return True
        else:
            print("定位到元素的个数：%s" % n)
            return True

    '''返回bool值'''

    def is_title(self, title):
        result = WebDriverWait(self.driver, self.timeout).until(EC.title_is(title))
        assert (result, True)

    '''返回bool值'''

    def is_title_contains(self, title):
        result = WebDriverWait(self.driver, self.timeout).until(EC.title_contains(title))
        assert (result, True)

    '''返回bool值'''

    def is_text_in_element(self, key, value, text):
        result = WebDriverWait(self.driver, self.timeout).until(
            EC.text_to_be_present_in_element(self.get_element(key, value), text))
        assert (result, True)

    def is_value_in_element(self, key, value, value1):
        '''返回bool值, value为空字符串，返回Fasle'''
        try:
            result = WebDriverWait(self.driver, self.timeout).until(
                EC.text_to_be_present_in_element_value(self.get_element(key, value), value1))
            return result
        except:
            return False

    def is_alert(self):
        try:
            result = WebDriverWait(self.driver, self.timeout).until(EC.alert_is_present())
            return result
        except:
            return False
