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

learning_material_button = driver.find_element(
    By.XPATH, "//button[normalize-space()='Learning Materials']")
learning_material_button.click()
time.sleep(2)

# Verify that the user is redirected to the Learning Materials page
learning_material_page_element = driver.find_element(
    By.XPATH, "//h2[normalize-space()='Practice Assessments']")
learning_material_page_element.is_displayed()

Actual_page_title = learning_material_page_element.text
Expected_page_title = "Practice Assessments"

if Actual_page_title == Expected_page_title:
    print("Test Passed: Text Learning Materials is displayed correctly.")
    assert True

else:
    print(f"Test Failed: Text Learning Materials is not displayed correctly.")
    assert False, f"Expected '{Expected_page_title}', but got '{Actual_page_title}'"
time.sleep(2)

Selenium_Practice_Button = driver.find_element(
    By.XPATH, "//button[normalize-space()='Selenium Practice']")

Selenium_Practice_Button.click()
time.sleep(2)

Selenium_Practice_page_element = driver.find_element(
    By.XPATH, "//h2[normalize-space()='💻 Practice Area']")
Selenium_Practice_page_element.is_displayed()

Actual_practice_page_title = Selenium_Practice_page_element.text
Expected_practice_page_title = "💻 Practice Area"

if Actual_practice_page_title == Expected_practice_page_title:
    print("Test Passed: Text Selenium Practice Area is displayed correctly.")
    assert True
else:
    print(f"Test Failed: Text Selenium Practice Area is not displayed correctly.")
    assert False, f"Expected '{Expected_practice_page_title}', but got '{Actual_practice_page_title}'"
time.sleep(2)

username_input = driver.find_element(By.ID, "username")
username_input.send_keys("testuser")

Actual_username = username_input.get_attribute("value")
Expected_username = "testuser"

if Actual_username == Expected_username:
    print("Test Passed: Username is entered correctly.")
    assert True
else:
    print(f"Test Failed: Expected username '{Expected_username}', but got '{Actual_username}'.")
    assert False, f"Expected '{Expected_username}', but got '{Actual_username}'"

password_input = driver.find_element(By.ID, "password")
password_input.send_keys("password123")

Actual_password = password_input.get_attribute("value")
Expected_password = "password123"
time.sleep(2)

if Actual_password == Expected_password:
    print("Test Passed: Password is entered correctly.")
    assert True
else:
    print(f"Test Failed: Expected password '{Expected_password}', but got '{Actual_password}'.")
    assert False, f"Expected '{Expected_password}', but got '{Actual_password}'"

time.sleep(2)

login_button = driver.find_element(By.ID, "submit-btn")
login_button.click()

time.sleep(2)

practice_area_element = driver.find_element(
    By.XPATH, "//h3[normalize-space()='Welcome, testuser!']")
practice_area_element.is_displayed()

Actual_welcome_message = practice_area_element.text
Expected_welcome_message = "Welcome, testuser!"

if Actual_welcome_message == Expected_welcome_message:
    print("Test Passed: Successfully logged in and redirected to Practice Area page.")
    assert True
else:
    print(f"Test Failed: Not redirected to Practice Area page.")
    assert False, f"Expected '{Expected_welcome_message}', but got '{Actual_welcome_message}'"

time.sleep(2)



