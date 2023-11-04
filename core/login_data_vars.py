import os
import json

__login_data = None

HOME_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))


def __load_login_json():
    global __login_data
    with open(HOME_PATH + os.path.sep + "login_data.json") as login_data_file:
        __login_data = json.load(login_data_file)
    return __login_data


# loads login data from file by module name an key
def get_login_data(key: str):
    if __login_data is None:
        __load_login_json()
    return __login_data[key]