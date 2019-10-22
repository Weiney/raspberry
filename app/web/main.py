from flask import render_template, request

from app.libs.redprint import Redprint

web = Redprint("main")


@web.route("/")
def index():
    return render_template("index.html")
