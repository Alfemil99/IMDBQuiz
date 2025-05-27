from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Secret key required for sessions
    app.config["SECRET_KEY"] = "super-secret-key-change-this"

    # Database URI (PostgreSQL or SQLite)
    app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    # Import routes and models to register with the app
    from app.routes import main
    from app import models

    app.register_blueprint(main)

    return app
