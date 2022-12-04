from core.rest_client import RestClient


# 类的继承
class Api(RestClient):
    # 初始化
    def __init__(self):
        super().__init__()

    # **kwargs可以将params，data，json，headers省略
    def get_mobile_belong(self, **kwargs):
        return self.post("/teladress/teladress", **kwargs)

    def post_data(self, **kwargs):
        return self.post("/posts", **kwargs)

    def get_tiktok(self, **kwargs):
        return self.get("/api/api-girl-11-02/index.php", **kwargs)

    def get_video(self, **kwargs):
        return self.get("/api/api-dy-girl/index.php", **kwargs)

    # 项目实战的方法
    """user_api"""

    def get_code(self, **kwargs):
        return self.post("/code/", **kwargs)

    # 注册
    def register_mobile(self, **kwargs):
        return self.post("/users/", **kwargs)

    # 登录
    def user_login(self, **kwargs):
        return self.post("/login/", **kwargs)

    """goods_api"""

    def banner(self, **kwargs):
        return self.get("/banners/", **kwargs)

    """shopping_api"""

    # 添加商品
    def shopping_add(self, **kwargs):
        return self.post("/shopcarts/", **kwargs)

    # 购物车展示商品
    def shopping_check(self, **kwargs):
        return self.get("/shopcarts/", **kwargs)

    """member_api"""

    # 查看我的订单
    def my_order(self, **kwargs):
        return self.get("/orders/", **kwargs)

    # 删除我的订单
    def delete_order(self, orderid, **kwargs):
        return self.delete(f"/orders/{orderid}/", **kwargs)

    # 查询我的收获地址
    def check_address(self, **kwargs):
        return self.get("/address/", **kwargs)

    # 查询我的收获地址
    def add_delivery_address(self, **kwargs):
        return self.post("/address/", **kwargs)


api_util = Api()
