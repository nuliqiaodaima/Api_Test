# 获取短信验证码
from utils.log_utils import logger
from utils.mysql_util import db


# 获取验证码
def get_code(mobile):
    sql = "select code from users_verifycode where mobile = '%s' order by add_time desc limit 1;" % mobile
    result = db.select_db_one(sql)
    logger.info(f"sql执行结果：{result}")
    return result['code']


# 删除用户
def delete_user(mobile):
    sql = "delete from users_userprofile where mobile = '%s';" % mobile
    result = db.execute_db(sql)
    logger.info(f"sql执行结果：{result}")


# 删除用户验证码
def delete_code(mobile):
    sql = "delete from users_userprofile where mobile = '%s';" % mobile
    result = db.execute_db(sql)
    logger.info(f"sql执行结果：{result}")
