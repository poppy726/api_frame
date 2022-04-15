
import json
import random
import re

import requests

from commons.requests_util import RequestsUtil
from commons.yaml_util import write_extract_yaml, read_extract_yaml


class TestUserApi:

    pass

    # def test_phpwind_index(self):
    #     urls = "/phpwind/"
    #     res = RequestsUtil("base","base_user_url").send_request(method="get",url=urls)
    #
    #     # TestUserApi.csrf_token = re.search('name="csrf_token" value="(.*?)"',res.text).group(1)
    #     write_extract_yaml({"csrf_token":re.search('name="csrf_token" value="(.*?)"',res.text).group(1)})
    #
    #     # TestApi.phpwind_cookies = res.cookies
    #     # TestApi.csrf_token = dict(TestApi.phpwind_cookies)['csrf_token']
    #     # print(TestUserApi.csrf_token)
    #
    #
    # def test_phpwind_login(self):
    #     urls = "/phpwind/index.php?m=u&c=login&a=dorun"
    #     datas = {
    #         "username":"poppy",
    #         "password":"123456",
    #         "csrf_token":read_extract_yaml("csrf_token"),
    #         "backurl":"http://47.107.116.139/phpwind/",
    #         "invite":""
    #     }
    #     headers = {
    #         "Accept":"application/json, text/javascript, /; q=0.01",
    #         "X-Requested-With":"XMLHttpRequest"
    #     }
    #
    #     res = RequestsUtil("base","base_user_url").send_request(method="post",url=urls,data=datas,headers=headers)
    #     # print(res.text)
    #     return res