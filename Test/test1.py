from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=ChromeService('C://Users//arman.ansari_infobea//Desktop//seleniumdrivers//chromedriver.exe'))
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://www.google.com')
print(driver.title)
search_bar = driver.find_element(By.NAME, "q")
time.sleep(5)
search_bar.clear()
search_bar.send_keys("getting started with python")
search_bar.send_keys(Keys.RETURN)
time.sleep(5)
print(driver.current_url)
driver.close()
