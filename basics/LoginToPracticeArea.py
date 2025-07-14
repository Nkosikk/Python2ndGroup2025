import time

from selenium import webdriver
from selenium.webdriver.common.by import By


import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://ndosiautomation.vercel.app/")

try:
    # Check welcome text
    element = driver.find_element(By.XPATH, "//h2[normalize-space()='Welcome to Nkosi Online Automation BootCamp']")
    assert element.is_displayed()
    assert element.text == "Welcome to Nkosi Online Automation BootCamp"
    print("Test Passed: The text is displayed correctly.")

    time.sleep(2)
    # Check Practice Assessments
    learning_material_page_element = driver.find_element(By.XPATH, "//h2[normalize-space()='Practice Assessments']")
    assert learning_material_page_element.is_displayed()
    assert learning_material_page_element.text == "Practice Assessments"
    print("Test Passed: Text Learning Materials is displayed correctly.")

    time.sleep(2)
    # Click Selenium Practice
    Selenium_Practice_Button = driver.find_element(By.XPATH, "//button[normalize-space()='Selenium Practice']")
    Selenium_Practice_Button.click()
    time.sleep(2)

    # Check Practice Area
    Selenium_Practice_page_element = driver.find_element(By.XPATH, "//h2[normalize-space()='💻 Practice Area']")
    assert Selenium_Practice_page_element.is_displayed()
    assert Selenium_Practice_page_element.text == "💻 Practice Area"
    print("Test Passed: The text, Selenium Practice Area is displayed.")

    time.sleep(2)
    # Enter username
    username_input = driver.find_element(By.ID, "username")
    username_input.send_keys("testuser")
    assert username_input.get_attribute("value") == "testuser"
    print("Test Passed: Username is entered correctly.")

    # Enter password
    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("password123")
    time.sleep(2)
    assert password_input.get_attribute("value") == "password123"
    print("Test Passed: Password is entered correctly.")

    time.sleep(2)
    # Click login
    login_button = driver.find_element(By.ID, "submit-btn")
    login_button.click()
    time.sleep(2)

    # Check welcome message
    practice_area_element = driver.find_element(By.XPATH, "//h3[normalize-space()='Welcome, testuser!']")
    assert practice_area_element.is_displayed()
    assert practice_area_element.text == "Welcome, testuser!"
    print("Test Passed: Successfully logged in and redirected to Practice Area page.")

    time.sleep(2)
finally:
    driver.quit()