# -*- coding: utf-8 -*- 
# @Time : 2020/8/13 21:33 
# @Author : daishuai 
# @File : test_main.py

import pytest

from base import operation_driver
from base import case_driver
from utilities import operate_excel


class TestCase(object):
    step_data_list = operate_excel.OperateExcel("C://Users//22131//Desktop//test.xlsx").read_excel_data()

    @pytest.mark.parametrize("step_data_list", step_data_list)
    def test_case(self, step_data_list):
        browser_type = "Chrome"
        cd = case_driver.CaseDriver(step_data_list)
        cd.case_run(browser_type)


if __name__ == "__main__":
    pytest.main()
