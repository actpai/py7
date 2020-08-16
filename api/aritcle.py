"""
文章相关的API
"""
from app import MP_BASE_URL, MP_HEADER, MIS_HEADER, MIS_BASE_URL, APP_BASE_URL, APP_HEADER
import requests


# 自媒体
class PublishAritcle:

    def __init__(self):
        # 发布文章的请求地址
        self.pb_aritcle_url = MP_BASE_URL + "/mp/v1_0/articles"

    # 发布文章接口方法
    def test_pb_aritcle(self, title, content, channel_id):
        # 定义测试数据
        params = {"title": title, "content": content, "channel_id": channel_id, "cover": {"type": 0, "images": []}}
        # 调用POST接口
        return requests.post(url=self.pb_aritcle_url, json=params, headers=MP_HEADER)


# 后台管理系统
class MisAritcle:

    # 定义接口路径
    def __init__(self):
        # 查询文章的请求地址
        self.qy_aritcle_url = MIS_BASE_URL + "/mis/v1_0/articles"
        # 审核文章的请求地址
        self.ex_aritcle_url = MIS_BASE_URL + "/mis/v1_0/articles"

    # 封装接口方法
    def test_qy_aritcle(self, title, channel):
        # 定义测试数据
        query_string = {"title": title, "channel": channel}
        # 调用接口请求
        return requests.get(url=self.qy_aritcle_url, params=query_string, headers=MIS_HEADER)

    # 封装审核文章
    # 定义测试方法
    def test_ex_aritcle(self, ar_id, status):
        # 定义接口数据
        params = {"article": [ar_id], "status": status}
        # 执行接口请求
        return requests.put(url=self.ex_aritcle_url, data=params, headers=MIS_HEADER)


# app
class AppAritcle:

    # 定义接口路径
    def __init__(self):
        # 根据频道查询新闻的接口数据
        self.qy_at_byc_url = APP_BASE_URL + "/app/v1_1/articles"

    # 定义测试方法
    def test_qy_at_by_channel(self, cl_id, timestamp, with_top):
        # 定义接口数据
        qy_string = {"channel_id": cl_id, "timestamp": timestamp, "with_top": with_top}
        # 执行接口请求
        return requests.get(url=self.qy_at_byc_url, params=qy_string, headers=APP_HEADER)
