import os

from flask import render_template, redirect, url_for, flash, send_from_directory, request

from app.forms.upload import UploadForm
from app.libs.flask_libs import random_filename, get_data_path
from app.libs.redprint import Redprint

web = Redprint("upload")


@web.route("/", methods=["GET", "POST"])
def index():
    form = UploadForm()
    if form.validate_on_submit():
        file_data = form.avatar.data
        filename = random_filename(file_data.filename)
        file_data.save(os.path.join(get_data_path("img"), filename))
        return render_template("upload/success.html", filetype="img", filename=filename)
    return render_template("upload/upload.html", form=form)


@web.route("/<filetype>/<filename>")
def get_upload(filetype, filename):
    print(get_data_path(filetype), filename)
    return send_from_directory(get_data_path(filetype), filename)
