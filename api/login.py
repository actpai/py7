import requests
from app import MP_BASE_URL, MP_HEADER, MIS_BASE_URL, MIS_HEADER, APP_BASE_URL, APP_HEADER


# 自媒体
class MpLogin:

    def __init__(self):
        # 自媒体登录的请求地址
        self.mp_login_url = MP_BASE_URL + "/mp/v1_0/authorizations"

    # 登录的测试方法
    def test_mp_login(self, mobile, code):
        # 定义数据
        params = {"mobile": mobile, "code": code}
        # 执行请求
        return requests.post(url=self.mp_login_url, json=params, headers=MP_HEADER)


# 后台管理系统
class MisLogin:
    # 1.定义接口路径
    def __init__(self):
        # 后台管理系统的请求地址
        self.mis_login_url = MIS_BASE_URL + "/mis/v1_0/authorizations"

    # 2.定义测试方法
    def test_mis_login(self, username, password):
        """
        :param username: 后台账号
        :param password: 后台密码
        :return:
        """
        # 3.定义接口数据
        params = {"account": username, "password": password}
        # 4.执行接口请求
        return requests.post(url=self.mis_login_url, json=params, headers=MIS_HEADER)


# APP
# 定义接口类
class AppLogin:
    # 定义接口路径
    def __init__(self):
        self.app_login_url = APP_BASE_URL + "/app/v1_0/authorizations"

    # 定义测试方法
    def test_app_login(self, mobile, code):
        """
        :param mobile: 账号
        :param code: 验证码
        :return: 登录响应体
        """
        # 定义接口数据
        params = {"mobile": mobile, "code": code}
        # 执行接口请求
        return requests.post(url=self.app_login_url, json=params, headers=APP_HEADER)
