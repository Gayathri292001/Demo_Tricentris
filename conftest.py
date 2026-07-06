from selenium.webdriver import Chrome,ChromeOptions
from time import sleep
import pytest
O=ChromeOptions()
O.add_experimental_option("detach",True)# To hold the browser
@pytest.fixture
def setup_and_teardown():
    driver = Chrome(O)
    driver.maximize_window()
    driver.get("https://demowebshop.tricentis.com/")
    sleep(2)
    yield driver
    driver.quit()

### cross browser testing

'''import pytest
from selenium import webdriver
from time import sleep
@pytest.fixture(params=["chrome","edge",'firefox'])
def setup_and_teardown(request):
    parameter=request.param  #3#3 store the current parameter
    if parameter=="chrome":
        driver=webdriver.Chrome() #it will execute in chrome 1st
    elif parameter=="edge":
        driver=webdriver.Edge()
    elif parameter=="firefox":
        driver=webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://demowebshop.tricentis.com/")
    sleep(2)
    yield driver
    driver.quit()'''
## request is a built in pytest object
## whenever s fixture is parameterized the current parameter is stored inside request.parm
