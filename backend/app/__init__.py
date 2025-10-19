import os
from flask import Flask
from flask_cors import CORS
from .config import Config
from .extensions import db, migrate, jwt
from .routes import register_routes

def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(Config)
    
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    
    CORS(app, resources={r"/*": {"origins": "*"}})
    
    register_routes(app)
    
    return app