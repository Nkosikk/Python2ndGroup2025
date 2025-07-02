import time
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from selenium.webdriver.support.wait import WebDriverWait

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

driver.find_element(By.XPATH, "//nav//button[normalize-space(text())='Learning Materials']").click() # Click on Learning Materials
driver.find_element(By.XPATH, "//*[@id='root']/div/main/section/div[1]/button[5]").click() # Click on Selenium Practice
driver.find_element(By.XPATH, "/html/body/div/div/main/section/div[2]/div/div/div[1]/div/p") # Click on Login to Practice Area
time.sleep(20)
element = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.XPATH, "//button[normalize-space(text())='Login']"))
)
#element.click()
#element.is_displayed() # Verify the Login to Practice Area text is displayed
#Actual=element.text
#Expected="Practice Area"

#if Actual == Expected:
   # print("Test Passed: The text is displayed correctly.")
    #assert True
#else:
    #print(f"Test Failed: Expected '{Expected}', but got '{Actual}'.")
    #assert False, f"Expected '{Expected}', but got '{Actual}'"

driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("testuser")
#driver.find_element((By.XPATH, "//*[@id='root']/div/main/section/div[2]/div[2]/input")).send_keys("testpassword")
#driver.find_element((By.XPATH, "//*[@id='root']/div/main/section/div[2]/div[3]/button")).click()
