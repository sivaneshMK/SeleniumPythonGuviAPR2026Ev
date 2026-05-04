import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#synchronization
time.sleep(10)
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.TAG_NAME, "button").click()
time.sleep(20)
driver.find_element(By.LINK_TEXT, "My Info").click()
time.sleep(20)
driver.find_element(By.NAME, "firstName").click()
time.sleep(3)
driver.find_element(By.NAME, "firstName").clear()
time.sleep(5)
driver.find_element(By.NAME, "firstName").send_keys("Sivanesh")
time.sleep(10)