#!/usr/bin/python3
# -*- coding: UTF-8 -*-

'''
前段测试环境自动化部署
放在前段项目根目录下
使用python deploy.py <branch>
'''

import os
import sys

BASE_PATH = os.path.dirname(__file__)
PACKAGE_NAME = 'gwtph-web'
SERVER_PATH = '/etc/nginx/html'
HOSTNAME = 'serve108'


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
  print('server pwd: '+dir_path)
  command_backup = "mv " + dir_path + ' ' + dir_path_backup
  print('executing backup ssh command: ' + command_backup)
  os.system('ssh root@'+ hostname + ' ' + command_backup)
  # print('execut success')
  package_path = os.path.join(BASE_PATH, PACKAGE_NAME)
  print (package_path)
  command_scp = "scp -r " + package_path + ' '+ 'root@'+hostname+':' + SERVER_PATH
  print('executing scp command: ' + command_scp)
  os.system(command_scp)
  # print('execut success')
  command_rm = "rm -rf " + dir_path_backup
  print('executing rm  ssh command: ' + command_rm)
  os.system('ssh root@'+ hostname + ' ' + command_rm)
  print('deploy success')
  os.system('rm -rf' + ' '+os.path.join(BASE_PATH, PACKAGE_NAME))


if __name__ == '__main__':
  branch = 'dev'
  if len(sys.argv) > 1:
    branch = sys.argv[1]
  if build_package(branch):
    ssh_deploy(HOSTNAME)


# os.chdir('')
# os.system("rm -rf dist")
# os.system("yarn build")
# os.system("mv dist gwtph-web")
