import os

import yaml


def analyze_file(file_name, key):
    '''
    用来解析yaml文件的数据
    :param file_name: yaml文件名
    :param key: 文件数据里面的key值
    :return:
    例子：@pytest.mark.parametrize("args", analyze_file('login_data.yaml','test_login')
    '''

    with open(".%sdata%s%s" % (os.sep, os.sep, file_name), "r",encoding='utf-8') as f:
        case_data = yaml.load(f)[key]
        data_list = list()
        for i in case_data.values():
            data_list.append(i)
        return data_list



