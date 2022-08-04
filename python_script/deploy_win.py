#!/usr/bin/python3
# -*- coding: UTF-8 -*-
'''
前段测试环境自动化部署
放在前段项目根目录下
gwtph-test项目标识 yaml文件配置
使用python deploy.py <gwtph-test> --branch <branch>
'''

import os
# import sys
import argparse
import yaml
import subprocess
from datetime import datetime
import platform


BASE_PATH = os.path.dirname(__file__)
# 操作系统
OS = platform.platform().split('-')[0]
print(BASE_PATH)
print(OS)

def parser_yaml():
    yaml_path = os.path.join(BASE_PATH, 'deploy.yaml')
    with open(yaml_path, 'r', encoding='utf8') as f:
        return yaml.safe_load(f.read())


def test_ssh_connect(server_ip='', **kwargs):
    print('test connect {} ...'.format(server_ip))
    command_args = ['ssh', 'root@{}'.format(server_ip), "echo 'hello'"]
    res = subprocess.check_output(command_args, encoding='utf8')
    return True if 'hello\n' == res else False


def build_package(branch, project_path='', package_name='', build_command='yarn build', **kwargs):
    os.chdir(project_path)
    os.system('git checkout ' + branch)
    os.system('git pull')
    print('local executing: {0}'.format(build_command))
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
    backup_name_list = list(filter(lambda i:i.startswith(package_name + '_'), file_list))
    # print(list(backup_name_list))
    if (len(backup_name_list)>=back_nums-1):
        # print(sorted(backup_name_list))
        rm_file = sorted(backup_name_list)[0]
        rm_file_path = os.path.join(server_deploy_path, rm_file)
        if(OS == 'Windows'):
          rm_file_path = rm_file_path.replace('\\', '/')
        rm_command = "rm -rf {0}".format(rm_file_path)
        os.system('ssh root@' + server_ip + ' ' + rm_command)
        print("executing ssh backup command: " + rm_command)
    backup_name_path = os.path.join(server_deploy_path, backup_name)
    if(OS == 'Windows'):
          backup_name_path = backup_name_path.replace('\\', '/')
    backup_command = "mv {0} {1}".format(package_dir, backup_name_path)
    os.system('ssh root@' + server_ip + ' ' + backup_command)
    print("executing ssh backup command: " + backup_command)


def ssh_deploy(server_ip='', server_deploy_path='', package_name='', project_path='', **kwargs):
    # backup
    if(not os.path.exists(project_path)):
      return print('project_path {} not exists'.format(project_path))
    package_dir = os.path.join(server_deploy_path, package_name)
    if(OS == 'Windows'):
      package_dir = package_dir.replace('\\','/')
    # 备份
    backup_dist(server_ip, server_deploy_path, package_dir,package_name)

    # scp translate
    package_dir_local = os.path.join(project_path, package_name)
    scp_command = "scp -r {0} root@{1}:{2}".format(package_dir_local, server_ip,server_deploy_path)
    print('executing scp command: ' + scp_command)

    os.system(scp_command)

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
    else:
      print('connected {}'.format(deploy_info['server_ip']))
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
    # print(test_ssh_connect(server_ip='192.168.10.8'))
