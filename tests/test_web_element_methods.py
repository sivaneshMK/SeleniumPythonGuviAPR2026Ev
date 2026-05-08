import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_web_element_methods():
    driver = webdriver.Firefox()

    driver.get("https://www.makemytrip.com/")
    driver.maximize_window()
    time.sleep(5)
    driver.find_element(By.XPATH, "//span[@class='commonModal__close']").click()
    class_value = driver.find_element(By.XPATH, "//li[@data-cy='oneWayTrip']").get_attribute("class")
    assert class_value =="selected", "the radio button is not selected"

def test_is_selected_method():
    driver = webdriver.Firefox()

    driver.get("https://v2.zenclass.in/login")
    driver.maximize_window()
    time.sleep(5)
    remember_me_checkbox = driver.find_element(By.XPATH, "//input[@aria-label='Checkbox demo']")
    ##flag = driver.find_element(By.XPATH, "//input[@aria-label='Checkbox demo']").is_selected()

    flag = remember_me_checkbox.is_selected()
    if flag:
        print("check box is selected")
    else :
        print("check box is not selected")
        #driver.find_element(By.XPATH, "//input[@aria-label='Checkbox demo']")
        remember_me_checkbox.click()

def test_is_enabled():
    driver = webdriver.Firefox()

    driver.get("https://retail.santander.co.uk/olb/app/logon/access/#/logon")
    driver.maximize_window()
    time.sleep(5)
    alert_popup = driver.find_element(By.XPATH, "//div[@role='alertdialog']")
    if alert_popup.is_displayed():
        print("the alert is displayed")
        driver.find_element(By.XPATH, "//button[text()='Accept all']").click()

    login_button = driver.find_element(By.XPATH, "//button[@id='submitbtn']")

    assert login_button.is_enabled() == False, "The login button is enabled when the form is empty"