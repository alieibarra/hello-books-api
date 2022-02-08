from sys import prefix
from flask import Blueprint

event_bp = Blueprint("event", __name__, url_prefix="/events")

@event_bp.route("", methods=["GET"])
def endpoint_name():
    testing_123 = "EVENTS WILL GO HERE!"
    return testing_123