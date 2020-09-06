# -*- coding: utf-8 -*- 
# @Time : 2020/8/13 21:33 
# @Author : daishuai 
# @File : test_main.py
import allure
import pytest

from base import case_driver
from utilities import excel_util, CMD_util
import conf.com_config


@allure.feature('百度搜索')
class TestCase(object):
    test_case_path = conf.com_config.TEST_CASE_PATH
    step_data_list = excel_util.OperateExcel(conf.com_config.get_test_case_path()).read_excel_data()

    @allure.description("这是搜索喜羊羊的一段描述")
    @allure.title("搜索喜羊羊")
    @allure.story('搜索喜羊羊')
    @pytest.mark.parametrize("step_data_list", step_data_list)
    def test_case(self, step_data_list):
        allure.dynamic.story()
        logger = conf.com_config.get_logger()
        browser_type = conf.com_config.get_browser_type()
        cd = case_driver.TestCaseDriver(step_data_list, logger)
        cd.test_case_run(browser_type)


if __name__ == "__main__":
    allure_conf = conf.com_config.get_allure_conf()
    # print(conf.com_config.get_pytest_command(allure_conf[0]))
    pytest.main(conf.com_config.get_pytest_command(allure_conf[0]))
    CMD_util.cmd_runner("allure generate ./{}/ -o ./{}/ --clean".format(allure_conf[0], allure_conf[1]))
