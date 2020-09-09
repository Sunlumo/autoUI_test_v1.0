# -*- coding: utf-8 -*- 
# @Time : 2020/8/13 21:33 
# @Author : daishuai 
# @File : test_main.py
import allure
import pytest

from base import case_driver
from utilities import excel_util, CMD_util
import conf.com_config

test_case_path = conf.com_config.TEST_CASE_PATH
oe = excel_util.OperateExcel(conf.com_config.get_test_case_path())
logger = conf.com_config.get_logger()


@allure.feature('百度搜索')
class TestCase(object):
    step_data_list = oe.read_excel_data()

    # @allure.description("这是搜索喜羊羊的一段描述")
    @allure.title("搜索喜羊羊")
    @allure.story('搜索喜羊羊')
    @pytest.mark.parametrize("case_data,step_data", step_data_list)
    def test_case(self, case_data,step_data):
        browser_type = conf.com_config.get_browser_type()
        cd = case_driver.TestCaseDriver(step_data, logger)
        cd.test_case_run(browser_type)
        allure.dynamic.title(case_data[3])
        allure.dynamic.severity("NORMAL")
        allure.dynamic.description(case_data[5])
        allure.dynamic.story(case_data[2])


if __name__ == "__main__":
    allure_conf = conf.com_config.get_allure_conf()
    # print(conf.com_config.get_pytest_command(allure_conf[0]))
    pytest.main(conf.com_config.get_pytest_command(allure_conf[0]))
    CMD_util.cmd_runner("allure generate ./{}/ -o ./{}/ --clean".format(allure_conf[0], allure_conf[1]))
