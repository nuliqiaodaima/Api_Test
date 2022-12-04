# pip install configparser
import configparser
import os
import yaml

ini_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config", "setting.ini")
data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "data.yaml")


class FileRead:
    def __init__(self):
        self.data_path = data_path
        self.ini_path = ini_path

    # 读取配置文件
    def read_ini(self):
        # 进行实例化
        config = configparser.ConfigParser()
        config.read(self.ini_path, encoding="utf8")
        return config

    # 读取yaml测试数据
    def read_data(self):
        # 打开yaml文件
        f = open(self.data_path, encoding="utf8")
        # 读取文件
        data = yaml.safe_load(f)
        return data


base_data = FileRead()
