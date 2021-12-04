import time
from typing import Dict

from selenium.webdriver.common.by import By

from pages import PageHandler, BasePage

IDENTIFIERS_MAP = {
    'TAG_NAME': By.TAG_NAME,
    'ID': By.ID,
    'CLASS': By.CLASS_NAME,
    'CSS_SELECTOR': By.CSS_SELECTOR
}


def collect_elements(page, param, *args, **kwargs):
    key, identifier = param.split('=')
    by = IDENTIFIERS_MAP[key]
    elements = PageHandler.find_elements(page=page, by=by, identifier=identifier)
    return elements


def wait_for(page, time_in_seconds, *args, **kwargs):
    time.sleep(time_in_seconds)
    return None


available_functions = {
    'collect_elements': collect_elements,  # type: ignore
    'wait_for': wait_for,  # type: ignore
}


def execute_stage(page: BasePage, scenario: Dict) -> object:
    action_stage = scenario.get('action', None)
    result = None
    if action_stage:
        for key, value in action_stage.items():
            func_to_exec = available_functions[key]
            result = func_to_exec(page, value, result)

    return result
