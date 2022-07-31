#!/usr/bin/python3
# -*- coding: UTF-8 -*-
'''
前段测试环境自动化部署
放在前段项目根目录下
gwtph-test项目标识 yaml文件配置
使用python deploy.py <gwtph-test> --branch <branch>
'''

import os
import sys
import argparse
import yaml

BASE_PATH = os.path.dirname(__file__)
PACKAGE_NAME = 'gwtph-web'
SERVER_PATH = '/etc/nginx/html'
HOSTNAME = 'serve108'


def parser_yaml():
    yaml_path = os.path.join(BASE_PATH, 'deploy.yaml')
    with open(yaml_path, 'r', encoding='utf8') as f:
        return yaml.safe_load(f.read()) 



def build_package(branch, package_name=PACKAGE_NAME):
    os.chdir(BASE_PATH)
    os.system('git checkout ' + branch)
    os.system('git pull')
    os.system('yarn build')
    if not os.path.exists('dist'):
        print('build failed')
        return
    os.system('mv dist ' + package_name)
    return True


def ssh_deploy(hostname='serve108'):
    dir_path = os.path.join(SERVER_PATH, PACKAGE_NAME)
    dir_path_backup = dir_path + '_backup'
    print('server pwd: ' + dir_path)
    command_backup = "mv " + dir_path + ' ' + dir_path_backup
    print('executing backup ssh command: ' + command_backup)
    os.system('ssh root@' + hostname + ' ' + command_backup)
    # print('execut success')
    package_path = os.path.join(BASE_PATH, PACKAGE_NAME)
    print(package_path)
    command_scp = "scp -r " + package_path + ' ' + 'root@' + hostname + ':' + SERVER_PATH
    print('executing scp command: ' + command_scp)
    os.system(command_scp)
    # print('execut success')
    command_rm = "rm -rf " + dir_path_backup
    print('executing rm  ssh command: ' + command_rm)
    os.system('ssh root@' + hostname + ' ' + command_rm)
    print('deploy success')
    os.system('rm -rf' + ' ' + os.path.join(BASE_PATH, PACKAGE_NAME))

def deploy(project, branch):
    server_dict = parser_yaml()
    # print(server_dict)
    if (project not in server_dict):
        print('%s not config, please add to deploy.yaml'%(project))
        return
    deploy_info = server_dict.get(project)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('project', help='项目标识必填yaml文件配置')
    parser.add_argument('--branch', help='发布分支名称，默认使用dev')
    # print(sys.argv)
    args = parser.parse_args()
    project = args.project
    branch = args.branch or 'dev'
    deploy(project, branch)
    # branch = 'dev'
    # if len(sys.argv) > 1:
    #     branch = sys.argv[1]
    # if build_package(branch):
    #     ssh_deploy(HOSTNAME)

# os.chdir('')
# os.system("rm -rf dist")
# os.system("yarn build")
# os.system("mv dist gwtph-web")
