"""
@author:poppy
@time:2022/4/14 21:50
"""
import requests

from commons.yaml_util import read_config_yaml


class RequestsUtil:

    def __init__(self,one_node,tow_node):
        self.base_url = read_config_yaml(one_node,tow_node)

    session = requests.session()

    # 统一请求封装
    def send_request(self,method,url,**kwargs):
        # 请求方法处理
        method = str(method).lower()
        # 基础路径拼接
        url = self.base_url + url
        res = RequestsUtil.session.request(method,url,**kwargs)
        print(res.text)
        return res

