import pytest

from base import case_driver
from utilities import excel_util, CMD_util, time_util
from conf.com_config import Path, GetLogger
import conf.com_config


# @pytest.fixture(scope="session")
# def test_int():
#     path = Path()
#     oe = excel_util.OperateExcel(conf.com_config.get_test_case_path(path.TEST_CASE_PATH))
#     step_data_list = oe.read_excel_data()
#     logger = GetLogger(path).logger
