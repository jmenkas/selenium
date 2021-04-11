from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
driver.get('https://www.y8.com/')
 
time.sleep(10)
screenshot = driver.save_screenshot('my_screenshot.png')

driver.quit()
