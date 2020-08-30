# -*- coding: utf-8 -*- 
# @Time : 2020/8/14 19:35 
# @Author : daishuai 
# @File : case_driver.py

from base import step_driver
from base import get_web_driver
import time
import conf.com_config


class CaseDriver(object):

    def __init__(self, step_data_list):
        self.step_data_list = step_data_list
        self.logging = conf.com_config.get_logger()

    def case_run(self, browser_type, case_num):
        try:
            num = 1
            self.logging.info("==============开始执行第{}条用例=============".format(case_num))
            self.logging.info("开始打开浏览器".format(case_num))
            gd = get_web_driver.GetWebDriver(browser_type).open_browser()
            sd = step_driver.StepDriver(gd, self.logging)
            for step_data in self.step_data_list:
                self.logging.info("")
                method_name = step_data[0]
                vaule1 = step_data[1]
                vaule2 = step_data[2]
                vaule3 = step_data[3]
                vaule4 = step_data[4]
                sd.step_run(method_name, vaule1, vaule2, vaule3, vaule4, num)
                num = num + 1
                time.sleep(2)
            gd.close()
            self.logging.info("==============执行第{}条用例完成==============".format(case_num))
        except Exception as e:
            self.logging.error("执行第{}条用例时发生运行时错误！错误详情：{}".format(case_num, e))
            self.logging.error("==============执行第{}条用例失败==============".format(case_num))
            raise Exception
