import yaml
import os

# 获取项目根路径
def get_object_path():
    return os.getcwd()


# 读取extract.yaml
def read_extract_yaml(key):
    with open(get_object_path()+r"\extract.yaml",mode='r',encoding='utf-8') as f:
        value = yaml.load(f,Loader=yaml.FullLoader)
        return value[key]

# 写入extract.yaml
def write_extract_yaml(data):
    with open(get_object_path()+r"\extract.yaml",mode='a',encoding='utf-8') as f:
        value = yaml.dump(data=data,stream=f,allow_unicode=True)
        return value


# 清空
def clear_extract_yaml():
    with open(get_object_path()+r"\extract.yaml",mode='w',encoding='utf-8') as f:
        f.truncate()


# 读取config.yaml
def read_config_yaml(one_node,tow_node):
    with open(get_object_path()+r"\config.yaml",mode='r',encoding='utf-8') as f:
        value = yaml.load(f,Loader=yaml.FullLoader)
        return value[one_node][tow_node]


# 读取测试用例的.yaml
def read_testcases_yaml(yaml_path):
    with open(get_object_path()+yaml_path,mode='r',encoding='utf-8') as f:
        value = yaml.load(f,Loader=yaml.FullLoader)
        return value