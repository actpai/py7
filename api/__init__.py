from api.aritcle import PublishAritcle, MisAritcle, AppAritcle
from api.login import MpLogin, MisLogin, AppLogin
from app import basic_logger_config

# 调用日志配置的方法
basic_logger_config()


class FactoryApi:
    # 自媒体登录类的类属性
    mp_login = MpLogin()
    # 自媒体发布文章的类属性
    pb_aritcle = PublishAritcle()
    # 后台管理系统登录类的类属性
    mis_login = MisLogin()
    # 后台管理系统文章的类属性
    mis_aritcle = MisAritcle()
    # app登录的类属性
    app_login = AppLogin()
    # app文章的类属性
    app_aritcle = AppAritcle()
