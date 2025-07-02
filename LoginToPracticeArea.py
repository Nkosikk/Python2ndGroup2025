import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait


driver=webdriver.Edge()
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

driver.find_element((By.XPATH, "//*[@id='root']/div/div[1]/nav/button[7]")).click() # Click on Learning Materials
#driver.find_element((By.XPATH, "//*[@id='root']/div/main/section/div[1]/button[5]")).click() # Click on Selenium Practice
#driver.find_element((By.XPATH, "//*[@id='root']/div/main/section/div[2]/div/div/div[2]/div/button[1]")).click() # Click on Login to Practice Area
#time.sleep(10)
#element = driver.find_element(By.XPATH, "//*[@id='root']/div/main/section/div[2]/div[1]/h2[1]")
#element.is_displayed() # Verify the Login to Practice Area text is displayed
#Actual=element.text
#Expected="Practice Area"

#if Actual == Expected:
    #print("Test Passed: The text is displayed correctly.")
    #assert True
#else:
   # print(f"Test Failed: Expected '{Expected}', but got '{Actual}'.")
    #assert False, f"Expected '{Expected}', but got '{Actual}'"

#driver.find_element((By.XPATH, "//*[@id='root']/div/main/section/div[2]/div[1]/input")).send_keys("testuser")
#driver.find_element((By.XPATH, "//*[@id='root']/div/main/section/div[2]/div[2]/input")).send_keys("testpassword")
#driver.find_element((By.XPATH, "//*[@id='root']/div/main/section/div[2]/div[3]/button")).click()
