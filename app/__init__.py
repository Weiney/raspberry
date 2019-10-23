from flask import Flask
from flask_bootstrap import Bootstrap
from flask_redis import FlaskRedis

from app.models.base import db

redis_store = FlaskRedis()


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
    Bootstrap(app)
    redis_store.init_app(app, decode_responses=True)
    db.init_app(app)


def register_blueprint(app):
    from app import web
    app.register_blueprint(web.create_blueprint())
