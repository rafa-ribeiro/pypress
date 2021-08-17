import time
from typing import Dict, List

from selenium.webdriver.common.by import By

from pages import PageHandler, BasePage
from ui_testrunner.services.browser.services import run_browser

IDENTIFIERS_MAP = {
    'TAG_NAME': By.TAG_NAME,
    'ID': By.ID,
    'CLASS': By.CLASS_NAME,
    'CSS_SELECTOR': By.CSS_SELECTOR
}


def load_page(page):
    PageHandler.load(page)


def collect_elements(page, param, *args, **kwargs):
    key, identifier = param.split('=')
    by = IDENTIFIERS_MAP[key]
    elements = PageHandler.find_elements(page=page, by=by, identifier=identifier)
    return elements


def count_elements_equal_to(page, to_check, expected_count, *args, **kwargs):
    result = {
        'count_elements_equal_to': len(to_check) == expected_count,
        'page_under_test': page.url,
        'calculated_count': len(to_check),
        'expected_count': expected_count,
    }
    return result


def wait_for(page, time_in_seconds, *args, **kwargs):
    time.sleep(time_in_seconds)
    return None


available_functions = {
    'on_page': load_page,
    'collect_elements': collect_elements,
    'count_elements_equal_to': count_elements_equal_to,
    'wait_for': wait_for,
}


class MockBrowser(object):

    def __init__(self):
        pass


def execute_all_scenarios(scenarios: List):
    browser = run_browser(config_browser='chrome', config_wait_time=10)
    results = list()

    try:
        for scenario in scenarios:
            validations = execute_scenario(browser=browser, scenario=scenario)
            results.extend(validations)

        return {
            'results': results,
        }
    finally:
        browser.quit()


def execute_scenario(browser, scenario: Dict):
    page = execute_prepare_stage(browser, scenario)
    result = execute_action_stage(page, scenario)
    validations = execute_check_stage(page, scenario, result)
    return validations


def execute_prepare_stage(browser, scenario: Dict) -> BasePage:
    try:
        prepare_stage = scenario.get('prepare', None)
    except KeyError as err:
        print(f'There is no "on_page" in prepare stage:\n: {err}')
    else:
        url = prepare_stage['on_page']
        page = BasePage(browser=browser, url=url)
        on_page_function = available_functions['on_page']
        on_page_function(page)
        return page


def execute_action_stage(page: BasePage, scenario: Dict) -> object:
    action_stage = scenario.get('action', None)
    result = None
    if action_stage:
        for key, value in action_stage.items():
            func_to_exec = available_functions[key]
            result = func_to_exec(page, value, result)

    return result


def execute_check_stage(page: BasePage, scenario: Dict, result) -> object:
    checks_results = list()
    check_step = scenario.get('check', None)
    if check_step:
        for key, value in check_step.items():
            func_to_exec = available_functions[key]
            check_result = func_to_exec(page, result, value)
            checks_results.append(check_result)
    return checks_results
