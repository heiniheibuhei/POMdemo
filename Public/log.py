# coding=utf-8
import logging


class Logger(object):
    def __init__(self):
        self.logger = logging.getLogger()
        logging.root.setLevel(logging.NOTSET)
        self.log_file_name = 'test.log'
        # 日志输出级别
        self.console_output_level = 'INFO'
        self.log_output_level = 'DEBUG'
        # 日志输出格式
        self.formatter = loging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

    def get_logger(self):
        '''封装logger'''
        if not self.logger.handlers:
            console_hangler = logging.StreamHandler()
            console_hangler.setFormatter(self.formatter)
            console_hangler.setForLevel(self.console_output_level)
            self.logger.addHandler(console_hangler)
            file_handler = logging.FileHandler(self.formatter)
            file_handler.setFormatter(self.formatter)
            file_handler.setLevel(self.log_file_level)
            self.logger.addHandler(file_handler)
            return self.logger
logger = Logger().get_logger()