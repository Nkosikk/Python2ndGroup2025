from symtable import Class

import pytest

from Pages.homePage import HomePage
from basics.LoginToPracticeArea import driver
from utils.readProperties_Login import ReadConfig_Login


class Test_LoginToSelenium:
    dev_url = ReadConfig_Login().getDevUrl()
    username = ReadConfig_Login().getusername()
    password = ReadConfig_Login().getpassword()

    @pytest.mark.sanity
    def test_verifyWelcomeText(self, setup):
        self.driver = setup
        self.hp=HomePage(self.driver)
        self.hp.verifyWelcomeText()
        self.driver.close()
