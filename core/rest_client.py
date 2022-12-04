import json
import requests
from utils.read import base_data
from utils.log_utils import logger

api_root_url = base_data.read_ini()["host"]["api_sit_url"]


class RestClient:
    def __init__(self):
        self.api_root_url = api_root_url

    # 封装请求
    def get(self, url, **kwargs):
        # return requests.get(self.api_root_url + url, **kwargs)
        return self.request(url, "GET", **kwargs)

    def post(self, url, **kwargs):
        # logger.info(url)
        # logger.info(kwargs)
        # return requests.post(self.api_root_url + url, **kwargs)
        return self.request(url, "POST", **kwargs)

    def put(self, url, **kwargs):
        return self.request(url, "PUT", **kwargs)

    def delete(self, url, **kwargs):
        return self.request(url, "DELETE", **kwargs)

    # 封装GET、POST请求
    def request(self, url, method, **kwargs):
        self.request_log(url, method, **kwargs)
        if method == "GET":
            return requests.get(self.api_root_url + url, **kwargs)
        if method == "POST":
            return requests.post(self.api_root_url + url, **kwargs)
        if method == "PUT":
            return requests.put(self.api_root_url + url, **kwargs)
        if method == "DELETE":
            return requests.delete(self.api_root_url + url, **kwargs)

    # 封装发送日志请求
    def request_log(self, url, method, **kwargs):
        data = dict(**kwargs).get("data")
        json_data = dict(**kwargs).get("json")
        params = dict(**kwargs).get("params")
        headers = dict(**kwargs).get("headers")
        logger.info("接口请求的地址>>>{}".format(self.api_root_url + url))
        logger.info("接口请求的方法>>>{}".format(method))
        # 判断请求参数类型
        if data is not None:
            logger.info("接口请求的data参数>>>\n{}".format(json.dumps(data, indent=2)))
        if json_data is not None:
            # json.dumps(kwargs["json"], indent=2 将获取到的json请求格式化
            logger.info("接口请求的json参数>>>\n{}".format(json.dumps(json_data, indent=2)))
        if params is not None:
            logger.info("接口请求的params参数>>>\n{}".format(json.dumps(params, indent=2)))
        if headers is not None:
            logger.info("接口请求的请求头参数>>>\n{}".format(json.dumps(headers, indent=2)))
