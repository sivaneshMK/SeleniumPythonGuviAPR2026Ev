import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def test_guvi_refer(get_driver_guvi_refer):
    driver = get_driver_guvi_refer
    language = driver.find_element(By.XPATH, "//select[@name='speakingLanguage']")
    select = Select(language)
    select.select_by_index(4)
    time.sleep(3)
    select.select_by_value("Kannada")
    time.sleep(3)
    select.select_by_visible_text("Tamil")
    time.sleep(10)

    # get all the options from the list box
    options = select.options

    for option in options:
        print(option.text)

    print(options[-1].text)

    print(select.first_selected_option.text)

    print(len(options))