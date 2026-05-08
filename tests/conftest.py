import os
import time

import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def get_driver():
    driver = webdriver.Chrome()
    driver.get("https://www.garnier.in/")
    yield driver
    driver.close()

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com/")
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def get_driver_foundit():
    driver = webdriver.Chrome()
    driver.get("https://www.foundit.in/")
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def get_driver_beej():
    driver = webdriver.Chrome()
    driver.get("https://beej.us/blog/data/drag-n-drop/")
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def get_driver_daily_thanthi():
    option = Options()
    option.add_argument("--start-maximized")
    option.add_argument("--disable-notifications")
    driver = webdriver.Chrome(option)
    driver.get("https://www.dailythanthi.com/")
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def get_driver_guvi_refer():
    option = Options()
    #option.add_argument("--headless=new")
    option.add_argument("--start-maximized")
    driver = webdriver.Chrome(option)
    driver.get("https://www.guvi.in/mlp/zen-class-refer-earn")
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            folder = "screenshots"
            os.makedirs(folder, exist_ok=True)
            file_path = os.path.join(folder, f"{item.name}_{int(time.time())}.png")
            driver.save_screenshot(file_path)

            #attach to report
            extra = getattr(report, "extra", [])
            extra.append(pytest_html.extras.image(file_path))
            report.extra = extra

            print("hooks is executed")
