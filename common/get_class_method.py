# -*- coding: utf-8 -*- 
# @Time : 2020/8/14 19:58 
# @Author : daishuai 
# @File : get_class_method.py

from base import operation_driver


class ClassTool(object):

    @staticmethod
    def get_class_method(obj):

        if isinstance(obj, object):
            method_list = dir(obj)
            for method in method_list:
                if method.startswith("__"):
                    method_list.remove(method)
                    # print(method_list)

            return method_list
        else:
            Exception("获取类中方法失败!")
