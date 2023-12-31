from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
import logging


def get_driver(requested_browser):
    if requested_browser == "firefox":
        try:
            return __get_local_firefox()
        except Exception as e:
            print(f"Browser not supported, could not load driver: {e}")
    else:
        print("Browser not supported")


def __get_local_firefox():
    logging.basicConfig(level=logging.DEBUG)
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")
    options.add_argument("--start-maximized")
    firefox_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
    print(f"this is firefox driver: {firefox_driver}")
    return firefox_driver

