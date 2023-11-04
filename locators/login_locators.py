from selenium.webdriver.common.by import By


class LoginLocators:
    USERNAME_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")
    LOG_IN_BTN = (By.ID, "log-in")