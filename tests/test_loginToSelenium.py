import time

import allure
import pytest

from Pages.homePage import HomePage
from Pages.learningMaterialPage import learningMaterialPage
from Pages.logoutPage import LogoutPage
from Pages.seleniumPracticePage import SeleniumPracticePage
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
        allure.attach(self.driver.get_screenshot_as_png(), name="Home Screen",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(3)

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
        time.sleep(3)

        self.driver.quit()

    @pytest.mark.sanity
    @pytest.mark.leaning_material_Part2
    @allure.severity(allure.severity_level.CRITICAL)
    def test_verifyPracticalAssignmentText(self, setup):
        self.driver = setup
        self.driver.get(self.dev_url)
        self.hp = HomePage(self.driver)
        self.hp.verifyWelcomeText()
        self.hp.clickLearningMaterial()
        self.lm = learningMaterialPage(self.driver)
        self.lm.verifyPracticalAssignmentText()
        allure.attach(self.driver.get_screenshot_as_png(), name="Verifying Learning Material Page",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(3)

        self.driver.quit()

    @pytest.mark.sanity
    @pytest.mark.selenium_practise
    @allure.severity(allure.severity_level.CRITICAL)
    def test_clickOnSeleniumPractise(self, setup):
        self.driver = setup
        self.driver.get(self.dev_url)
        self.hp = HomePage(self.driver)
        self.hp.verifyWelcomeText()
        self.hp.clickLearningMaterial()
        self.lm = learningMaterialPage(self.driver)
        self.lm.verifyPracticalAssignmentText()
        self.lm.clickOnSeleniumPractise()
        allure.attach(self.driver.get_screenshot_as_png(), name="Click on Selenium Practise tab",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(3)

        self.driver.quit()

    @pytest.mark.sanity
    @pytest.mark.selenium_practise_Part2
    @allure.severity(allure.severity_level.CRITICAL)
    def test_verifyPracticeAreasText(self, setup):
        self.driver = setup
        self.driver.get(self.dev_url)
        self.hp = HomePage(self.driver)
        self.hp.verifyWelcomeText()
        self.hp.clickLearningMaterial()
        self.lm = learningMaterialPage(self.driver)
        self.lm.verifyPracticalAssignmentText()
        self.lm.clickOnSeleniumPractise()
        self.sp = SeleniumPracticePage(self.driver)
        self.sp.verifyPracticeAreasText()
        allure.attach(self.driver.get_screenshot_as_png(), name="Practice Areas Page",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(3)

        self.driver.quit()

    @pytest.mark.sanity
    @pytest.mark.leaning_material_Part3
    @allure.severity(allure.severity_level.CRITICAL)
    def test_verifyLoginToYourAccountText(self, setup):
        self.driver = setup
        self.driver.get(self.dev_url)
        self.hp = HomePage(self.driver)
        self.hp.verifyWelcomeText()
        self.hp.clickLearningMaterial()
        self.lm = learningMaterialPage(self.driver)
        self.lm.verifyPracticalAssignmentText()
        self.lm.clickOnSeleniumPractise()
        self.sp = SeleniumPracticePage(self.driver)
        self.sp.verifyPracticeAreasText()
        self.sp.verifyLoginToYourAccountText()
        time.sleep(3)
        allure.attach(self.driver.get_screenshot_as_png(), name="Login to Your Account Page",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(3)

        self.driver.quit()

    @pytest.mark.sanity
    @pytest.mark.username
    @allure.severity(allure.severity_level.CRITICAL)
    def test_enterUsername(self, setup):
        self.driver = setup
        self.driver.get(self.dev_url)
        self.hp = HomePage(self.driver)
        self.hp.verifyWelcomeText()
        self.hp.clickLearningMaterial()
        self.lm = learningMaterialPage(self.driver)
        self.lm.verifyPracticalAssignmentText()
        self.lm.clickOnSeleniumPractise()
        self.sp = SeleniumPracticePage(self.driver)
        self.sp.verifyPracticeAreasText()
        self.sp.verifyLoginToYourAccountText()
        self.sp.enterUsername(self.username)
        time.sleep(3)
        allure.attach(self.driver.get_screenshot_as_png(), name="Username Entered",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(3)

        self.driver.quit()

    @pytest.mark.sanity
    @pytest.mark.password
    @allure.severity(allure.severity_level.CRITICAL)
    def test_enterPassword(self, setup):
        self.driver = setup
        self.driver.get(self.dev_url)
        self.hp = HomePage(self.driver)
        self.hp.verifyWelcomeText()
        self.hp.clickLearningMaterial()
        self.lm = learningMaterialPage(self.driver)
        self.lm.verifyPracticalAssignmentText()
        self.lm.clickOnSeleniumPractise()
        self.sp = SeleniumPracticePage(self.driver)
        self.sp.verifyPracticeAreasText()
        self.sp.verifyLoginToYourAccountText()
        self.sp.enterUsername(self.username)
        self.sp.enterPassword(self.password)
        allure.attach(self.driver.get_screenshot_as_png(), name="Password Entered",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(3)

        self.driver.quit()

    @pytest.mark.sanity
    @pytest.mark.Login_Button_Click
    @allure.severity(allure.severity_level.CRITICAL)
    def test_clickLogin(self, setup):
        self.driver = setup
        self.driver.get(self.dev_url)
        self.hp = HomePage(self.driver)
        self.hp.verifyWelcomeText()
        self.hp.clickLearningMaterial()
        self.lm = learningMaterialPage(self.driver)
        self.lm.verifyPracticalAssignmentText()
        self.lm.clickOnSeleniumPractise()
        self.sp = SeleniumPracticePage(self.driver)
        self.sp.verifyPracticeAreasText()
        self.sp.verifyLoginToYourAccountText()
        self.sp.enterUsername(self.username)
        self.sp.enterPassword(self.password)
        self.sp.clickLogin()
        time.sleep(3)
        allure.attach(self.driver.get_screenshot_as_png(), name="Click Login Button",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(3)

        self.driver.quit()

    @pytest.mark.sanity
    @pytest.mark.welcome_username_text
    @allure.severity(allure.severity_level.CRITICAL)
    def test_verifyWelcomeUsernameText(self, setup):
        self.driver = setup
        self.driver.get(self.dev_url)
        self.hp = HomePage(self.driver)
        self.hp.verifyWelcomeText()
        self.hp.clickLearningMaterial()
        self.lm = learningMaterialPage(self.driver)
        self.lm.verifyPracticalAssignmentText()
        self.lm.clickOnSeleniumPractise()
        self.sp = SeleniumPracticePage(self.driver)
        self.sp.verifyPracticeAreasText()
        self.sp.verifyLoginToYourAccountText()
        self.sp.enterUsername(self.username)
        self.sp.enterPassword(self.password)
        self.sp.clickLogin()
        self.lo = LogoutPage(self.driver)
        self.lo.verifyWelcomeUsernameText()
        allure.attach(self.driver.get_screenshot_as_png(), name="Welcome Username Text",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(3)

        self.driver.quit()


    @pytest.mark.sanity
    @pytest.mark.logout_button_click
    @allure.severity(allure.severity_level.CRITICAL)
    def test_clickLogout(self, setup):
        self.driver = setup
        self.driver.get(self.dev_url)
        self.hp = HomePage(self.driver)
        self.hp.verifyWelcomeText()
        self.hp.clickLearningMaterial()
        self.lm = learningMaterialPage(self.driver)
        self.lm.verifyPracticalAssignmentText()
        self.lm.clickOnSeleniumPractise()
        self.sp = SeleniumPracticePage(self.driver)
        self.sp.verifyPracticeAreasText()
        self.sp.verifyLoginToYourAccountText()
        self.sp.enterUsername(self.username)
        self.sp.enterPassword(self.password)
        self.sp.clickLogin()
        self.lo = LogoutPage(self.driver)
        self.lo.verifyWelcomeUsernameText()
        self.lo.clickLogout()
        allure.attach(self.driver.get_screenshot_as_png(), name="Logout Button Clicked",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(3)

        self.driver.quit()


