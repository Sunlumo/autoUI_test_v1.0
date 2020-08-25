# -*- coding: utf-8 -*- 
# @Time : 2020/8/14 19:35 
# @Author : daishuai 
# @File : step_driver.py

from base import operation_driver, get_web_driver
from common import get_class_method


class StepDriver(object):

    def __init__(self, driver):
        self.driver = driver

    def step_run(self, method_name, value1=None, value2=None, value3=None, value4=None):
        op = __import__("base.operation_driver", fromlist=[''])
        wb = getattr(op, "WebTools")(self.driver)
        ct = get_class_method.ClassTool()
        method_list = ct.get_class_method(wb)
        if method_name in method_list:
            mathod = getattr(wb, method_name)
            keys_num = mathod.__code__.co_argcount
            if keys_num == 1:
                mathod()
            elif keys_num == 2:
                mathod(value1)
            elif keys_num == 3:
                mathod(value1, value2)
            elif keys_num == 4:
                mathod(value1, value2, value3)
            elif keys_num == 5:
                mathod(value1, value2, value3, value4)

        else:
            print("操作类中不存在{}方法！".format(method_name))
