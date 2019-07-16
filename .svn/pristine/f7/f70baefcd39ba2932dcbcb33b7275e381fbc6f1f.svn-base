# encoding: utf-8
'''
@author: lingshu
@file: get_file_path.py
@time: 2019/6/21 17:09
@desc: 获取文件路径
'''
import os

project_name="api_auto_test"
def get_root_path():
    '''
    获取根路径
    :param project_name: 项目名
    :return:
    '''
    curPath = os.path.abspath(os.path.dirname(__file__))
    rootPath = curPath[:curPath.find(project_name+"\\") + len(project_name+"\\")]  # 获取myProject，也就是项目的根路径
    # print("rootPath= %s",rootPath)
    return rootPath

if __name__ == '__main__':
    print(get_root_path())