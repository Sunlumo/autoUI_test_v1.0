# -*- coding: utf-8 -*- 
# @Time : 2020/8/14 19:35 
# @Author : daishuai 
# @File : case_driver.py

from base import step_driver
from base import get_web_driver
import time


class CaseDriver(object):

    def __init__(self, step_data_list):
        self.step_data_list = step_data_list

    def case_run(self, browser_type):
        gd = get_web_driver.GetWebDriver(browser_type).open_browser()
        sd = step_driver.StepDriver(gd)
        for step_data in self.step_data_list:
            method_name = step_data[0]
            vaule1 = step_data[1]
            vaule2 = step_data[2]
            vaule3 = step_data[3]
            vaule4 = step_data[4]
            sd.step_run(method_name, vaule1, vaule2, vaule3, vaule4)
            time.sleep(2)
        gd.close()
