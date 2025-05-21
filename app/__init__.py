from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI

    db.init_app(app)

    # Import routes and models here to avoid circular import
    from app.routes import main
    from app import models

    app.register_blueprint(main)

    return app
