from core.base_page import *
from locators.transaction_page_locators import *


class TransactionsPage(BasePage):

    def count_complete_rows(self):
        if self.is_element_present(*TransactionPageLocators.TRANSACTIONS_TABLE):
            rows = self.find_elements(*TransactionPageLocators.TRANSACTIONS_ROW)
            return len([row for row in rows if "Complete" in row.text])
<<<<<<< HEAD
        raise Exception("Transactions table was not loaded")
=======
        raise Exception("Transactions table was not loaded")
>>>>>>> bb8ff2709f39e2c9fb0a57d0f4f55d59d5f91a9c
