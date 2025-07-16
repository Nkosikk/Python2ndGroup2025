from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class LogoutPage:

    lbl_Welcome_User_xpath = "//h3[starts-with(normalize-space(text()), 'Welcome,')]"
    btn_logout_xpath = "//button[contains(@style, 'background: linear-gradient') and contains(normalize-space(.), 'Logout')]"

    def __init__(self, driver):
        self.driver = driver

    def verifyWelcomeUsernameText(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.visibility_of_element_located((By.XPATH, self.lbl_Welcome_User_xpath)))
        element.is_displayed()

    def clickLogout(self):
        wait = WebDriverWait(self.driver, 10)
        logout_button = wait.until(ec.element_to_be_clickable((By.XPATH, self.btn_logout_xpath)))
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", logout_button)
        logout_button.click()
