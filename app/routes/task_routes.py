from sys import prefix
from app import db
from flask import Blueprint, request, make_response, jsonify, abort
from app.models.task import Task
from datetime import datetime

task_bp = Blueprint("task", __name__, url_prefix="/tasks")


@task_bp.route("", methods=["GET"])
def get_all_tasks():
    tasks = Task.query.all()
    tasks_response = []
    for task in tasks:
        tasks_response.append(task.to_dict())
    return jsonify(tasks_response)