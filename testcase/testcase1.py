import unittest
from page.cal import Count
import HTMLTestRunner
import time

class Testcase(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls):
    #     print("setUpClass")

    def setUp(self):
        print("test start")

    def test1(self):
        print('test1')

    def test_add(self):
        print("tsetadd")
        cal = Count(3,5)
        try:
            self.assertEqual(cal.add(),8,msg="预期结果是8")
            print("用例pass")
        except AssertionError:
            print("用例失败")

    def test_sheng(self):
        print("tsetsheng")
        cal = Count(3, 5)
        self.assertEqual(cal.sheng(),15,"预期结果是15")

    def tearDown(self):
        print("test end")

    # @classmethod
    # def tearDownClass(cls):
    #     print("tearDownClass")



if __name__ == '__main__':
    # unittest.main()
    sutie = unittest.TestSuite()
    sutie.addTest(Testcase("test_add"))
    sutie.addTest(Testcase("test_sheng"))
    # sutie.addTests(map(Testcase,['test1','test_add']))

    #控制台看到测试运行结果
    # runner = unittest.TextTestRunner()
    # runner.run(sutie)

    #测试运行结果写到文件里
    filename = time.strftime("%Y%m%d%H%M%S")
    filepath = "d:\\study\\ecshop\\report\\" + filename + "_testReport.html"
    result = open(filepath, 'wb')
    print(filepath)
    # result = open("testreport.html", 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=result, title='ecshop测试报告', description='测试执行情况')
    runner.run(sutie)
    result.close()

