import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def test_drag_and_drop():
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options)
    driver.get("https://demo.guru99.com/test/drag_drop.html")

    actions = ActionChains(driver)
    # //a[@class='button button-orange' and contains(text(), ' 5000')]
    # (//li[@id='fourth']//a[@class='button button-orange'])[2]

    five_thousand = driver.find_element(By.XPATH, "(//li[@id='fourth']//a[@class='button button-orange'])[2]")
    # //table/tbody//td/h3[contains(text(),'DEBIT SIDE')]/following-sibling::table//td//h3[contains(text(), 'Amount')]/..//li
    #//table//h3[contains(text(),'DEBIT SIDE')]/following-sibling::table//h3[contains(text(),'Amount')]/following-sibling::div//li
    #//ol[@id='amt7']/li

    amount = driver.find_element(By.XPATH, "//ol[@id='amt7']/li")

    actions.drag_and_drop(five_thousand, amount).perform()

def test_mouse_over_actions():
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options)
    driver.get("https://www.flipkart.com/")
    time.sleep(10)
    ac = ActionChains(driver)
    # close_button = driver.find_element(By.XPATH, "//span[@role='button' and text()='✕']")
    # ac.click(close_button).perform()

    email_id_text_box = driver.find_element(By.XPATH, "//label[text()='Enter Email/Mobile number']/preceding-sibling::input")
    ac.send_keys_to_element(email_id_text_box, "9087394995").perform()

    login = driver.find_element(By.XPATH, "//span[text()='Login']/..")

    ac.move_to_element(login).perform()

    raise NoSuchElementException