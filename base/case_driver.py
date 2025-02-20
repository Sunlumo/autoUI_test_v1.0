# -*- coding: utf-8 -*- 
# @Time : 2020/8/14 19:35 
# @Author : daishuai 
# @File : case_driver.py

from base import step_driver
from base import get_web_driver
import time
import allure


class TestCaseDriver(object):

    def __init__(self, step_data_list, logger,path):
        self.step_data_list = step_data_list
        self.logging = logger
        self.path = path
        self.case_id = int(step_data_list[0][1])

    def test_case_run(self, browser_type):
        gd = get_web_driver.GetWebDriver(browser_type).open_browser()
        try:
            step_num = 1
            self.logging.info("==============开始执行第{}条用例=============".format(self.case_id))
            self.logging.info("开始打开浏览器".format(self.case_id))
            sd = step_driver.StepDriver(gd, self.logging, self.case_id,self.path)
            for step_data in self.step_data_list:
                with allure.step("第{}步：{}".format(int(step_data[0]), step_data[2])):
                    self.logging.info("")
                    method_name = step_data[4]
                    vaule1 = step_data[5]
                    vaule2 = step_data[6]
                    vaule3 = step_data[7]
                    try:
                        sd.step_run(method_name, vaule1, vaule2, vaule3, int(step_data[0]))
                    except Exception:
                        allure.attach('{}'.format(step_data), '失败')
                        raise Exception
                    allure.attach('{}'.format(step_data), '成功')
                    step_num = step_num + 1
                    time.sleep(2)
            gd.close()
            self.logging.info("==============执行第{}条用例完成==============".format(self.case_id))
        except Exception as e:
            self.logging.error("执行第{}条用例时发生错误！错误详情：{}".format(self.case_id, e))
            self.logging.error("==============执行第{}条用例失败==============".format(self.case_id))
            gd.close()
            raise Exception
