import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
action=ActionChains(driver)
scroll=driver.find_element(By.XPATH,'//button[text()="Copy Text"]')
driver.execute_script('arguments[0].scrollIntoView()',scroll)
time.sleep(5)
point=driver.find_element(By.XPATH,'//button[text()="Point Me"]')
action.move_to_element(point).perform()
mob=driver.find_element(By.XPATH,'//a[text()="Mobiles"]')
mob.click()
time.sleep(5)
driver.close()