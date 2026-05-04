import time

from selenium.webdriver.common.by import By

def select_day(driver, day):
    driver.find_element(By.XPATH, "//div[@aria-label='Select day' and @role='combobox']").click()
    driver.find_element(By.XPATH, "//div[@role='option']//div[text()='"+day+"']").click()
    print("Day "+ day+" is Selected")

def test_user_is_able_to_create_account(get_driver_facebook):
    driver = get_driver_facebook
    driver.find_element(By.LINK_TEXT, "Create new account").click()
    create_new_account_title = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div[2]/span/span").text
    assert "Create an account to connect with friends, family and communities of people who share your interests." == create_new_account_title, "We are not in the signup page"
    driver.find_element(By.XPATH, "(//input[@type='text'])[1]").send_keys("Shunmuga")
    driver.find_element(By.XPATH, "//label[text()='Surname']/preceding-sibling::input").send_keys("Priya")
    select_day(driver, "30")
    time.sleep(5)


