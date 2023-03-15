from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import config
from .view import home_views

db = SQLAlchemy()
migrate = Migrate()
from . import models

def create_app():
    app = Flask(__name__)
    # config
    app.config.from_object(config)

    # database
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(home_views.bp)

    return app