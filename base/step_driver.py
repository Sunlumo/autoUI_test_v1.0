# -*- coding: utf-8 -*- 
# @Time : 2020/8/14 19:35 
# @Author : daishuai 
# @File : step_driver.py

from common import get_class_method
import conf.com_config


class StepDriver(object):

    def __init__(self, driver, logger, case_id, path):
        self.driver = driver
        self.logging = logger
        self.path = path
        self.case_id = case_id

    def step_run(self, method_name, value1=None, value2=None, value3=None, num=None):
        try:
            timeout = conf.com_config.get_timeout()
            op = __import__("base.operation_driver", fromlist=[''])
            self.logging.debug("生成WebTools类对象")
            wb = getattr(op, "WebTools")(self.driver, self.logging, timeout, self.case_id, num, self.path)
            self.logging.debug("生成WebTools类对象成功")
            ct = get_class_method.ClassTool()
            method_list = ct.get_class_method(wb)
            self.logging.debug("加载WebTools类对象方法、属性：{}".format(method_list))
            self.logging.info("-------------开始执行步骤{}_{}----------------".format(self.case_id, num))
            if method_name in method_list:
                method = getattr(wb, method_name)
                keys_num = method.__code__.co_argcount
                if keys_num == 1:
                    method()
                elif keys_num == 2:
                    method(value1)
                elif keys_num == 3:
                    method(value1, value2)
                elif keys_num == 4:
                    method(value1, value2, value3)
                self.logging.info("-------------执行步骤{}_{}完成----------------".format(self.case_id, num))
                self.logging.info("                                         ")

            else:
                self.logging.error("操作类中不存在{}方法！".format(method_name))
                raise ValueError
        except Exception as e:
            self.logging.error("错误详情：{}".format(e))
            self.logging.error("-------------执行执行步骤{}_{}失败----------------".format(self.case_id, num))
            raise Exception
