from symtable import Class

import allure
import pytest

from Pages.homePage import HomePage
from utils.readProperties_Login import ReadConfig_Login


class Test_LoginToSelenium:
    dev_url = ReadConfig_Login().getDevUrl()
    username = ReadConfig_Login().getusername()
    password = ReadConfig_Login().getpassword()

    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_verifyWelcomeText(self, setup):
        self.driver = setup
        self.driver.get(self.dev_url)
        self.hp = HomePage(self.driver)
        self.hp.verifyWelcomeText()
        allure.attach(self.driver.get_screenshot_as_png(), name="Home Screen",
                      attachment_type=allure.attachment_type.PNG)

        self.driver.quit()
