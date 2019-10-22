from flask import render_template, session, current_app

from app import redis_store
from app.forms.login import LoginForm
from app.libs.flask_libs import randon_code
from app.libs.redprint import Redprint

web = Redprint("login")


@web.route("/", methods=("GET", "POST"))
def login():
    form = LoginForm()

    if form.validate_on_submit():
        if form.username.data == "weiney" and form.password.data == "123456":
            csrf_token = session.get("csrf_token")
            server_code = redis_store.get(csrf_token)
            if server_code is None:
                return "验证码失效,请刷新重试"
            if server_code == form.verification.data.lower():
                redis_store.delete(csrf_token)
                return "登录成功"
            else:
                return "验证码错误"

    code = randon_code()
    redis_store.set(session.get("csrf_token"), code.lower(), ex=current_app.config.get("VERIFICATION_TIMEOUT", 300))
    return render_template("login/login.html", form=form, code=code)
