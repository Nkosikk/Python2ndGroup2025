import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://ndosiautomation.vercel.app/")
element = driver.find_element(By.XPATH, "//h2[normalize-space()='Welcome to Nkosi Online Automation BootCamp']")
element.is_displayed()

Actual = element.text
Expected = "Welcome to Nkosi Online Automation BootCamp"

if Actual == Expected:
    print("Test Passed: The text is displayed correctly.")
    assert True
else:
    print(f"Test Failed: Expected '{Expected}', but got '{Actual}'.")
    assert False, f"Expected '{Expected}', but got '{Actual}'"

time.sleep(2)

# I want to click on learning material button

element = driver.find_element(By.XPATH, "//button[normalize-space()='Learning Materials']")
element.click()

# I want to click on the selenium practice button

element = driver.find_element(By.XPATH, "//button[normalize-space()='Selenium Practice']")
element.click()

# I want to input Username in username field

element = driver.find_element(By.ID, "//input[@id='username']")
element.send_keys("testuser")

# I want to input Password in password field

element = driver.find_element(By.ID, "//input[@id='password']")
element.send_keys("password123")
