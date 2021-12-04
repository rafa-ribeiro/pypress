import json
from os import environ

import falcon
from celery.result import AsyncResult

from pypress import scenarios
from pypress.scenarios import SCENARIOS_LIST
from pypress.services.runner import execute_all_scenarios


class TestRunnerView:

    def on_put(self, req, resp):
        task = scenarios.create_task()
        resp.status = falcon.HTTP_200
        result = {
            'status': 'success',
            'data': {
                'task_id': task.id
            },
        }
        resp.text = json.dumps(result)


class SyncTestRunnerView:
    def on_get(self, req, resp):
        result = execute_all_scenarios(scenarios=SCENARIOS_LIST)
        resp.text = json.dumps(result)
        resp.status = falcon.HTTP_200


class TaskStatusCheck(object):

    def on_get(self, req, resp, task_id):
        task_result = AsyncResult(task_id)
        result = {'status': task_result.status, 'result': task_result.result}
        resp.status = falcon.HTTP_200
        resp.text = json.dumps(result)


class CheckEnv:

    def on_get(self, req, resp):
        selenium_host = environ.get('SELENIUM_HOST', None)
        selenium_host = 'Selenium running locally' if selenium_host else 'Selenium running on container.'
        resp.status = falcon.HTTP_200
        resp.text = selenium_host


class HealthCheckView:

    def on_get(self, req, resp):
        resp.text = 'Pypress is working!'
        resp.status = falcon.HTTP_200
