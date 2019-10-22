from flask_wtf.file import FileRequired, FileAllowed

from app.forms import MyBaseForm
from wtforms import StringField, PasswordField, FileField, SubmitField
from wtforms.validators import DataRequired, Length


class UploadForm(MyBaseForm):
    username = StringField("账号:", validators=[DataRequired(), Length(6, 12)])
    password = PasswordField("密码:", validators=[DataRequired(), Length(6, 12)])
    avatar = FileField("上传头像:", validators=[FileRequired(), FileAllowed(["jpg", "png", "jpeg", "gif"])])
    submit = SubmitField("登录")
