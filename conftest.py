"""
@author:poppy
@time:2022/4/14 23:15
"""
import pytest

from commons.yaml_util import clear_extract_yaml


@pytest.fixture(scope="session",autouse=True)
def clear_extract():
    clear_extract_yaml()