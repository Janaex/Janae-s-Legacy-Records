from flask import Flask
from flask_sqlalchemy import sqlalchemy
from .config import Config
from flask_cors import CORS



def create_app():
    app = Flask(__name__)
    
    app.config.from_object('config.Config')
    
    with app.app_context():
        # Import routes
        from . import routes
    
    return app