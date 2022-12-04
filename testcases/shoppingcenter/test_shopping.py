import allure

from api.shopping_api import add_shopping_cart, check_shopping_cart
from testcases.conftest import get_data
from testcases.shoppingcenter.conftest import get_shop_cart_num


@allure.feature("添加购物车模块")
class TestShopping:
    @allure.story("购物车模块操作")
    @allure.title("购物车添加食品")
    def test_shopping_cart(self, login_fixture):
        token = login_fixture[0]
        param = get_data()["shopping_cart"]
        result = add_shopping_cart(param, token)
        # 判断接口返回的食品goods是否等于添加的食品goods
        assert result.success is True
        assert result.body["goods"] == param["goods"]

    @allure.story("购物车模块操作")
    @allure.title("查看购物车")
    def test_pay(self, login_fixture):
        token = login_fixture[0]
        username = login_fixture[1]
        param = get_data()["shopping_cart"]
        result = check_shopping_cart(token)
        # 查询购物车数量(添加后查询)
        num = get_shop_cart_num(username, param['goods'])
        assert result.success is True
        assert result.body[0]['nums'] == num
