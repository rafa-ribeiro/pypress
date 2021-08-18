from typing import Dict

from pages import BasePage, PageHandler


def visit_page(page):
    PageHandler.load(page)


setup_functions = {
    'visit': visit_page,
}


def execute_stage(browser, scenario: Dict) -> BasePage:
    try:
        prepare_stage = scenario.get('setup', None)
    except KeyError as err:
        print(f'There is no "visit" in setup stage:\n: {err}')
    else:
        url = prepare_stage['visit']
        page = BasePage(browser=browser, url=url)
        visit_function = setup_functions['visit']
        visit_function(page)
        return page
