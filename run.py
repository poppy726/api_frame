
import os
import time

import pytest

if __name__ == '__main__':
    pytest.main()
    time.sleep(3)
#     # times = time.strftime("%Y_%m_%d_%H_%M_%S",time.localtime())
#     # os.system("allure generate ./temps -o ./reports/report_"+times+" --clean")
#     # os.system("allure generate ./temps -o ./reports --clean")


# from commons.yaml_util import get_object_path, read_extract_yaml
#
# if __name__ == '__main__':
#     # get_object_path()
#     read_extract_yaml()
#     print(read_extract_yaml())