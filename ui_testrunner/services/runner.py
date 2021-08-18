from typing import Dict, List

from ui_testrunner.services.browser.services import run_browser
from ui_testrunner.validations import action
from ui_testrunner.validations import check
from ui_testrunner.validations import setup


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
    page = setup.execute_stage(browser, scenario)
    result = action.execute_stage(page, scenario)
    validations = check.execute_stage(page, scenario, result)
    return validations
