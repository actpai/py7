# 文章发布-审核-查看流程
import time
import logging
import pytest
from api import FactoryApi
from app import MP_HEADER, MIS_HEADER, APP_HEADER
from utils.utils_tools import assert_t_f, build_data


# 定义测试类
class TestPbEmQyAritcle:
    # 发布文章的id类属性
    aritcle_id = None

    # 文章标题的类属性
    aritcle_title = None

    # 定义测试方法
    def test_mp_login(self):
        # 定义测试数据
        mobile = "15811859004"
        code = "246810"
        # 调用登录的方法
        mp_login_response = FactoryApi.mp_login.test_mp_login(mobile, code)
        logging.info("自媒体登录结果返回信息为={}".format(mp_login_response.json()))
        # 获取实际结果进行断言
        assert mp_login_response.status_code == 201
        assert mp_login_response.json().get("message") == "OK"
        # 获取登录后的token并存储
        mp_token = mp_login_response.json().get("data").get("token")
        logging.info("自媒体登录后返回token={}".format(mp_token))
        # 给mp后续头部信息添加登录后键值对
        MP_HEADER["Authorization"] = "Bearer " + mp_token
        logging.info("登录后基础配置的头部信息为={}".format(MP_HEADER))

    """
    自媒体-发布文章测试方法
    """

    @pytest.mark.parametrize("ar_title,ar_content,ch_id,status_code,msg", build_data("./data/pb_article_data.json"))
    def test_pb_aritcle(self, ar_title, ar_content, ch_id, status_code, msg):
        # 1.定义测试数据:每一组数据代表的就是一种测试情况
        self.aritcle_title = ar_title.format(time.strftime("%Y%m%d%H%M%S"))
        aritcle_content = ar_content.format(time.strftime("%Y%m%d%H%M%S"))
        channel_id = ch_id
        # 2.调用测试方法:执行对应业务请求的接口方法
        pb_al_response = FactoryApi.pb_aritcle.test_pb_aritcle(self.aritcle_title, aritcle_content, channel_id)
        print("发布文章的结果信息:", pb_al_response.json())
        assert assert_t_f(pb_al_response, status_code, msg)
        # 3.获取测试结果
        # status_code = pb_al_response.status_code
        # msg = pb_al_response.json().get("message")
        # # 4.执行测试断言
        # assert status_code == 201
        # assert msg == "OK"
        # 5.获取关联数据(*)
        self.aritcle_id = pb_al_response.json().get("data").get("id")
        print("发布文章的id为", self.aritcle_id)

    """
    后台管理系统-登录
    """

    def test_mis_login(self):
        # 1.定义测试数据
        username = "testid"
        password = "testpwd123"
        # 2.调用测试方法
        mis_login_response = FactoryApi.mis_login.test_mis_login(username, password)
        print("后台登录结果为:", mis_login_response.json())
        # 3.获取测试结果
        status_code = mis_login_response.status_code
        msg = mis_login_response.json().get("message")
        # 4.执行测试断言
        assert status_code == 201
        assert msg == "OK"
        # 5.获取关联数据
        mis_token = mis_login_response.json().get("data").get("token")
        MIS_HEADER["Authorization"] = "Bearer " + mis_token
        print(MIS_HEADER)

    """
    后台管理系统-文章查询
    """

    # 定义测试方法
    def test_qy_article(self):
        # 定义测试数据
        aritcle_title = self.aritcle_title
        channel = "html"
        # 调用接口方法
        qy_response = FactoryApi.mis_aritcle.test_qy_aritcle(aritcle_title, channel)
        print("查询文章结果为:", qy_response.json())
        # 获取测试结果
        status_code = qy_response.status_code
        msg = qy_response.json().get("message")
        # 执行测试断言
        assert status_code == 200
        assert msg == "OK"
        # assert qy_response.json().get("data").get("articles")[0].get("article_id") == self.aritcle_id
        # 获取关联数据

    """
    app-登录
    """

    # 定义测试方法
    def test_app_login(self):
        phone = "15811859004"
        code = "246810"
        # 定义测试数据
        # 定义接口方法
        al_response = FactoryApi.app_login.test_app_login(phone, code)
        print("app登录响应结果", al_response.json())
        # 获取测试结果
        # 执行测试断言
        assert assert_t_f(al_response, 201, "OK")
        # 获取关联数据
        ap_token = al_response.json().get("data").get("token")
        APP_HEADER["Authorization"] = "Bearer " + ap_token
        print("app带token的请求头信息为:------>", APP_HEADER)

    """
    app-根据频道查询文章
    """

    # 定义测试方法
    def test_qy_al_by_cl(self):
        # 定义测试数据
        cl_id = 1
        time_stamp = int(time.time() * 1000)
        print("当前时间戳:", time_stamp)
        with_top = 1
        # 调用接口方法
        qabc_response = FactoryApi.app_aritcle.test_qy_at_by_channel(cl_id, time_stamp, with_top)
        print("根据频道查询的文章结果为:", qabc_response.json())
        # 获取测试结果
        # 执行测试断言
        assert assert_t_f(qabc_response, 200, "OK")
        # 获取关联数据
