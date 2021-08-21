from os import environ

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

SELENIUM_HOST = environ.get('SELENIUM_HOST', "http://selenium:4444/wd/hub")


def run_browser(config_browser, config_wait_time):
    if config_browser == 'chrome':
        driver = webdriver.Remote(SELENIUM_HOST, DesiredCapabilities.CHROME)
    else:
        raise Exception(f'"{config_browser}" is not a supported browser')

    # Wait implicitly for elements to be ready before attempting interactions
    driver.implicitly_wait(config_wait_time)

    # Return the driver object at the end of setup
    return driver
