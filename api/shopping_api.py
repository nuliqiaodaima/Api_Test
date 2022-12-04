from core.api_util import api_util
from utils.response_util import process_response


def add_shopping_cart(params, token):
    """
    购物车添加接口
    :param token:
    :param params:
    :return:
    """
    headers = {
        "Authorization": "JWT " + token
    }
    response = api_util.shopping_add(json=params, headers=headers)
    return process_response(response)


def check_shopping_cart(token):
    """
    查看购物车
    :param token:
    :return:
    """
    headers = {
        "Authorization": "JWT " + token
    }
    response = api_util.shopping_check(headers=headers)
    return process_response(response)
