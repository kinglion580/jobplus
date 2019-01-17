from flask import Flask


def register_blueprints(app):
    from .handlers import front
    app.register_blueprint(front)


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    register_blueprints(app)
    return app
