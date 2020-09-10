# -*- coding: utf-8 -*- 
# @Time : 2020/8/13 21:33 
# @Author : daishuai 
# @File : test_main.py
import allure
import pytest

from base import case_driver
from utilities import excel_util, CMD_util
from conf.com_config import Path, GetLogger
import conf.com_config

path = Path()
oe = excel_util.OperateExcel(conf.com_config.get_test_case_path(path.TEST_CASE_PATH))
step_data_list = oe.read_excel_data()
logger = GetLogger(path).logger


# @allure.epic("测试用例集")
# @allure.feature('百度搜索')
class TestCase(object):

    # @allure.description("这是搜索喜羊羊的一段描述")
    @allure.title("搜索喜羊羊")
    # @allure.story('搜索喜羊羊')
    # @pytest.mark.usefixtures("get_status")
    @pytest.mark.parametrize("case_data,step_data", step_data_list)
    def test_case(self, case_data, step_data):
        allure.dynamic.feature(case_data[1])
        allure.dynamic.story(case_data[2])
        allure.dynamic.title(case_data[3])
        allure.dynamic.severity("NORMAL")
        allure.dynamic.description(case_data[5])
        browser_type = conf.com_config.get_browser_type()
        cd = case_driver.TestCaseDriver(step_data, logger, path)
        cd.test_case_run(browser_type)


if __name__ == "__main__":
    allure_conf = conf.com_config.get_allure_conf(path.RESULT_PATH)
    # print(conf.com_config.get_pytest_command(allure_conf[0]))
    pytest.main(conf.com_config.get_pytest_command(allure_conf[0]))
    CMD_util.cmd_runner("allure generate ./{}/ -o ./{}/ --clean".format(allure_conf[0], allure_conf[1]))
