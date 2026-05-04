import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def get_driver():
    driver = webdriver.Chrome()
    driver.get("https://www.garnier.in/")
    yield driver
    driver.close()

@pytest.fixture(scope="function")
def get_driver_facebook():
    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com/")
    yield driver
    driver.close()
