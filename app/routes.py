from flask import Blueprint

hello_world_bp = Blueprint("hello_world", __name__)

@hello_world_bp.route('/hello-world', methods = ["Get"])
def get_hello_world():
    my_response = "Hello, World!"
    return my_response

@hello_world_bp.route('/hello-world/JSON', methods = ["Get"])
def get_hello_world_json():
    return {
        "name": "Alie", 
        "message": "I'm OOO: On Maui"
    }, 200