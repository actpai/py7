import json


# 封装获取测试结果并且返回断言结果的方法
def assert_t_f(http_respone, reponse_code, reponse_msg):
    """
    :param http_respone:发送请求后响应体
    :param reponse_code: 返回状态码
    :param reponse_msg: 返回msg
    :return:
    """
    # 获取测试结果
    status_code = http_respone.status_code
    msg = http_respone.json().get("message")
    # 执行测试断言
    if status_code == reponse_code and msg == reponse_msg:
        return True
    else:
        return False


# 读取数据的公用方法
def build_data(data_path):
    """
    :param data_path:读取文件的路径
    :return:
    """
    # 定义空列表数据
    build_data = []
    # 打开测试数据文件
    with open(data_path, encoding="utf_8") as f:
        # 读取完整数据
        r_data = json.load(f)
        # 遍历所有键值
        for case_data in r_data.values():
            # 再次遍历键值(字典对象)的键值列表
            build_data.append(list(case_data.values()))
            print(build_data)
            # 返回读取数据
        return build_data
