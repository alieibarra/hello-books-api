from sys import prefix
from app import db
from flask import Blueprint, request, make_response, jsonify, abort
from app.models.task import Task
from datetime import datetime

task_bp = Blueprint("task", __name__, url_prefix="/tasks")

# Helper Function
def get_task_from_id(id):
    try:
        id = int(id)
    except:
        abort(400, {"error": "invalid id"})
    return Task.query.get_or_404(id)

#CREATE
@task_bp.route("", methods=["POST"])
def create_task():
    request_body = request.get_json()
    new_task = Task(
        title=request_body["title"],
        priority=request_body["priority"],
        dueDate=request_body["dueDate"],
    )

    db.session.add(new_task)
    db.session.commit()

    return make_response(f"New task {new_task.title} successfully created!", 201)

#READ
@task_bp.route("", methods=["GET"])
def read_all_tasks():
    tasks = Task.query.all()
    tasks_response = []
    for task in tasks:
        tasks_response.append(task.to_dict())
    return jsonify(tasks_response)

@task_bp.route("<id>", methods=["GET"])
def read_one_tasks(id):
    task = get_task_from_id(id)
    return jsonify(task.to_dict())

#UPDATE
@task_bp.route("<id>", methods=["PUT"])
def update_task(id):
    task = get_task_from_id(id)
    request_body = request.get_json()
    if "title" in request_body:
        task.title = request_body["title"]
    if "dueDate" in request_body:
        task.dueDate = request_body["dueDate"]
    if "priority" in request_body:
        task.priority = request_body["priority"]
    if "status" in request_body:
        task.status = request_body["status"]
    db.session.commit()
    return jsonify([task.to_dict(), "Update Successful"])

#DELETE
@task_bp.route("<id>", methods=["DELETE"])
def delete_task(id):
    task = get_task_from_id(id)
    db.session.delete(task)
    db.session.commit()
    return make_response("Delete successful", 200)