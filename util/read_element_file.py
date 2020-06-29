from configparser import ConfigParser



class Read_element:
    def __init__(self):
        self.cf = ConfigParser()
        self.cf.read('D:\study\ecshop\config\LocalElement.ini',encoding='utf-8')

    def getItemSection(self,sectionName):
        optionDict = dict(self.cf.items(sectionName))
        return optionDict

    def getOptionValue(self,sectionName,optionName):
        value = self.cf.get(sectionName,optionName)
        return value



if __name__ == '__main__':
    test = Read_element()
    dict1 = test.getItemSection("login_element")
    print(dict1)
    value = test.getOptionValue("login_element","login_message")
    print(value)