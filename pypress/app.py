import falcon

from pypress.views.runner import RunnerView, CreateTask, TaskStatusCheck, CheckEnv, SyncRunnerView

app = application = falcon.App()

runner_view = RunnerView()
app.add_route('/execute_runner', runner_view)

app.add_route('/execute_sync_runner', SyncRunnerView())

app.add_route('/status/{task_id}', TaskStatusCheck())

fib_task = CreateTask()
app.add_route('/fib', fib_task)

app.add_route('/env', CheckEnv())
