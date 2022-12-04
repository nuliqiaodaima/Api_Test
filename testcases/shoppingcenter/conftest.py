from utils.log_utils import logger
from utils.mysql_util import db


# 查询user_id
def user_id(mobile):
    sql = "select id from users_userprofile where mobile = '%s';" % mobile
    # sql = f"select id from users_userprofile where mobile = {mobile};"
    result = db.select_db_one(sql)
    return result["id"]


def get_shop_cart_num(username, good_id):
    # 查询UID
    id = user_id(username)
    # sql = "select nums from trade_shoppingcart where user_id = %d and goods_id = %d;" % (id, good_id)
    sql = f"select nums from trade_shoppingcart where user_id = {id} and goods_id = {good_id};"
    result = db.select_db_one(sql)
    return result['nums']


# 查询购物车商品
def check_shop_cart(username):
    id = user_id(username)
    sql = f"select name from goods_goods RIGHT JOIN trade_shoppingcart ON goods_goods.id = trade_shoppingcart.goods_id where user_id = {id};"
    result = db.select_db_all(sql)
    return result
