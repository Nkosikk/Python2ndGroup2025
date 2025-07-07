import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://ndosiautomation.vercel.app/")
element = driver.find_element(By.XPATH, "//h2[normalize-space()='Welcome to Nkosi Online Automation BootCamp']")
element.is_displayed()

Actual=element.text
Expected="Welcome to Nkosi Online Automation BootCamp"

if Actual == Expected:
    print("Test Passed: The text is displayed correctly.")
    assert True
else:
    print(f"Test Failed: Expected '{Expected}', but got '{Actual}'.")
    assert False, f"Expected '{Expected}', but got '{Actual}'"

time.sleep(2)


