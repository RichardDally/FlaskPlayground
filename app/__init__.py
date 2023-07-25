from flask import Flask
from config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here

    # Register blueprints here

    @app.route('/')
    def index_page():
        return '<h1>Flask Playground</h1>'

    return app