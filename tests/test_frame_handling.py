import time

from selenium.webdriver.common.by import By


def test_handling_frame(get_driver_beej):
    driver = get_driver_beej
    time.sleep(5)
    driver.switch_to.frame(0)

    text = driver.find_element(By.XPATH, "//div[@id='playground']//p").text
    print(text)

def test_daily_thanthi_iframe(get_driver_daily_thanthi):
    driver = get_driver_daily_thanthi
    #driver.maximize_window()
    #driver.switch_to.frame(0)
    #driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[contains(@id,'google_ads_iframe')]"))
    #driver.switch_to.frame(id attribute value or name attribute value)

   # driver.find_element(By.XPATH, "//div[@id='google_image_div']").click()
    # switch back to the main HTML
    #driver.switch_to.default_content()
    # switch back to the parent
    #driver.switch_to.parent_frame()

    time.sleep(50)