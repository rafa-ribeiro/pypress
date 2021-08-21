import json
import os

import pytest
from selenium.webdriver import Chrome, Firefox

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


CONFIG_PATH = 'tests/config.json'
DEFAULT_WAIT_TIME = 10
SUPPORTED_BROWSERS = ['chrome', 'firefox']

BASE_DIR = os.path.dirname(__file__)


@pytest.fixture(scope='session')
def config():
    # Read the JSON config file and returns it as a parsed dict

    config_path = os.path.join(os.getcwd(), 'config.json')

    with open(config_path) as config_file:
        data = json.load(config_file)
    return data


@pytest.fixture(scope='session')
def config_browser(config):
    # Validate and return the browser choice from the config data
    if 'browser' not in config:
        raise Exception('The config file does not contain "browser"')
    elif config['browser'] not in SUPPORTED_BROWSERS:
        raise Exception(f'"{config["browser"]}" is not a supported browser')
    return config['browser']


@pytest.fixture(scope='session')
def config_wait_time(config):
    # Validate and return the wait time from the config data
    return config['wait_time'] if 'wait_time' in config else DEFAULT_WAIT_TIME


@pytest.fixture
def browser(config_browser, config_wait_time):
    # Initialize WebDriver
    if config_browser == 'chrome':
        driver = Chrome("/Users/rafaelribeiro/dev_me/pypress_project/web-driver/chromedriver")
    elif config_browser == 'firefox':
        driver = Firefox()
    else:
        raise Exception(f'"{config_browser}" is not a supported browser')

    # Wait implicitly for elements to be ready before attempting interactions
    driver.implicitly_wait(config_wait_time)

    # Return the driver object at the end of setup
    yield driver

    # For cleanup, quit the driver
    driver.quit()


def run_browser(config_browser, config_wait_time):
    # Initialize WebDriver
    chromedriver_path = os.path.join(os.getcwd(), 'web-driver', 'chromedriver')

    if config_browser == 'chrome':
        # driver = Chrome("/Users/rafaelribeiro/dev_me/pypress/web-driver/chromedriver")
        driver = webdriver.Remote("http://selenium:4444/wd/hub", DesiredCapabilities.CHROME)
    elif config_browser == 'firefox':
        driver = Firefox()
    else:
        raise Exception(f'"{config_browser}" is not a supported browser')

    # Wait implicitly for elements to be ready before attempting interactions
    driver.implicitly_wait(config_wait_time)

    # Return the driver object at the end of setup
    return driver
