import logging

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_redis import FlaskRedis

from app.libs.flask_level import FlaskLevel
from app.models.base import db

redis_store = FlaskRedis()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object("app.settings.secure")
    app.config.from_object("app.settings.setting")

    register_extension(app)
    register_blueprint(app)

    with app.app_context():
        # 在执行create_all之前要保证所有的model至少有一次引入,无法创建
        db.create_all()

    return app


def register_extension(app):
    if app.config.get("DEBUG") == False and app.config.get("ENV") == "production":
        gunicorn_logger = logging.getLogger('gunicorn.error')
        app.logger.handlers = gunicorn_logger.handlers
        app.logger.setLevel(gunicorn_logger.level)


    Bootstrap(app)
    redis_store.init_app(app, decode_responses=True)
    db.init_app(app)

    flask_level = FlaskLevel()
    flask_level.init_app(app)
    # flask_level.limited_view = "web.login+limited"

    login_manager.init_app(app)
    login_manager.login_view = "web.login+login"


def register_blueprint(app):
    from app import web
    app.register_blueprint(web.create_blueprint())
