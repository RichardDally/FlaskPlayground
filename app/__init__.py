import os
from flask import Flask
from config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here

    # Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.upload import bp as upload_bp
    app.register_blueprint(upload_bp)

    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.mkdir(app.config['UPLOAD_FOLDER'])
        app.logger.info(f"[{app.config['UPLOAD_FOLDER']}] directory has been created")

    @app.route('/test/')
    def index_page():
        return '<h1>Flask Playground (not from blue print)</h1>'

    return app
