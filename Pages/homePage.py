from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    lbl_welcome_xpath = "//h2[normalize-space()='Welcome to Nkosi Online Automation BootCamp']"
    tab_learningMaterial_xpath = "//button[normalize-space()='Learning Materials']"

    def __init__(self, driver):
        self.driver = driver

    def verifyWelcomeText(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.lbl_welcome_xpath)))
        element.is_displayed()

    def clickLearningMaterial(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.tab_learningMaterial_xpath)))
        element.click()
