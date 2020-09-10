import time

import yaml
import os
import logging
import utilities.time_util

ROOT_PATH = os.getcwd()
CONFIG_PATH = ROOT_PATH + "\\conf\\config.yaml"


class Path(object):
    TIME = utilities.time_util.GetTime().get_date()

    RESULT_PATH = "\\test_result\\" + TIME
    PICTURE_PATH = ROOT_PATH + RESULT_PATH + "\\screenshots\\"
    TEST_CASE_PATH = ROOT_PATH + "\\test_data\\"
    LOGGING_PATH = ROOT_PATH + RESULT_PATH + "\\log"


"""
日志等级（level）	描述
DEBUG	最详细的日志信息，典型应用场景是 问题诊断
INFO	信息详细程度仅次于DEBUG，通常只记录关键节点信息，用于确认一切都是按照我们预期的那样进行工作
WARNING	当某些不期望的事情发生时记录的信息（如，磁盘可用空间较低），但是此时应用程序还是正常运行的
ERROR	由于一个更严重的问题导致某些功能不能正常运行时记录的信息
CRITICAL	当发生严重错误，导致应用程序不能继续运行时记录的信息
链接：https://www.jianshu.com/p/e5595fd9f0e8
"""


class GetLogger(object):

    def __init__(self, path):
        self.path = path
        self.logger = self.get_logger()

    def get_logger(self):
        conf = get_log_conf()
        creat_path(self.path.LOGGING_PATH)
        logger_file = self.path.LOGGING_PATH + "\\log_" + utilities.time_util.GetTime.get_time_now() + ".txt"
        time.sleep(2)
        logger = logging.getLogger(__name__)
        logger.handlers.clear()
        logger.propagate = False
        if conf.get("level") == "info":
            logger.setLevel(level=logging.INFO)
        elif conf.get("level") == "debug":
            logger.setLevel(level=logging.DEBUG)
        elif conf.get("level") == "error":
            logger.setLevel(level=logging.ERROR)
        elif conf.get("level") == "critical":
            logger.setLevel(level=logging.CRITICAL)
        else:
            logger.setLevel(level=logging.INFO)
        handler = logging.FileHandler(logger_file, encoding='utf-8')
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter(conf.get("formatter"))
        handler.setFormatter(formatter)
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        console.setFormatter(formatter)

        logger.addHandler(handler)
        logger.addHandler(console)

        return logger


def creat_path(path):
    if os.path.exists(path):
        pass
    else:
        os.makedirs(path)


"""
***获取yaml文件数据***
# yaml键值对：即python中字典
usr: my
psw: 123455
类型：<class 'str'>
***转化yaml数据为字典或列表***
{'usr': 'my', 'psw': 123455}
类型：<class 'dict'>
"""


def get_yaml_data(yaml_file):
    # 打开yaml文件
    file = open(yaml_file, 'r', encoding="utf-8")
    file_data = file.read()
    file.close()

    # 将字符串转化为字典或列表
    data = yaml.load(file_data, Loader=yaml.FullLoader)
    return data


def get_log_conf():
    conf = get_yaml_data(CONFIG_PATH).get("logging")
    return conf


def get_browser_type():
    browser_type = get_yaml_data(CONFIG_PATH).get("webdriver").get("browser_type")
    if browser_type != "":
        return browser_type
    else:
        return "Chrome"


def get_test_case_path(test_case_path):
    conf = get_yaml_data(CONFIG_PATH).get("test_case_path")
    if conf.get("path") != "":
        path = conf.get("path")
    else:
        path = test_case_path
    file_list = os.listdir(path)
    file_list1 = []
    for file in file_list:
        if file.split(".")[0].startswith("test_") and file.split(".")[1] == "xlsx":
            file_list1.append(path + "\\" + file)
        else:
            pass
    return file_list1


def get_timeout():
    return get_yaml_data(CONFIG_PATH).get("webdriver").get("timeout")


def get_pytest_command(result_path):
    pytest_command_list = []
    pytest_command = get_yaml_data(CONFIG_PATH).get("webdriver").get("pytest")
    for command in pytest_command:
        pytest_command_list.append(command)
    result_path = result_path.replace("\\", "/")
    allure_command = "--alluredir=.{}".format(result_path)
    pytest_command_list.append(allure_command)
    return pytest_command_list


def get_allure_conf(df_result_path):
    result_path = get_yaml_data(CONFIG_PATH).get("allure").get("result_path")
    report_path = get_yaml_data(CONFIG_PATH).get("allure").get("report_path")
    if result_path == "":
        result_path = df_result_path + "\\result"
    if report_path == "":
        report_path = df_result_path + "\\report"
    allure_conf = [result_path, report_path]
    return allure_conf


def get_mysql_conf():
    conf = get_yaml_data(CONFIG_PATH).get("DB_config").get("mysql")
    mysql_conf_list = [v for k, v in conf.items()]
    return mysql_conf_list
