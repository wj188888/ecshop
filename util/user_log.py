import os
import logging
import datetime


class UserLog:
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        # # # 控制台输出日志
        # console = logging.StreamHandler()
        # self.logger.addHandler(console)

        # 文件名字
        base_dir = (os.path.dirname(os.path.abspath(__file__)))
        log_dir = os.path.join(base_dir,'log')
        log_file = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")+".log"
        log_name = log_dir + "\\" + log_file
        print(log_name)
        # 输出日志到文件
        self.file_handle = logging.FileHandler(log_name)
        self.file_handle.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s %(filename)s---> %(funcName)s %(levelno)s: %(levelname)s ----> %(message)s')
        self.file_handle.setFormatter(formatter)
        self.logger.addHandler(self.file_handle)

    def get_log(self):
        return self.logger

    def close_handle(self):

        self.logger.removeHandler(self.file_handle)
        self.file_handle.close()


if __name__ == '__main__':
    user = UserLog()
    logger = user.get_log()
    logger.info('info logger')
    logger.warning("warning")
    user.close_handle()