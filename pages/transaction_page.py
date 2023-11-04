from core.base_page import *
from locators.transaction_page_locators import *


class TransactionsPage(BasePage):

    def count_complete_rows(self):
        rows = self.find_elements(*TransactionPageLocators.TRANSACTIONS_ROW)
        return len([row for row in rows if "Complete" in row.text])