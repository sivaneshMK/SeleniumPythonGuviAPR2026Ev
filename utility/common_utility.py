
import os
import time
from datetime import datetime, timedelta

from selenium.webdriver.common.by import By


def find_element(driver, locator, value):
    match (locator):
        case "xpath": return driver.find_element(By.XPATH, value)
        case 'id': return driver.find_element(By.ID, value)
        case 'name': return driver.find_element(By.NAME, value)
        case 'class_name': return driver.find_element(By.CLASS_NAME, value)
        case 'link_text': return driver.find_element(By.LINK_TEXT, value)
        case 'partial_link_text': return driver.find_element(By.PARTIAL_LINK_TEXT, value)
        case 'css': return driver.find_element(By.CSS_SELECTOR, value)

def take_screenshot(driver):
    os.makedirs("screenshots", exist_ok=True)
    file_name = f"screenshot_{int(time.time())}.png"
    file_path=os.path.join("screenshots",file_name)
    driver.save_screenshot(file_path)

def generate_date(no_of_days):
    current_date = datetime.now()
    new_date = current_date + timedelta(no_of_days)

    formatted_date= new_date.strftime("%a %b %d %Y")
    print(formatted_date)
