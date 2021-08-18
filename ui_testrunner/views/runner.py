import json
from os import environ

import falcon
from celery.result import AsyncResult

from ui_testrunner import scenarios
from ui_testrunner.services.runner import execute_all_scenarios
from ui_testrunner.tasks import fib, execute_testrunner


class RunnerView:

    def on_post(self, req, resp):
        task = execute_testrunner.delay()
        resp.status = falcon.HTTP_200
        result = {
            'status': 'success',
            'data': {
                'task_id': task.id
            }
        }
        resp.text = json.dumps(result)

    def on_get(self, req, resp):
        task = scenarios.create_task()
        resp.status = falcon.HTTP_200
        result = {
            'status': 'success',
            'data': {
                'task_id': task.id
            },
        }
        resp.text = json.dumps(result)


class SyncRunnerView:
    def on_get(self, req, resp):
        result = execute_all_scenarios()
        resp.text = json.dumps(result)
        resp.status = falcon.HTTP_200


class CreateTask:

    def on_post(self, req, resp):
        raw_json = req.stream.read()
        result = json.loads(raw_json)
        task = fib.delay(int(result['number']))
        resp.status = falcon.HTTP_200
        result = {
            'status': 'success',
            'data': {
                'task_id': task.id
            }
        }
        resp.text = json.dumps(result)


class TaskStatusCheck(object):

    def on_get(self, req, resp, task_id):
        task_result = AsyncResult(task_id)
        result = {'status': task_result.status, 'result': task_result.result}
        resp.status = falcon.HTTP_200
        resp.text = json.dumps(result)


class CheckEnv:

    def on_get(self, req, resp):
        selenium_host = environ.get('SELENIUM_HOST')
        resp.status = falcon.HTTP_200
        resp.text = selenium_host
