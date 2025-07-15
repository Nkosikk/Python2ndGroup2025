from symtable import Class

from utils.readProperties_Login import ReadConfig_Login


class Test_LoginToSelenium:
    dev_url = ReadConfig_Login().getDevUrl()
    username = ReadConfig_Login().getusername()
    print(dev_url)
    print(username)
    # def test_login_to_selenium(self):
    #     print(self.dev_url)
