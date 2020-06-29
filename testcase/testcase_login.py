import sys
sys.path.append('D:\study\ecshop')
import unittest
import HTMLTestRunner
import time
from page.login import Login
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from util.user_log import UserLog
import os
import datetime
import logging
import ddt
import threading
from util.send_email import send_report_email,send_email

#获取log日志存放目
currentpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
loggerpath = currentpath + "\\" + "logs"
filename = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")+".logs"
imagename = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
loggername = os.path.join(loggerpath,filename)
print(loggername)
# #定义logger日志
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger_hander = logging.FileHandler(loggername)
formator = logging.Formatter(" %(asctime)s--%(filename)s --%(levelname)s--%(thread)d--%(lineno)d --%(message)s")
logger_hander.setFormatter(formator)
logger.addHandler(logger_hander)


class Testcase(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome()
        chrome_options = Options() #无头模式，不会看到启动浏览器
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)

    def test_login_success(self):
        logger.info("开始登录成功测试")
        l = Login(self.driver)
        self.assertTrue(l.login("wangyu","W7548zhang"),msg="登录失败，用例失败")

    def test_login_fail(self):
        logger.info("开始登录失败测试测试")
        l = Login(self.driver)
        self.assertFalse(l.login("wangyu", "123456"), msg="用例失败")


    def test_user_input(self):
        logger.info("用户名输入测试")
        l = Login(self.driver)
        self.assertTrue(l.userobject("23556"))
        self.driver.save_screenshot("d:\\study\\ecshop\\report\\" + imagename +"user_input_int.png")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    # unittest.main()
    sutie = unittest.TestSuite()
    sutie.addTest(Testcase("test_login_success"))
    sutie.addTest(Testcase("test_login_fail"))
    sutie.addTest(Testcase("test_user_input"))

    # 控制台看到测试运行结果
    # runner = unittest.TextTestRunner()
    # runner.run(sutie)
    # 测试运行结果写到文件里
    filename = time.strftime("%Y%m%d%H%M%S")
    filepath = "d:\\study\\ecshop\\report\\" + filename  + "_testReport.html"
    result = open(filepath, 'wb')
    print(filepath)
    # result = open("testreport.html", 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=result, title='ecshop测试报告', description='测试执行情况')
    runner.run(sutie)
    result.close()
    # sub = filename+"测试报告"
    # to_list = ["wyu0430@126.com", "224138170@qq.com"]
    # send_report_email(sub, to_list, filepath)
