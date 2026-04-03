import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
driver=webdriver.Chrome()
driver.get("https://demoqa.com/upload-download")
driver.find_element(By.XPATH,'//input[@id="uploadFile"]').send_keys(r'c:\Users\Manas\Pictures\Screenshots\Screenshot 2026-03-21 193701.png')
time.sleep(4)
driver.close()