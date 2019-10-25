from flask import url_for
from werkzeug.utils import redirect

from app.libs.flask_level import PermissionException
from app.web import bp_web


@bp_web.errorhandler(PermissionException)
def handle_PermissionException(e):
    return str(e.description)


@bp_web.app_errorhandler(404)
def handle_403(e):
    return redirect(url_for("web.main+index"))
