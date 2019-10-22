from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    username = StringField("用户名:", validators=[DataRequired(), Length(6, 16, message="用户名长度为6-16位字符")])
    password = PasswordField("密码:", validators=[DataRequired(), Length(6, 16, message="密码长度为6-16位字符")])
    verification = StringField("验证码:", validators=[DataRequired(), Length(4, 4, "验证码为四位字符")])
    login = SubmitField("登录")
