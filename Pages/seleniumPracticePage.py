from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class SeleniumPracticePage:
    lbl_practiceAreas_xpath = "//h2[normalize-space(text())='💻 Practice Area']"
    lbl_LoginToYourAccount_xpath = "//h3[normalize-space(text())='🔑 Login to Your Account']"
    txt_username_xpath = "//input[@name='username']"
    txt_password_xpath = "//input[@name='password']"
    btn_login_xpath = "//button[@id='submit-btn' and @type='submit' and contains(text(), 'Login')]"

    def __init__(self, driver):
        self.driver = driver

    def verifyPracticeAreasText(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.visibility_of_element_located((By.XPATH, self.lbl_practiceAreas_xpath)))
        element.is_displayed()

    def verifyLoginToYourAccountText(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.visibility_of_element_located((By.XPATH, self.lbl_LoginToYourAccount_xpath)))
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
        element.is_displayed()

    def enterUsername(self, username):
        wait = WebDriverWait(self.driver, 10)
        username_field = wait.until(ec.visibility_of_element_located((By.XPATH, self.txt_username_xpath)))
        username_field.clear()
        username_field.send_keys(username)

    def enterPassword(self, password):
        wait = WebDriverWait(self.driver, 10)
        password_field = wait.until(ec.visibility_of_element_located((By.XPATH, self.txt_password_xpath)))
        password_field.clear()
        password_field.send_keys(password)

    def clickLogin(self):
        wait = WebDriverWait(self.driver, 10)
        login_button = wait.until(ec.element_to_be_clickable((By.XPATH, self.btn_login_xpath)))
        login_button.click()
