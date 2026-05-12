Tags: Regression tag, sanity, smoke, e2e

Xpath -->
XML path
We can identify the element based on the expressions
we can identify the element by using text as well
the advantages of xpath is 
we can go back forth on the web page to find element

Types Xpath
-------------
Absolute xpath
    absolute xpath starts from root node to current node
    EX: /html/body/div/div.....input
    is not recommend to use



Relative Xpath
    we can give the references for the element
based on the relationship between the elements 
and we can use own properties of element

//tagname[@propertyname='property value']
//tagname[text()='text of the element']
//tagname[contains(@propertyname, 'property value')]
//tagname[contains(text(),'text of the element')]

//phno[text()='9087394995']

following-sibling
preceding-sibling
ancestor
descendant
following
parent
child
preceding


instructions
------------
/ --> immediate child

FindElements Method
---------------------
it is used to find multiple elements

what are the elements are matched with xpath
it will featch all the elements
and it will return list of webelements

if the locator is failed find any of elements
find_elements method will return empty list


iframe:
-----------
iframe --> Inline frame
where --> to load content from different sources
Examples: ad

<html>


    <body>
        <iframe>
            <html>
                <body>
                    <iframe>
                    </iframe>
                </body>
            </html>
        </iframe>
        <iframe>
        </iframe>
    </body
</html>


Desired capabilities 
-----------------------
it will give the configuration for the browser


WebDriver methods
--------------------
switch_to
find_element
find_elements
get
quit
close
current_url
title
back
forward
maximize_window
minimize_window
refresh
current_window_handle
window_handles
implicitly_wait



WebElement method
------------------
send_keys
click
clear
is_selected
is_displayed
is_enabled
get_attribute
text

popups
-------
Alert popup 
notification popup
location popup
prompt 
calender popup

Exceptions
-------------
DetachedShadowRootException,
    ElementClickInterceptedException,
    ElementNotInteractableException,
    ElementNotSelectableException,
    ElementNotVisibleException,
    ImeActivationFailedException,
    ImeNotAvailableException,
    InsecureCertificateException,
    InvalidArgumentException,
    InvalidCookieDomainException,
    InvalidCoordinatesException,
    InvalidElementStateException,
    InvalidSelectorException,
    InvalidSessionIdException,
    InvalidSwitchToTargetException,
    JavascriptException,
    MoveTargetOutOfBoundsException,
    NoAlertPresentException,
    NoSuchAttributeException,
    NoSuchCookieException,
    NoSuchDriverException,
    NoSuchElementException,
    NoSuchFrameException,
    NoSuchShadowRootException,
    NoSuchWindowException,
    ScreenshotException,
    SessionNotCreatedException,
    StaleElementReferenceException,
    TimeoutException,
    UnableToSetCookieException,
    UnexpectedAlertPresentException,
    UnexpectedTagNameException,
    UnknownMethodException,
    WebDriverException,

Wait statements 
-----------------
implicit wait
explicit wait(WebDriver wait)
fluent wait

Synchronization
----------------
synchronize browser speed and selenium speed

Framework
------------
Pytest
POM, single tone approach
Json/Yaml -- Environment data
Requirements.txt
execute the script in different browser
report
screenshots
Datadriven
util functions
How read data from DB
API Tests




