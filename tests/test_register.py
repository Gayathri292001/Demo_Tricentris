from pages.register import RegisterPage
import pytest

def test_register_page(setup_and_teardown):
    rp=RegisterPage(setup_and_teardown)
    rp.click_register()
    rp.click_gender()
    rp.enter_first_name("gayathri")
    rp.enter_last_name("venkatesan")
    rp.enter_email("gayu1234@gmail.com")
    rp.enter_password("gayu12345@1234")
    rp.enter_confirm_password("gayu12345@1234")
    rp.click_login()
