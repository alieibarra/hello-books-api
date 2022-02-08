from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()

def create_app(test_config=None):
    app = Flask(__name__)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')

    from app.models.task import Task
    from app.models.event import Event

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes.event_routes import event_bp
    app.register_blueprint(event_bp)

    from .routes.task_routes import task_bp
    app.register_blueprint(task_bp)

    return app
