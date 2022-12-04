from core.api_util import api_util
from utils.response_util import process_response


def check_my_order(token):
    """
    查询我的订单接口
    :return:
    """
    headers = {
        "Authorization": "JWT " + token
    }
    response = api_util.my_order(headers=headers)
    return process_response(response)


def delete_my_order(token, orderid):
    """
    删除订单接口
    :param orderid:
    :param token:
    :return:
    """
    headers = {
        "Authorization": "JWT " + token
    }
    response = api_util.delete_order(orderid, headers=headers)
    return process_response(response)
