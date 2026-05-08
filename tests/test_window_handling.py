import time

from selenium.webdriver.common.by import By


def test_companies_are_listed(get_driver_foundit):
    # whether the companies are listed
    # how many companies are listed
    # log all the companies name
    driver = get_driver_foundit
    time.sleep(10)
    all_companies=driver.find_elements(By.XPATH, "//h2[text()='Featured Companies']/parent::div/following-sibling::div/div//img")
    print(len(all_companies))

    assert len(all_companies)>0, "The companies are not listed"

    print(len(all_companies))
    companies_title=[company.get_attribute("title") for company in all_companies]
    # for company in all_companies:
    #     companies_title.append(company.get_attribute("title"))
    #
    #print([company.get_attribute("title") for company in all_companies])
    print(companies_title)


def test_how_many_links_in_the_web_page(get_driver_facebook):
    driver = get_driver_facebook

    all_links =driver.find_elements(By.TAG_NAME, "a")
    time.sleep(10)
    all_link_text = [element.text for element in all_links]

    for link in all_link_text:
        driver.find_element(By.LINK_TEXT, link).click()
        #link.click()


def test_handling_window(get_driver_foundit):
    driver = get_driver_foundit
    time.sleep(10)
    # getting all the company list
    all_companies = driver.find_elements(By.XPATH,
                                         "//h2[text()='Featured Companies']/parent::div/following-sibling::div/div//img")
    #clicking on first 3 companies
    for i in range(3):
        company = all_companies[i]
        # getting company title attribute
        print(company.get_attribute("title"))
        company.click()

    #printing the parent window title
    print(driver.title)

    # current window reference
    parent_window = driver.current_window_handle

    # Getting all windows reference including parent window
    all_windows = driver.window_handles

    # switch to the particular window
    driver.switch_to.window(all_windows[3])

    # getting current window title
    print(driver.title)

    # close the current window
    driver.close()
    time.sleep(5)


def  test_current_window_handle(get_driver_foundit):
    driver = get_driver_foundit
    time.sleep(10)
    # getting all the company list
    all_companies = driver.find_elements(By.XPATH,
                                         "//h2[text()='Featured Companies']/parent::div/following-sibling::div/div//img")
    # clicking on first 3 companies
    for i in range(3):
        company = all_companies[i]
        # getting company title attribute
        print(company.get_attribute("title"))
        company.click()

    # printing the parent window title
    print(driver.title)

    # current window reference
    parent_window = driver.current_window_handle

    # Getting all windows reference including parent window
    all_windows = driver.window_handles

    #driver.switch_to.window(all_windows[0])

    for window in all_windows:

        if parent_window != window:
            driver.switch_to.window(window)
            print(driver.title)
            driver.close()
        else:
            print("both window reference are same")


