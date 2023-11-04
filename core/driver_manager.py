from selenium import webdriver
import time
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService

# select driver
def get_driver(requested_browser):
    if requested_browser == "firefox":
        try:
            return __get_local_firefox()
        except Exception as e:
            print(f"Browser not supported, could not load driver: {e}")
    else:
        print("Browser not supported")


def __get_local_firefox():
    options = webdriver.FirefoxOptions()
    options.add_argument("--ignore-ssl-errors")
    options.add_argument("--start-maximized")
    firefox_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
    return firefox_driver
