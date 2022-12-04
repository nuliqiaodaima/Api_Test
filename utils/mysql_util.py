import pymysql

from utils.log_utils import logger
from utils.read import base_data

# 读取配置文件数据
data = base_data.read_ini()["mysql"]
DB_CONF = {
    "host": data["MYSQL_HOST"],
    "port": int(data["MYSQL_PORT"]),
    "user": data["MYSQL_USER"],
    "password": data["MYSQL_PASSWORD"],
    "db": data["MYSQL_DB"]
}


class MysqlDb:
    def __init__(self):
        # mysql连接数据库
        self.conn = pymysql.connect(**DB_CONF, autocommit=True)
        # 创建游标
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    # 释放资源
    def __del__(self):
        self.cur.close()
        self.conn.cursor()

    # 查询一条数据
    def select_db_one(self, sql):
        logger.info(f'执行sql：{sql}')
        self.cur.execute(sql)
        # 获取数据
        result = self.cur.fetchone()
        logger.info(f'sql执行结果：{result}')
        return result

    # 查询多条数据
    def select_db_all(self, sql):
        logger.info(f'执行sql：{sql}')
        self.cur.execute(sql)
        # 获取数据
        result = self.cur.fetchall()
        logger.info(f'sql执行结果：{result}')
        return result

    # 更新数据
    def execute_db(self, sql):
        try:
            logger.info(f'执行sql：{sql}')
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            logger.info("执行sql出错{}".format(e))


db = MysqlDb()
if __name__ == '__main__':
    db = MysqlDb()
    result = db.select_db_all(
        "select name from goods_goods RIGHT JOIN trade_shoppingcart ON goods_goods.id = trade_shoppingcart.goods_id where user_id = 162751")

