import time
from selenium.webdriver.remote.webdriver import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# a class for general functionality
class BasePage:

    def __init__(self, driver: WebDriver = None, env=None):
        self.driver = driver
        self.env = env

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def is_element_present(self, *locator) -> bool:
        self.driver.implicitly_wait(2)
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False
        finally:
            self.driver.implicitly_wait(2)

    def send_value_to_field(self, value, *locator):
        element = self.find_element(*locator)
        element.send_keys(value)
        time.sleep(0.5)

    def explicitly_wait_for_element_to_be_clickable(
        self, wait_time: float, *locator: tuple
    ):
        try:
            WebDriverWait(self.driver, wait_time).until(
                EC.element_to_be_clickable(locator)
            )
        except Exception as e:
            print(f"failed to load element {str(e)}")