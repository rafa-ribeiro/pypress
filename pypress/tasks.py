import os
from time import sleep

import celery

from pages.vivadecora.decoracao import DecoracaoPage
from pypress.services.browser.services import run_browser
from pypress.services.runner import execute_all_scenarios

CELERY_BROKER = os.environ.get('CELERY_BROKER')
CELERY_BACKEND = os.environ.get('CELERY_BACKEND')

app = celery.Celery('tasks', broker=CELERY_BROKER, backend=CELERY_BACKEND)


@app.task
def fib(n):
    sleep(2)  # simulate slow computation
    if n < 0:
        return []
    elif n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    else:
        results = fib(n - 1)
        results.append(results[-1] + results[-2])
        return results


@app.task
def execute_testrunner():
    browser = run_browser(config_browser='chrome', config_wait_time=10)

    try:
        decoracao_page = DecoracaoPage(browser=browser)
        decoracao_page.load()

        data = decoracao_page.all_h1()
        result = {
            'has_only_one_h1': len(data) == 1,
            'page': decoracao_page.URL
        }
        return result
    finally:
        browser.quit()


@app.task
def execute_all_validations(scenarios):
    try:
        results = execute_all_scenarios(scenarios=scenarios)
    except Exception as err:
        results = {
            'status': 'Error',
            'messagge': str(err),
        }
    return results
