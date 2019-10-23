from flask_login import UserMixin
from sqlalchemy import Column, Integer, String
from werkzeug.security import generate_password_hash, check_password_hash

from app import login_manager
from app.libs.flask_level import BaseLevel
from app.models.base import Base


class User(Base, UserMixin, BaseLevel):
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=True)
    _password = Column("password", String(128), nullable=True)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    def check_password(self, raw):
        return check_password_hash(self._password, raw)


@login_manager.user_loader
def get_user(uid):
    return User.query.get(int(uid))
