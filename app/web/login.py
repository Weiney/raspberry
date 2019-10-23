from flask import render_template, session, current_app, redirect, url_for, request, flash
from flask_login import login_user, login_required, current_user

from app import redis_store
from app.forms.login import LoginForm
from app.libs.flask_libs import randon_code
from app.libs.redprint import Redprint
from app.models.user import User

web = Redprint("login")


@web.route("/", methods=("GET", "POST"))
def login():
    if current_user.is_active:
        return "你已经登陆过了"

    form = LoginForm()

    if form.validate_on_submit():
        csrf_token = session.get("csrf_token")
        server_code = redis_store.get(csrf_token)
        if server_code is None:
            flash("验证码失效,请从新登录")
            return redirect(url_for("web.login+login"))
        if server_code != form.verification.data.lower():
            flash("验证码错误")
            return redirect(url_for("web.login+login"))

        user = User.query.filter_by(username=form.username.data).first()
        if user:
            redis_store.delete(csrf_token)
            if user.check_password(form.password.data):
                login_user(user)
                next = request.args.get("next")
                if next and next.startswith("/"):
                    return redirect(next)
                return redirect(url_for("web.login+login_success"))
            else:
                flash("密码错误")
                return redirect(url_for("web.login+login"))
        else:
            flash("账号不存在")
            return redirect(url_for("web.login+login"))


    code = randon_code()
    redis_store.set(session.get("csrf_token"), code.lower(), ex=current_app.config.get("VERIFICATION_TIMEOUT", 300))
    return render_template("login/login.html", form=form, code=code)


@web.route("/success")
@login_required
def login_success():
    return "登录成功"
