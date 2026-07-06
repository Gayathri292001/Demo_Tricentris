from time import sleep
from pages.base_page import Basepage   ## import login_page
class LoginPage(Basepage):
    login_link =("link text","Log in")
    email= ("id","Email")
    password = ("id","Password")
    login_btn = ("xpath","//input[@value='Log in']")

    def click_login(self):
        self.click(self.login_link)
    def enter_email(self,email):
        self.enter_text(self.email,email)
    def enter_password(self,password):
        self.enter_text(self.password,password)
    def click_login_btn(self):
        self.click(self.login_btn)
