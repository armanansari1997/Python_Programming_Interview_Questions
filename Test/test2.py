from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import time

driver = webdriver.Chrome(service=ChromeService('C://Users//arman.ansari_infobea//Desktop//seleniumdrivers//chromedriver.exe'))
driver.maximize_window()
driver.get('https://infobeans.darwinbox.in/user/adfs/thankyou')
driver.find_element(By.LINK_TEXT, 'LOGIN').click()
# time.sleep(678)
email = driver.find_element(By.XPATH, '//input[@aria-label="Email or phone"]')
email.send_keys('arman.ansari@infobeans.com')
# driver.find_element(By.XPATH, '//span[text()="Next"]').click()
email.send_keys(Keys.ENTER)
# time.sleep(5)
element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//input[@name="password"]')))
# //span[text()="Next"]
password = driver.find_element(By.XPATH, '//input[@name="password"]')
password.send_keys('Arman@1234')
password.send_keys(Keys.ENTER)
# driver.find_element(By.XPATH, '//span[text()="Next"]').click()
time.sleep(30)

driver.find_element(By.XPATH, "(//p[text()='Attendance'])[2]").click()
present_days = driver.find_element(By.XPATH, "//span[@id='total_present']")
print(present_days.text)

