from flask import Blueprint

bp_web = Blueprint("web", __name__)

def create_blueprint():
    from app.web import main, upload, login, errors
    main.web.register(bp_web, url_prefix="")
    upload.web.register(bp_web)
    login.web.register(bp_web)
    return bp_web