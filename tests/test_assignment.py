from selenium import webdriver
from selenium.webdriver.common.by import By

def test_facebook_language_selection():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(30)

    driver.get("https://www.facebook.com/")
    #Click More languages and get the language list
    driver.find_element(By.XPATH, '(//div/div[8])[1]').click()
    all_languages_element = driver.find_elements(By.XPATH, '//div[text()="Af-Soomaali"]/../../../..//div/span/span/div')

    all_languages_text_list = [el.text for el in all_languages_element]
    for language in all_languages_text_list:
        #Choose the language
        if language in ["English (UK)", "العربية", "پښتو", "فارسی", "کوردیی ناوەندی", "ܣܘܪܝܝܐ"]:
            continue
        xpath = f'//*[text()="{language}"]'
        print("xpath is: ", xpath)
        driver.find_element(By.XPATH, xpath ).click()
        #Assert the language change
        selected_language_text = driver.find_element(By.XPATH, "(//div/div[8]/../div[1])[1]").text
        assert selected_language_text == language
        #click more languages again
        driver.find_element(By.XPATH, '(//div/div[8])[1]').click()