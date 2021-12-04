import falcon

from pypress.views.runner import TestRunnerView, TaskStatusCheck, CheckEnv, SyncTestRunnerView, HealthCheckView

app = application = falcon.App()

app.add_route('/env', CheckEnv())

# Execute tests scenarios
runner_view = TestRunnerView()
app.add_route('/execute_runner', runner_view)
app.add_route('/execute_sync_runner', SyncTestRunnerView())
app.add_route('/task/{task_id}/status', TaskStatusCheck())

# Healthy check
app.add_route('/status', HealthCheckView())
