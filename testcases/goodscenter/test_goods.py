import allure
import pytest

from api.goods_api import get_banner
from testcases.goodscenter.conftest import banner_num


@allure.feature("用户中心模块")
class TestGoods:
    @allure.story("首页展示内容")
    @allure.title("banner")
    @pytest.mark.run(order=2)
    def test_banner(self, banner_num):
        result = get_banner()
        assert result.success is True
        assert len(result.body) == banner_num
