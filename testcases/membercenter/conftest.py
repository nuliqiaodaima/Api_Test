import pytest

from utils.mysql_util import db


# 查询用户所有订单
def user_order(mobile):
    sql = f"select * from trade_orderinfo where singer_mobile = {mobile};"
    result = db.select_db_all(sql)
    return result


# 查询用户订单id
def order_id(mobile):
    sql = f"select id from trade_orderinfo where singer_mobile = {mobile} order by add_time desc limit 1;"
    result = db.select_db_one(sql)
    return result["id"]


