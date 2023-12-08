import pytest
from core import load_config
from core.load_config import get_config
from core.driver_manager import get_driver
from pages.login_page import LoginPage
from core.login_data_vars import *
import logging

logging.basicConfig(level=logging.DEBUG)
# enables selecting browser (currently FF only)
def pytest_addoption(parser):
    parser.addoption("--bro", action="store", default=None, help="please choose browser: --bro=<browser>")
    parser.addoption("--env", action="store", default=None, help="Please choose environment as a must param : --env")


# enables selecting test environment
@pytest.fixture(scope="session")
def env(request):
    env = request.config.getoption("--env")
    if not env:
        with open(os.path.join(load_config.HOME_PATH, "tests", "config.json")) as config:
            config_data = json.load(config)
            env = config_data["env"]
    return env


#load test data
@pytest.fixture(scope="session")
def data(env):
    data_files = {
        "dev": "test_data.json",
    }
    with open(os.path.join(load_config.HOME_PATH, "data", data_files[env]), encoding="utf-8") as data_file:
        data = json.load(data_file)
    return data


# set driver
@pytest.fixture(scope="session")
def driver(request):
    if request.config.getoption("--bro") is not None:
        config_browser = request.config.getoption("--bro")
    else:
        config_browser = get_config("browser")
    driver = get_driver(config_browser)
    yield driver
    driver.quit()


# setup all tests
@pytest.fixture(scope="class")
def test_setup(request, data, driver, env):
    request.cls.data = data
    request.cls.driver = driver
    request.cls.env = env


# perform login
@pytest.fixture(scope="class")
def login_setup(driver, data):
    login = LoginPage(driver)
    yield login.login_on_startup(data["url"], get_login_data("username"), get_login_data("password"))