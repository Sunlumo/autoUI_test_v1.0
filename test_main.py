# -*- coding: utf-8 -*- 
# @Time : 2020/8/13 21:33 
# @Author : daishuai 
# @File : test_main.py

import pytest

from base import case_driver
from utilities import excel_util
import conf.com_config


class TestCase(object):
    test_case_path = conf.com_config.TEST_CASE_PATH
    step_data_list = excel_util.OperateExcel(conf.com_config.get_test_case_path()).read_excel_data()

    @pytest.mark.parametrize("step_data_list", step_data_list)
    def test_case(self, step_data_list):
        browser_type = conf.com_config.get_browser_type()
        case_id = int(step_data_list[0])
        cd = case_driver.CaseDriver(step_data_list[1])
        cd.case_run(browser_type, case_id)


if __name__ == "__main__":
    pytest.main()
