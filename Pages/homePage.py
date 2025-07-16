from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class HomePage:

    lbl_welcome_xpath="//h2[normalize-space()='Welcome to Nkosi Online Automation BootCamp']"
    tab_learning_material_xpath= "//button[normalize-space(text())='Learning Materials']"

    def __init__(self, driver):
        self.driver = driver

    def verifyWelcomeText(self):
        wait=WebDriverWait(self.driver, 10)
        element = wait.until(ec.visibility_of_element_located((By.XPATH, self.lbl_welcome_xpath)))
        element.is_displayed()

    def clickLearningMaterial(self):
        wait=WebDriverWait(self.driver, 10)
        element = wait.until(ec.visibility_of_element_located((By.XPATH, self.tab_learning_material_xpath)))
        element.click()