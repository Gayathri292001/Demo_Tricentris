import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager

@pytest.fixture
def setup_and_teardown():
    options = Options()
    options.add_argument("--headless=new")   # optional for CI
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    service = Service(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=service, options=options)
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
