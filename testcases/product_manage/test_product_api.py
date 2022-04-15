import random
import pytest
import requests

from commons.requests_util import RequestsUtil
from commons.yaml_util import write_extract_yaml, read_extract_yaml, read_testcases_yaml


class TestProductApi:

    # 通过session会话去关联，session默认情况下会自动关联cookie
    session = requests.session()

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("args_name",read_testcases_yaml('/testcases/product_manage/test_get_token.yaml'))
    def test_get_token(self,args_name):
        name = args_name['name']
        methods = args_name['request']['method']
        urls = args_name['request']['url']
        headers = args_name['request']['headers']
        datas = args_name['request']['datas']
        validate = args_name['validate']

        # urls = "/cgi-bin/token"
        # datas = {
        #     "grant_type":"client_credential",
        #     "appid":"wxb932279ffa5b1f1a",
        #     "secret":"fa4fa2bb2cd3b558526bf14312152595"
        # }

        res = RequestsUtil("base","base_product_url").send_request(method=methods,url=urls,params=datas)
        write_extract_yaml({"access_token":res.json()["access_token"]})


    @pytest.mark.parametrize("args_name", read_testcases_yaml('/testcases/product_manage/test_select_flag.yaml'))
    def test_select_flag(self, args_name):
        name = args_name['name']
        methods = args_name['request']['method']
        urls = args_name['request']['url']
        headers = args_name['request']['headers']
        datas = args_name['request']['datas']
        validate = args_name['validate']

        urls = urls+read_extract_yaml("access_token")
        res = RequestsUtil("base","base_product_url").send_request(method=methods,url=urls)
        return res

    @pytest.mark.parametrize("args_name", read_testcases_yaml('/testcases/product_manage/test_create_flag.yaml'))
    def test_create_flag(self,args_name):
        name = args_name['name']
        methods = args_name['request']['method']
        urls = args_name['request']['url']
        headers = args_name['request']['headers']
        datas = args_name['request']['datas']
        validate = args_name['validate']

        urls = urls+read_extract_yaml("access_token")
        res = RequestsUtil("base","base_product_url").send_request(methods,url=urls,json=datas)
        return res
        # print(json.loads(json.dumps(res.json()).replace(r"\\","\\")))


    @pytest.mark.parametrize("args_name", read_testcases_yaml('/testcases/product_manage/test_file_upload.yaml'))
    def test_file_upload(self,args_name):
        name = args_name['name']
        methods = args_name['request']['method']
        urls = args_name['request']['url']
        headers = args_name['request']['headers']
        datas = args_name['request']['datas']
        validate = args_name['validate']

        urls = urls+read_extract_yaml("access_token")

        for key,value in dict(datas).items():
            datas[key] = open(value,"rb")

        res = RequestsUtil("base","base_product_url").send_request(method=methods,url=urls,files=datas)
        return res


