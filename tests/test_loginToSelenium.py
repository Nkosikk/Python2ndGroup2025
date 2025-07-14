import time
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
    @pytest.mark.welcomeText
    @allure.severity(allure.severity_level.CRITICAL)
    def test_verifyWelcomeText(self, setup):
        self.driver = setup
        self.driver.get(self.dev_url)
        self.hp = HomePage(self.driver)
        self.hp.verifyWelcomeText()
        self.hp.clickLearningMaterial()
        allure.attach(self.driver.get_screenshot_as_png(), name="Home Screen",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(5)

        self.driver.quit()

    @pytest.mark.sanity
    @pytest.mark.leaning_material
    @allure.severity(allure.severity_level.CRITICAL)
    def test_clickLearningMaterial(self, setup):
        self.driver = setup
        self.driver.get(self.dev_url)
        self.hp = HomePage(self.driver)
        self.hp.verifyWelcomeText()
        self.hp.clickLearningMaterial()
        allure.attach(self.driver.get_screenshot_as_png(), name="Learning Material Page",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(5)

        self.driver.quit()
