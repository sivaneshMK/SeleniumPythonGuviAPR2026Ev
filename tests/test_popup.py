import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def test_alert_popup():
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options)
    driver.get("https://demoqa.com/alerts")
    driver.find_element(By.XPATH, "//button[@id='confirmButton']").click()
    alert = driver.switch_to.alert
    #alert.accept()
    time.sleep(3)
    print(alert.text)
    alert.dismiss()
    driver.find_element(By.XPATH, "//button[@id='promtButton']").click()
    time.sleep(3)
    prompt = driver.switch_to.alert
    prompt.send_keys("Priya dharshini")
    time.sleep(3)
    prompt.accept()

