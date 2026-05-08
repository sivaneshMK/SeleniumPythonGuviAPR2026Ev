import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as firefox_options
from selenium.webdriver.common.by import By


def test_geolocation():

    option= Options()
    option.add_experimental_option("detach", True)
    prefs = {"profile.default_content_setting_values.geolocation": 2}
    option.add_experimental_option("prefs",prefs)
    driver = webdriver.Chrome(option)
    driver.get("https://www.google.com/maps")
    time.sleep(20)
    driver.find_element(By.XPATH, "//button[@aria-label='Show Your Location' or @aria-label='Your Location']").click()


def test_firefox_options():

    option= firefox_options()
    option.set_preference("dom.webnotifications.enabled",False)
    option.add_argument("--private")
    driver = webdriver.Firefox(option)
    driver.get("https://www.dailythanthi.com/")

def download_selenium_language_binding(driver, language):
    driver.find_element(By.XPATH, "(//p[text()='"+language+"']/following-sibling::p[normalize-space('Stable:')])[1]/a").click()

def test_download_file():

    option= firefox_options()

    download_path = r"C:\Users\sivan\PycharmProjects\SeleniumPythonGuviAPR2026Ev\Downloads"
    option.set_preference("browser.download.folderList", 2)
    option.set_preference("browser.download.dir", download_path)
    option.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/zip")

    driver = webdriver.Firefox(option)
    driver.get("https://www.selenium.dev/downloads/")
    download_selenium_language_binding(driver, "Java")

