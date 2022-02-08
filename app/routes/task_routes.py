from sys import prefix
from flask import Blueprint

task_bp = Blueprint("task", __name__, url_prefix="/tasks")

@task_bp.route("", methods=["GET"])
def endpoint_name():
    testing_123 = "TASKS WILL GO HERE!"
    return testing_123