from authlib.integrations.flask_client import OAuth
oauth = OAuth()
from flask import Flask
from dotenv import load_dotenv
load_dotenv()
import os

def create_app():
    app = Flask(__name__)
    production = os.environ.get('PRODUCTION', False)
    app.secret_key = os.environ.get('SECRET_KEY') if production else "dev"

    oauth.init_app(app)
    
    from .routes import auth_blueprint
    app.register_blueprint(auth_blueprint)
    
    return app
