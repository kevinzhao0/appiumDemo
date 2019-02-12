# coding=utf-8

import logging.handlers
import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class MyLog(object):
    def __init__(self, deviceName):
        log_file = PATH("../../log/test.log")
        # logger命名实例化
        self.logger = logging.getLogger(deviceName)
        if not self.logger.handlers:
            # 添加文件handler
            file_handler = logging.handlers.RotatingFileHandler(log_file, maxBytes=1024*1024, backupCount=5)
            # 添加控制台handler
            # console_handler = logging.StreamHandler(sys.stdout)
            # 指定日志输出格式
            fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'
            formatter = logging.Formatter(fmt)
            # 文件日志输出格式
            file_handler.setFormatter(formatter)
            # 控制台日志输出格式
            # console_handler.formatter = formatter
            # 添加handler
            self.logger.addHandler(file_handler)
            # self.logger.addHandler(console_handler)
            # 设定日志输出级别
            self.logger.setLevel(logging.INFO)

    def log_start_line(self):
        self.logger.info("---------------------start-----------------------------")

    def log_end_line(self):
        self.logger.info("----------------------end------------------------------")

    def log_info(self, msg):
        self.logger.info(msg)