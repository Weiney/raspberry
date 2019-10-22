from flask import Flask
from flask_bootstrap import Bootstrap
from flask_redis import FlaskRedis

redis_store = FlaskRedis()

def create_app():
    app = Flask(__name__)
    app.config.from_object("app.settings.secure")
    app.config.from_object("app.settings.setting")


    register_extension(app)
    register_blueprint(app)

    return app


def register_extension(app):
    Bootstrap(app)
    redis_store.init_app(app, decode_responses=True)

def register_blueprint(app):
    from app import web
    app.register_blueprint(web.create_blueprint())
