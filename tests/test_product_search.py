import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.sanity
@pytest.mark.parametrize("search",["Cleanser", "Face Wash", "Sunscreen"])
def test_user_can_search_product(get_driver, search):
    # launch the browser
    # driver = webdriver.Chrome()
    # # launch the application
    # driver.get("https://www.garnier.in/")
    driver = get_driver
    time.sleep(10)
    driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "button.search-input__icon.newsearch").click()
    time.sleep(1)
    driver.find_element(By.CLASS_NAME,'search-input__input').send_keys(search)
    time.sleep(20)
    actual_product = driver.find_element(By.CSS_SELECTOR, "a[class='suggested-search__result']").text
    expected = search

    assert expected in actual_product, "The Searched Product is not listed"


@pytest.mark.regression
def test_user_can_view_all_products(get_driver):
    # launch the browser
    # driver = webdriver.Chrome()
    #
    # # launch the application
    # driver.get("https://www.garnier.in/")
    driver = get_driver
    time.sleep(10)
    driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "button.search-input__icon.newsearch").click()
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, 'search-input__input').send_keys("cleanser")
    time.sleep(20)

    driver.find_element(By.CSS_SELECTOR, "a[aria-label='View all search results']").click()

    actual =driver.find_element(By.CSS_SELECTOR, "h1.filters-title").text

    assert 'results for "cleanser"' in actual, "user is not getting in to products list page"