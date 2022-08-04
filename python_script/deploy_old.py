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
import subprocess
from datetime import datetime


BASE_PATH = os.path.dirname(__file__)
# PACKAGE_NAME = 'gwtph-web'
# SERVER_PATH = '/etc/nginx/html'
# HOSTNAME = 'serve108'


def parser_yaml():
    yaml_path = os.path.join(BASE_PATH, 'deploy.yaml')
    with open(yaml_path, 'r', encoding='utf8') as f:
        return yaml.safe_load(f.read()) 


def test_ssh_connect(server_ip='', **kwargs):
    print(server_ip)
    test_command = "ssh root@{0} echo 'connect success'".format(server_ip) 
    # test_command = 'ssh root@{0} pwd'.format('192.168.10.157') 
    c = os.system(test_command)
    if(os.system(test_command) != 0):
        return False
    return True


def build_package(branch, project_path='', package_name='', build_command='yarn build', **kwargs):
    os.chdir(project_path)
    os.system('git checkout ' + branch)
    os.system('git pull')
    print('executing: {0}'.format(build_command))
    os.system(build_command)
    if not os.path.exists('dist'):
        print('build failed')
        return False
    os.system('mv dist ' + package_name)
    return True


# 最多保存5份
def backup_dist(server_ip, server_deploy_path, package_dir,package_name, back_nums=5):
    backup_name = package_name + '_' + datetime.today().strftime('%m%d%H%M')
    # suf = re.sub(u'([^\u0041-\u007a])', '', file)
    # name = re.sub(u"([^\u0030-\u0039])", "", file)
    command_args = ['ssh', 'root@{}'.format(server_ip), 'ls {}'.format(server_deploy_path)]
    result_ls = subprocess.check_output(command_args, encoding='utf8')
    file_list = result_ls.split('\n')
    backup_name_list = filter(lambda i:i.startswith(package_name), file_list)
    if (len(list(backup_name_list))<5):
        backup_command = "mv {0} {1}".format(package_dir, backup_name)
    else:
        rm_file = sorted(backup_name_list)[0]
        rm_command = "rm -rf {0}".format(rm_file)
        # os.system('ssh root@' + server_ip + ' ' + rm_command)
        print(rm_command)
    # os.system('ssh root@' + server_ip + ' ' + backup_command)
    print(backup_command)


def ssh_deploy(server_ip='', server_deploy_path='', package_name='', project_path='', **kwargs):
    # backup
    package_dir = os.path.join(server_deploy_path, package_name)
    package_backup_dir = package_dir + '_backup'
    backup_command = "mv {0} {1}".format(package_dir, package_backup_dir)
    print('executing backup ssh command: ' + backup_command)
    backup_dist(server_ip, server_deploy_path, package_dir,package_name)
    #os.system('ssh root@' + server_ip + ' ' + backup_command)

    # scp translate
    package_dir_local = os.path.join(project_path, package_name)
    scp_command = "scp -r {0} root@{1}:{2}".format(package_dir_local, server_ip,server_deploy_path)
    print('executing scp command: ' + scp_command)

    #os.system(scp_command)

    # 删除服务器备份包
    rm_command = "rm -rf {0}".format(package_backup_dir)
    print('executing rm  ssh command: ' + rm_command)

    #os.system('ssh root@' + server_ip + ' ' + rm_command)

    print('deploy success')
    # delete local dist
    os.system('rm -rf' + ' ' + os.path.join(BASE_PATH, package_dir_local))

def deploy(project, branch):
    server_dict = parser_yaml()
    # print(server_dict)
    if (project not in server_dict):
        return print('%s not config, please add to deploy.yaml'%(project))
    deploy_info = server_dict.get(project)
    if(not test_ssh_connect(**deploy_info)):
        return print('unable to connect {server_ip}'.format(**deploy_info))
    # if(build_package(branch, **deploy_info)):
    if(1):
        ssh_deploy(**deploy_info)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('project', help='项目标识必填yaml文件配置')
    parser.add_argument('--branch', help='发布分支名称，默认使用dev')
    args = parser.parse_args()
    project = args.project
    branch = args.branch or 'dev'
    deploy(project, branch)