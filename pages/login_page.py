import time

from core.base_page import *
from locators.login_locators import *
from locators.transaction_page_locators import *


class LoginPage(BasePage):

    def fill_username(self, username):
        try:
            self.send_value_to_field(username, *LoginLocators.USERNAME_FIELD)
            time.sleep(1)
        except Exception as e:
            print(f"Could not fill username field: {e}")

    def fill_password(self, password):
        try:
            self.send_value_to_field(password, *LoginLocators.PASSWORD_FIELD)
            time.sleep(1)
        except Exception as e:
            print(f"Could not fill password field: {e}")

    def login_on_startup(self, url, username, password):
        self.driver.get(url)
        self.explicitly_wait_for_element_to_be_clickable(10, *LoginLocators.USERNAME_FIELD)
        self.fill_username(username)
        self.fill_password(password)
        try:
            self.find_element(*LoginLocators.LOG_IN_BTN).click()
        except Exception as e:
            print(f"Could not click Log In Button: {e}")
        self.explicitly_wait_for_element_to_be_clickable(20, *TransactionPageLocators.LOGGED_USER_ICON)
        if self.is_element_present(*TransactionPageLocators.LOGGED_USER_ICON):
            pass
        else:
            raise Exception("Login failed")