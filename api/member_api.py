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


def check_my_address(token):
    """
    查询我的收货地址接口
    :param token:
    :return:
    """
    headers = {
        "Authorization": "JWT " + token
    }
    response = api_util.check_address(headers=headers)
    return process_response(response)


def add_delivery_address(params, token):
    """
    新增收货地址接口
    :param params:
    :param token:
    :return:
    """
    headers = {
        "Authorization": "JWT " + token
    }
    response = api_util.add_delivery_address(json=params, headers=headers)
    return process_response(response)
