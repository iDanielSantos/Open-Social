from flask import Flask
from .models import bcrypt

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    with app.app_context():
        bcrypt.init_app(app)

        return app