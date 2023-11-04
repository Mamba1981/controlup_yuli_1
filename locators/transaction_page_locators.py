from selenium.webdriver.common.by import By


class TransactionPageLocators:
    TRANSACTIONS_TABLE = (By.CLASS_NAME, "table-responsive")
    TRANSACTIONS_ROW = (By.XPATH, "//div[@class='table-responsive']//tr")
    LOGGED_USER_ICON = (By.CLASS_NAME, "logged-user-w")