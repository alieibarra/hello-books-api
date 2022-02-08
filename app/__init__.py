from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from dotenv import load_dotenv

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()

def create_app(test_config=None):
    app = Flask(__name__)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/mydash_development'

    from app.models.task import Task
    from app.models.event import Event

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes.event_routes import event_bp
    app.register_blueprint(event_bp)

    from .routes.task_routes import task_bp
    app.register_blueprint(task_bp)

    return app
