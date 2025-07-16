from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class learningMaterialPage:

    lbl_practicalAssignment_xpath = "//h2[normalize-space(text())='Practice Assessments']"

    def __init__(self, driver):
        self.driver = driver

    def verifyPracticalAssignmentText(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.visibility_of_element_located((By.XPATH, self.lbl_practicalAssignment_xpath)))
        element.is_displayed()



