Python Flask学习
====
### Day1 文件上传
通过Flask-wtf实现图片的上传保存服务器

### Day2 验证码的实现
使用Redis缓存和Flask-wtf的csrf_token给验证码添加过期时间和过期失效
提高图形验证码的安全性<br>
PS:图形验证码部份未实现,项目中用文本代替,只用作测试功能<br>
如果需要实现图形验证码请转链接: https://www.weiney.com/2108.html

### Day3 实现用户系统,添加接口权限验证
使用Flask-Login实现了登录用户的权限验证Flask_Level
简单的实现了装饰器@limit_level(level=1)保护接口访问
具体的实现细节请查看文件/app/libs/flask_level.py
详细介绍访问:https://www.weiney.com/2204.html

### Day4 完善了Flask-Level,增加异常类
增加了异常信息类PermissionException
完善了Flask-Level的limited_message的使用场景
完善了演示页面的信息,演示了七级权限的接口访问

### Day5 使用Flask-Limiter实现了接口限频的简单Demo
依赖插件Flask-Limiter,实现了简单的接口限频<br>
数据使用Redis缓存,如果没有Redis可以存在内存或者其他<br>
实现了简单的错误处理,处理函数实现在/app/web/errors.py<br>
详细使用请查阅文档:https://flask-limiter.readthedocs.io/en/stable

