from Demo_Tricentis_Framework.pages.login_page import LoginPage
from Demo_Tricentis_Framework.utilities import read_excel
import pytest

'''@pytest.mark.smoke
def test_valid_login(setup_and_teardown):
    lp=LoginPage(setup_and_teardown)
    lp.click_login()
    lp.enter_email("gayu@2912@gmail.com")
    lp.enter_password("gayu12345")
    lp.click_login_btn()

def test_invalid_login(setup_and_teardown):
    lp=LoginPage(setup_and_teardown)
    lp.click_login()
    lp.enter_email("gayu@2912@gmail.com")
    lp.enter_password("gayu12345")
    lp.click_login_btn()'''

#3##3 read excel data
@pytest.mark.parametrize("username,password", read_excel.get_data())
def test_valid_login(setup_and_teardown,username,password):
    lp=LoginPage(setup_and_teardown)
    lp.click_login()
    lp.enter_email(username)
    lp.enter_password(password)
    lp.click_login_btn()



