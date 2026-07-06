from Demo_Tricentis_Framework.pages.base_page import Basepage
from time import sleep
class RegisterPage(Basepage):
    Reg_click = ("link text","Register")
    gender=("id","gender-female")
    first_name=("id","FirstName")
    last_name=("id","LastName")
    email=("id","Email")
    password=("id","Password")
    confirm_password=("xpath","//input[@name='ConfirmPassword']")
    reg_button = ("id","register-button")
    def click_register(self):
        self.click(self.Reg_click)
    def click_gender(self):
        self.click(self.gender)
    def enter_first_name(self,first_name):
        self.enter_text(self.first_name,first_name)
    def enter_last_name(self,last_name):
        self.enter_text(self.last_name,last_name)
    def enter_email(self,email):
        self.enter_text(self.email,email)
    def enter_password(self,password):
        self.enter_text(self.password,password)
    def enter_confirm_password(self,confirm_password):
        self.enter_text(self.confirm_password,confirm_password)
    def click_login(self):
        self.click(self.Reg_click)
