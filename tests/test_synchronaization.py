import datetime
import time

from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_implicit_wait():
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options)
    driver.implicitly_wait(10)
    driver.get("https://www.flipkart.com/")
    # time.sleep(10)
    ac = ActionChains(driver)
    # close_button = driver.find_element(By.XPATH, "//span[@role='button' and text()='✕']")
    # ac.click(close_button).perform()
    time.sleep(5)
    print("applying the wait", (datetime.datetime.now()))

    try:
        email_id_text_box = driver.find_element(By.XPATH,
                                            "//label[text()='Enter Email/Mobile number']/preceding-sibling::input")
    except:
        print("after applying the wait", (datetime.datetime.now()))

    ac.send_keys_to_element(email_id_text_box, "9087394995").perform()


def test_explicit_wait():

    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options)
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.flipkart.com/")
    # time.sleep(10)
    ac = ActionChains(driver)
    # close_button = driver.find_element(By.XPATH, "//span[@role='button' and text()='✕']")
    # ac.click(close_button).perform()
    print("applying the wait", (datetime.datetime.now()))
    email_id_text_box = wait.until(EC.visibility_of_element_located((By.XPATH,"//label[text()='Enter Email/Mobile number']/preceding-sibling::input")))
    print("after applying the wait", (datetime.datetime.now()))

    ac.send_keys_to_element(email_id_text_box, "9087394995").perform()



def test_explicit_wait1():

    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options)
    wait = WebDriverWait(driver, 10)
    driver.get("https://retail.santander.co.uk/olb/app/logon/access/#/logon")
    #wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Accept all']"))).click()
    #accept_all = driver.find_element(By.XPATH, "//button[text()='Accept all']")
    wait.until(EC.visibility_of(driver.find_element(By.XPATH, "//button[text()='Accept all']"))).click()
    logon_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='submitbtn']")))

    logon_btn.click()


def test_fluent_wait():

    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options)
    wait = WebDriverWait(driver, 10, poll_frequency=2,ignored_exceptions=[NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException])
    driver.get("https://retail.santander.co.uk/olb/app/logon/access/#/logon")
    wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Accept all']"))).click()
    #accept_all = driver.find_element(By.XPATH, "//button[text()='Accept all']")
    #wait.until(EC.visibility_of(driver.find_element(By.XPATH, "//button[text()='Accept all']"))).click()
    print("popup is closed")
    #logon_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='submitbtn']")))
    wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='submitbtn']"))).click()
    #logon_btn.click()
    driver.find_element(By.XPATH, "//button[@id='submitbtn']").click()