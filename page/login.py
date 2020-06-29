from selenium import webdriver
from util.get_element import get_element
from util.read_element_file import Read_element

class Login:
    def __init__(self,driver):
        self.driver = driver
        self.rendcf = Read_element()
        self.loginOption = self.rendcf.getItemSection("login_element")
        self.driver.get("http://localhost:9000/ECShop_V2.7.2_UTF8_Release0604/upload66/user.php")
    # def user_login(self,user,pwd):
    #     elm_user = get_element(self.driver,"name","username")
    #     elm_user.send_keys(user)
    #     elm_pwd = get_element(self.driver,"name","password")
    #     elm_pwd.send_keys(pwd)
    #     elm_login = get_element(self.driver,"name","submit")
    #     elm_login.click()
    #     try:
    #         if get_element(self.driver,"xpath","//font[contains(@class,'f4_b')]").text == user:
    #             print("登录成功")
    #             return True
    #         else:
    #             return False
    #     except Exception as e:
    #         print(e)

    def userobject(self,user):
        method, value = self.loginOption['username'].split(">")
        elm_user = get_element(self.driver, method, value)
        try:
            elm_user.send_keys(user)
            return True
        except:
            return False



    def pwdbject(self, pwd):
        method, value = self.loginOption['password'].split(">")
        elm_user = get_element(self.driver, method, value)
        elm_user.send_keys(pwd)

    def login_button(self):
        method, value = self.loginOption['login_button'].split(">")
        elm_user = get_element(self.driver, method, value)
        elm_user.click()

    def check_login(self,user):
        method, value = self.loginOption['login_message'].split(">")

        try:
            elm_user = get_element(self.driver, method, value)
            if elm_user.text == user:
                print("登录成功")
                return True
            else:
                return False
        except Exception as e:
            return False


    def login(self,user,pwd):
        self.userobject(user)
        self.pwdbject(pwd)
        self.login_button()
        return self.check_login(user)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    test = Login(driver)
    # test.user_login("wangyu","W7548zhang")
    test.login("wangyu","W7548zhang")