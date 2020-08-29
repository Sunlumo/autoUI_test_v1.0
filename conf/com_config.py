import yaml
import os
import logging


logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
handler = logging.FileHandler("log.txt")
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

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

FILE_PATH = os.path.dirname(os.path.abspath('.'))

def get_yaml_data(yaml_file):
    # 打开yaml文件
    print("***获取yaml文件数据***")
    file = open(yaml_file, 'r', encoding="utf-8")
    file_data = file.read()
    file.close()

    print(file_data)
    print("类型：", type(file_data))

    # 将字符串转化为字典或列表
    print("***转化yaml数据为字典或列表***")
    data = yaml.load(file_data)
    print(data)
    print("类型：", type(data))
    return data


# current_path = os.path.abspath(".")
# yaml_path = os.path.join(current_path, "config.yaml")
# get_yaml_data(yaml_path)

