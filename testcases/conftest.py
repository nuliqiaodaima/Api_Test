import pytest

from api.user_api import login
from utils.read import base_data


# 优化读取data.yaml文件
def get_data():
    return base_data.read_data()


# 登录封装
@pytest.fixture
def login_fixture():
    data = get_data()["login_fixture"]
    mobile = data["mobile"]
    password = data["password"]
    data1 = get_data()["user_login"]
    result = login(mobile, password)
    return result.body["token"], mobile

