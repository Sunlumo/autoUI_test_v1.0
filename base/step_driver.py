# -*- coding: utf-8 -*- 
# @Time : 2020/8/14 19:35 
# @Author : daishuai 
# @File : step_driver.py

from base import operation_driver, get_web_driver
from common import get_class_method
import conf.com_config


class StepDriver(object):

    def __init__(self, driver, logger, case_id):
        self.driver = driver
        self.logging = logger
        self.case_id = case_id

    def step_run(self, method_name, value1=None, value2=None, value3=None, value4=None, num=None):
        try:
            timeout = conf.com_config.get_timeout()
            op = __import__("base.operation_driver", fromlist=[''])
            # self.logging.info("生成WebTools类对象")
            wb = getattr(op, "WebTools")(self.driver, self.logging, timeout, self.case_id, num)
            # self.logging.info("生成WebTools类对象成功")
            ct = get_class_method.ClassTool()
            method_list = ct.get_class_method(wb)
            self.logging.debug("加载WebTools类对象方法、属性：{}".format(method_list))
            self.logging.info("-------------开始执行步骤{}----------------".format(num))
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
                elif keys_num == 5:
                    method(value1, value2, value3, value4)
                self.logging.info("-------------执行步骤{}完成----------------".format(num))
                self.logging.info("                                         ")

            else:
                self.logging.error("操作类中不存在{}方法！".format(method_name))
                raise ValueError
        except RuntimeError as e:
            self.logging.error("执行步骤时发生运行时错误！错误详情：{}".format(e))
            raise RuntimeError
