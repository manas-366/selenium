from selenium import webdriver
from selenium.webdriver.chrome.service import service
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.find_element(By.XPATH,"//button[text()='New Tab']").click()
window_handle=driver.window_handles
driver.switch_to.window(window_handle[1])
assert "SDET-QA Blog" in driver.title
print("success")
driver.close()