from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__)

    from .routes.event_routes import event_bp
    app.register_blueprint(event_bp)

    from .routes.task_routes import task_bp
    app.register_blueprint(task_bp)

    return app
