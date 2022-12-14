import allure

from api.member_api import check_my_order, delete_my_order, check_my_address, add_delivery_address
from testcases.conftest import get_data
from testcases.membercenter.conftest import user_order, order_id


@allure.feature("会员中心")
class TestMember:
    @allure.story("订单中心")
    @allure.title("查看我的订单")
    def test_my_order(self, login_fixture):
        token = login_fixture[0]
        username = login_fixture[1]
        result = check_my_order(token)
        # 查询刚刚的订单是否创建成功
        order = user_order(username)
        assert result.success is True

    @allure.title("删除订单")
    def test_delete_order(self, login_fixture):
        token = login_fixture[0]
        username = login_fixture[1]
        orderid = order_id(username)
        result = delete_my_order(token, orderid)
        assert result.success is True

    @allure.title("查询收货地址")
    def test_check_address(self, login_fixture):
        token = login_fixture[0]
        username = login_fixture[1]
        result = check_my_address(token)
        assert result.success is True

    @allure.title("新增收货地址")
    def test_check_address(self, login_fixture):
        token = login_fixture[0]
        param = get_data()["user_address"]
        result = add_delivery_address(param, token)
        assert result.success is True
        # 判断接口返回的地址是否等于添加的地址
        assert result.success is True
        assert result.body["city"] == param["city"]
        assert result.body["district"] == param["district"]
        assert result.body["province"] == param["province"]

