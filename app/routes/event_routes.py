from sys import prefix
from app import db
from flask import Blueprint, request, make_response, jsonify, abort
from app.models.event import Event
from datetime import datetime

event_bp = Blueprint("event", __name__, url_prefix="/events")

# Helper Function
def get_event_from_id(id):
    try:
        id = int(id)
    except:
        abort(400, {"error": "invalid id"})
    return Event.query.get_or_404(id)

#CREATE
@event_bp.route("", methods=["POST"])
def create_event():
    request_body = request.get_json()
    new_event = Event(
        title=request_body["title"],
        date=request_body["date"],
    )

    db.session.add(new_event)
    db.session.commit()

    return make_response(f"New task {new_event.title} successfully created!", 201)

#READ
@event_bp.route("", methods=["GET"])
def read_all_events():
    events = Event.query.all()
    
    events_response = []
    for event in events:
        events_response.append(event.to_dict())
    return jsonify(events_response)

@event_bp.route("<id>", methods=["GET"])
def read_one_event(id):
    event = get_event_from_id(id)
    return jsonify(event.to_dict())

#UPDATE
@event_bp.route("<id>", methods=["PUT"])
def update_event(id):
    event = get_event_from_id(id)
    request_body = request.get_json()
    if "title" in request_body:
        event.title = request_body["title"]
    if "date" in request_body:
        event.date = request_body["date"]
    
    db.session.commit()
    return jsonify([event.to_dict(), "Update Successful"])

#DELETE
@event_bp.route("<id>", methods=["DELETE"])
def delete_event(id):
    event = get_event_from_id(id)
    db.session.delete(event)
    db.session.commit()
    return make_response("Delete successful", 200)