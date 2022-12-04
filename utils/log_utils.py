import logging
import os
import time

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# 定义日志文件路径
LOG_PATH = os.path.join(BASE_PATH, "log")


class Logger:
    def __init__(self):
        # 定义日志位置和文件名
        self.logname = os.path.join(LOG_PATH, "{}.log".format(time.strftime("%Y-%m-%d")))
        # 定义一个日志容器
        self.logger = logging.getLogger("log")
        # 设置日志打印的级别
        self.logger.setLevel(logging.DEBUG)
        # 创建日志输入的格式
        self.formater = logging.Formatter('[%(asctime)s][%(filename)s%(lineno)d][%(levelname)s]:%(message)s')
        # 创建日志处理器，用来存放日志文件
        self.filelogger = logging.FileHandler(self.logname, mode='a', encoding="UTF-8")
        # 创建日志处理器，在控制台打印
        self.console = logging.StreamHandler()
        # 设置控制台打印日志界别
        self.console.setLevel(logging.DEBUG)
        # 文件存放日志级别
        self.filelogger.setLevel(logging.DEBUG)
        # 文件存放日志格式
        self.filelogger.setFormatter(self.formater)
        # 控制台打印日志格式
        self.console.setFormatter(self.formater)
        # 将日志输出渠道添加到日志收集器中
        self.logger.addHandler(self.filelogger)
        self.logger.addHandler(self.console)


logger = Logger().logger

if __name__ == '__main__':
    logger.info("---info---")
    logger.debug("---debug---")
    logger.warning("---warning---")
    logger.error("---error---")
