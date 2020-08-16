import logging.handlers
import time

# 自媒体域名地址
MP_BASE_URL = "http://ttapi.research.itcast.cn"

# 自媒体请求头
MP_HEADER = {"Content-Type": "application/json"}

# 后台管理系统域名地址
MIS_BASE_URL = "http://ttapi.research.itcast.cn"

# 后台管理系统请求头
MIS_HEADER = {"Content-Type": "application/json"}

# APP域名地址
APP_BASE_URL = "http://ttapi.research.itcast.cn"

# APP请求头
APP_HEADER = {"Content-Type": "application/json"}


# 日志配置
def basic_logger_config():
    # 1.创建日志器
    logger = logging.getLogger()
    # 2.设置级别
    logger.setLevel(level=logging.INFO)
    # 3.创建处理器
    ls = logging.StreamHandler()
    log_file = "./log/apiAtuoTest_log_{}".format(time.strftime("%Y%m%d%H%M%S"))
    lht = logging.handlers.TimedRotatingFileHandler(filename=log_file, when='midnight', interval=1, backupCount=2)
    # 4.创建格式化器
    formatter = logging.Formatter(fmt="%(asctime)s %(levelname)s [%(funcName)s:%(lineno)d] - %(message)s")
    # 5.给处理器添加格式化器
    ls.setFormatter(formatter)
    lht.setFormatter(formatter)
    # 6.给日志添加处理器
    logger.addHandler(ls)
    logger.addHandler(lht)
