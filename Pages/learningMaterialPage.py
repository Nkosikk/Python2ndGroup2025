from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class learningMaterialPage:

    lbl_practicalAssignment_xpath = "//h2[normalize-space(text())='Practice Assessments']"
    tab_seleniumPractise_xpath = "//button[normalize-space(text())='Selenium Practice']"

    def __init__(self, driver):
        self.driver = driver

    def verifyPracticalAssignmentText(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.visibility_of_element_located((By.XPATH, self.lbl_practicalAssignment_xpath)))
        element.is_displayed()

    def clickOnSeleniumPractise(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.visibility_of_element_located((By.XPATH, self.tab_seleniumPractise_xpath)))
        element.click()
