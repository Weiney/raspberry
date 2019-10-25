'''
    基于Flask-Login和SQLAlchemy实现的接口等级管理插件
    用户Model类需要继承自基类BaseLimit,这个基类只有一个字段
    limit_level = Column(SmallInteger, default=0)

    这个字段用做等级限制

    可以通过装饰器@level_limit(level=0)实现对接口的权限限制

    注意:
        这个装饰器必须与flask_login的@login_required搭配使用,
        且必须放在@login_required之后,否则会出现一些不可控的错误
        eg:
            @web.route("/test")
            @login_required
            @level_limit(level=2)
            def test():
                return "这是一个级别为2的路由"

    本扩展只做权限的简单判断,登录处理都是由Flask-Login处理

    当用户权限符合接口权限则执行路由内部相关代码,
    否则会raise一个PermissionException,这个异常就是一个简单封装的HTTPException,错误码为403

    你可以通过error_handler捕获这个异常并加以处理,
    同时你也可以定义一个limited_message来替换掉原生的description

    你同样还可以像Flask-Login一样设置一个limited_view
    此时在出现权限限制的时候会将请求重定向到这个试图当中


'''
from functools import wraps

from flask import current_app, redirect, url_for
from flask_login import current_user
from sqlalchemy import SmallInteger, Column
from werkzeug.exceptions import HTTPException


class FlaskLevel():
    def __init__(self):
        self.limited_view = None
        self.limited_message = None

    def init_app(self, app):
        app.limit_level = self


class BaseLevel():
    limit_level = Column(SmallInteger, default=0)


def level_limit(level=0):
    def decorater(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if current_user.limit_level >= level:
                return func(*args, **kwargs)
            elif current_app.limit_level.limited_view:
                return redirect(url_for(current_app.limit_level.limited_view))
            else:
                limited_message = current_app.limit_level.limited_message
                if limited_message is None:
                    limited_message = "访问出现了错误,您似乎发送了一个超权限请求,权限等级{},您的权限等级{}".format(
                        level, current_user.limit_level)
                raise PermissionException(limited_message)

        return wrapper

    return decorater


class PermissionException(HTTPException):
    code = 403
