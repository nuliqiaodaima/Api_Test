import json
from core.ResultBase import ResultResponse
from utils.log_utils import logger


# 封装接口返回结果处理
def process_response(response):
    # 处理删除接口204(不可以用json接收)
    if response.status_code == 204:
        ResultResponse.success = True
        ResultResponse.body = response.text
        logger.info("接口的返回内容>>>" + response.text)
    elif 199 < response.status_code < 301:
        ResultResponse.success = True
        ResultResponse.body = response.json()
        logger.info("接口的返回内容>>>" + json.dumps(response.json(), ensure_ascii=False))
    else:
        ResultResponse.success = False
        logger.info("接口状态码不是2开头，请检查！")
        logger.info("接口的返回内容>>>" + json.dumps(response.json(), ensure_ascii=False))
    return ResultResponse

