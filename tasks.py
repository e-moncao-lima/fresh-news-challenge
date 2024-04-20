from robocorp.tasks import task
from src.service.controller import AutomationController

@task
def emanuel_lima():
    message = "Hello"
    message = message + " World!"
    AutomationController().run()
