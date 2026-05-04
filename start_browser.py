import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# in different packages we will be having modules and classes in same name

# to launch the browser
driver = webdriver.Chrome()

# to launch the url
driver.get("https://in.bookmyshow.com/")

# driver1= webdriver.Firefox()
# driver2 = webdriver.Edge()
#driver3 = webdriver.Safari()

print(driver.title)

print(driver.current_url)

driver.find_element(By.ID, "dummy").send_keys("Chennai")

# if any space present in between the class attribute value it is called as compound class name

driver.find_element(By.XPATH, "(//span[text()='Chennai'])[2]").click()

'''
find_element method --> return first matched element in the web page
if elements are not matched in the web page it will throw no such element exception


send_keys()--> WebElement type method, it is used to enter
text on text box, password text box, multiline text box, search box


input as string argument


'''


time.sleep(10)