from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.amazon.com/")
driver.maximize_window()
driver.find_element(By.XPATH, '//*[@id="nav-link-accountList"]').click()
#driver.find_element().click()
act_title = driver.title
expected_title = "Amazon Sign-In"
if act_title == expected_title:
    print("Sing-In test passed")
else:
    print("Sign-In test failed")

