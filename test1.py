import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import service
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@id='name']").send_keys("Manas ranjan")
driver.find_element(By.XPATH,'//input[@id="email"]').send_keys("manasjena366@gmail.com")
driver.find_element(By.XPATH,"//input[@id='phone']").send_keys('8249881729')
driver.find_element(By.XPATH,"//textarea[@id='textarea']").send_keys("Hyderabad,India")
driver.find_element(By.XPATH,"//input[@id='male']").click()
driver.find_element(By.XPATH,"//input[@id='female']").click()
time.sleep(2)
select=Select(driver.find_element(By.XPATH,'//select[@id="country"]'))
select.select_by_visible_text("India")
time.sleep(2)
sel1=Select(driver.find_element(By.XPATH,"//select[@id='colors']"))
sel1.select_by_visible_text('Blue')
sel1.select_by_visible_text('Red')
time.sleep(2)
sel2=Select(driver.find_element(By.XPATH,"//select[@id='animals']"))
sel2.select_by_value('cheetah')
sel2.select_by_value('deer')                                                            #this  one didnt work with visible text
sel2.select_by_value('dog')
time.sleep(1)
driver.find_element(By.XPATH,"//input[@id='monday']").click()
driver.find_element(By.XPATH,"//input[@id='tuesday']").click()
driver.find_element(By.XPATH,"//input[@id='friday']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//button[@id='alertBtn']").click()
time.sleep(1)
driver.switch_to.alert.accept()
driver.find_element(By.XPATH,'//button[@id="confirmBtn"]').click()
driver.switch_to.alert.dismiss()
time.sleep(2)
driver.find_element(By.XPATH,'//button[@id="promptBtn"]').click()
driver.switch_to.alert.send_keys('naruto uzumaki').accept()

time.sleep(2)
driver.find_element(By.XPATH,'//input[@id="Wikipedia1_wikipedia-search-input"]').send_keys('sachin')
driver.find_element(By.XPATH,'//input[@type="submit"]').click()
time.sleep(1)
res1=driver.find_elements(By.XPATH,'//div[@id="Wikipedia1_wikipedia-search-results"]')
for i in res1:
    if "Sachin Tendulkar" in i.text:
        print('success')                                                                      #i failed to make the logic
    else:
        pass
    time.sleep(3)

driver.close()