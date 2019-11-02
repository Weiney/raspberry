from flask import url_for, jsonify
from flask_limiter.errors import RateLimitExceeded
from werkzeug.utils import redirect

from app.libs.flask_level import PermissionException
from app.web import bp_web


@bp_web.errorhandler(PermissionException)
def handle_PermissionException(e):
    return str(e.description)


@bp_web.app_errorhandler(404)
def handle_403(e):
    return redirect(url_for("web.main+index"))


@bp_web.app_errorhandler(RateLimitExceeded)
def handle_limiter(e: RateLimitExceeded):
    """
    Flask_Limiter的错误处理函数,所有的错误都将会在这里被处理
    :param e: RateLimitExceeded,Flask-Limiter自定义的错误类型
    :return: 返回相应的json数据
    """
    response = {
        "status": "error",
        "code": e.code,
        "info": e.description
    }
    return jsonify(response)
