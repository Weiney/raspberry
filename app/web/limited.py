from app import limiter
from app.libs.redprint import Redprint

web = Redprint("limited")
share_limit = limiter.shared_limit("10 per hour", scope="test")


# scope可以为string或者为一个可调用的方法,传入方法可以实现访问频率的动态配置
# 详情查看: https://flask-limiter.readthedocs.io/en/stable/#flask_limiter.Limiter.shared_limit


@web.route("/slow")
@limiter.limit("1 per day")
def slow():
    # 限制每天只能有一次访问
    return "i am slow"


@web.route("/default")
def default():
    # 没有添加限频,使用默认限频配置
    return "i am default"


@web.route("/exempt")
@limiter.exempt
def exempt():
    # 这个路由不会被频率限制
    return "i am exempt"


@web.route("/share1")
@share_limit
def share1():
    # 共享限频器,两个路由使用一个配置
    return "i am share1"


@web.route("/share2")
@share_limit
def share2():
    # 共享限频器,两个路由使用一个配置
    return "i am share2"
