from sys import prefix
from app import db
from flask import Blueprint, request, make_response, jsonify, abort
from app.models.event import Event
from datetime import datetime

event_bp = Blueprint("event", __name__, url_prefix="/events")

@event_bp.route("", methods=["GET"])
def get_all_events():
    events = Event.query.all()
    
    events_response = []
    for event in events:
        events_response.append(event.to_dict())
    return jsonify(events_response)