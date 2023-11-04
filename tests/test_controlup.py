import pytest
from pages.transaction_page import *


@pytest.mark.usefixtures("test_setup", "login_setup")
class TestTable:
    def test_successful_rows (self):
        page = TransactionsPage(self.driver)
        assert page.count_complete_rows() == 2
