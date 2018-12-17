from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from webapp.config import Config


db = SQLAlchemy() # Database
bcrypt = Bcrypt() # Encyption

from webapp.main.routes import main
from webapp.errors.handlers import errors 


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
 
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app