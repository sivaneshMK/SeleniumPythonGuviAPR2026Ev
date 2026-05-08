import time

from selenium.webdriver.common.by import By

from utility import common_utility


def test_navigation_methods(driver):
    driver = driver
    common_utility.take_screenshot(driver)
    common_utility.find_element(driver, "xpath", "//span[text()='Forgotten password?']").click()
    print(driver.title)
    common_utility.take_screenshot(driver)
    time.sleep(3)
    driver.back()
    common_utility.take_screenshot(driver)
    time.sleep(3)
    print(driver.title)
    driver.forward()
    common_utility.take_screenshot(driver)
    print(driver.title)
    time.sleep(5)
    driver.refresh()
    common_utility.take_screenshot(driver)
    time.sleep(5)

