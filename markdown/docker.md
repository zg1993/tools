### 一.安装配置
##### Ubuntu 安装 Docker CE


##### 用户添加到group分组
$ sudo groupadd docker
$ sudo usermod -aG docker $USER
注销重新登陆

#### 镜像加速
* [Docker 官方提供的中国 registry mirror `https://registry.docker-cn.com`](https://docs.docker.com/registry/recipes/mirror/#use-case-the-china-registry-mirror)
* [七牛云加速器 `https://reg-mirror.qiniu.com/`](https://kirk-enterprise.github.io/hub-docs/#/user-guide/mirror)

**upstart系统**: /etc/default/docker:
``` bash
 DOCKER_OPTS="--registry-mirror=https://registry.docker-cn.com"
```
重新启动服务
```bash
$ sudo service docker restart
```

**systemd系统**: /etc/docker/daemon.json
```json
{
  "registry-mirrors": [
    "https://registry.docker-cn.com"
  ]
}
```
重启服务
```bash
$ sudo systemctl deamon-reload
$ sudo service docker restartn
```
#### 私人仓库搭
- 远程访问修改/etc/default/docker
- 镜像查看: curl -X GET https://admin:admin@tdocker.mgm-iot.com/v2/_catalog -k
- 密码:htpasswd -b -m -c /etc/nginx/conf.d/htpasswd admin admin
- 下载镜像: docker pull tdocker.mgm-iot.com/admin/hello-world:latest
- 上传镜像:
```bash
$	docker	tag	ubuntu:17.10	docker.domain.com/username/ubuntu:17.10
$	docker	push	docker.domain.com/username/ubuntu:17.10
```
- ![doc](https://docs.docker.com/registry/recipes/nginx/#starting-and-stopping)
- ![blog](https://blog.csdn.net/gqtcgq/article/details/51163558)
- 启动:docker run -d -p 5000:5000 -v /home/zhou/registry/:/var/lib/registry --name registry registry
- 查看仓库镜像: curl 127.0.0.1:5000/v2/_catalog
- 标记镜像: docker tag alpine:latest 127.0.0.1:5000/alpine:latest
- 推送镜像: docker push 127.0.0.1:5000/alpine

##### 11-13
- 查看镜像仓库的内容: curl -X GET localhost:5000/v2/_catalog -k
- 获取某个镜像的标签列表：curl -X GET https://admin:admin@tdocker.mgm-iot.com/v2/moses/tags/list -k
- 镜像推送:
 + docker tag redis:latest localhost:5000/redis:latest
 + docker push localhost:5000/redis
- 镜像下载: docker pull localhost:5000/redis
- 登录：docker login -u=abc https://localhost:5000
- 其它主机登录:/etc/docker/daemon.json:
{"insecure-registries":["192.168.1.186:5000"]}



### 1.指令
- 列出镜像: docker image ls
- 查找镜像: docker search mirror-name
- 获取镜像: docker pull python:2.7
- 删除镜像: docker image rm docker  ID、镜像名、摘要
- 去除为none的镜像: docker image prune
- 启动镜像: docker run python:2.7
 * -d: 后台运行
 * --rm: 运行完后删除 container
 * -p <localhost:port>:<container:port>
- 列出所有正在运行的容器: docker ps
    + 列出所有容器: docker ps -a
- 列出docker的容器: docker container ls
- 启动容器: docker start <name\>
- 获取容器ip:
  + docker inspect --format '{{.NetworkSettings.IPAddress}}' <name\>
  + cat /etc/hosts
- 暂停容器: docker stop <name\>
- 进入容器: docker exec -ti <name\> bash
- 容器和主机文件copy: docker cp
- 删除容器: docker rm <name\> (容器必须是停止状态)
- 删除所有已停止的容器: docker rm $(docker ps -a -q)
- 构建镜像: docker build -t hello .
  + -t tag options
  + -f 指定Dockerfile
  + . 镜像构建的上下文
- 容器修改后提交: \
```
$	docker	commit	\
				--author	"Tao	Wang	<twang2218@gmail.com>"	\
				--message	"修改了默认网页"	\
				webserver	\
				nginx:v2
```
- log 查看： docker logs -f container

### 2.compose
##### install
```bash
$ sudo curl -L https://github.com/docker/compose/releases/download/1.18.0/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
$ sudo chmod +x /usr/local/bin/docker-compose
```
##### 命令
- 启动 docker-compose up


### frequently question answer
- 容器访问本机端口：docker0的地址：端口


### 配置文件事例

#### Dockerfile
``` python
# Use an official Python runtime as a parent image
FROM python:2.7-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]
```
#### .dcokerignore
```bash
.git
front 忽略目录front
tools
uitest
sandbox
*.pyc

*/* 忽略所以
!back back文件或者目录除外
!common
```

### frequent question answer
```
Traceback (most recent call last):
  File "/root/moses/back/bms/bms_server.py", line 9, in <module>
    from web.server import configure, configure_options
ImportError: No module named web.server
```
python的site-packages目录添加moses.pth: /root/moses/back

alpine
```
env: can't execute 'bash': No such file or directory
```
Dockerfile 添加
```
RUN set -euxo pipefail && \
    apk add --no-cache bash
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories && \
    apk update
```


## redis
##### 基本命令
- 服务的开启（关闭）: service redis-server start (stop)



### FQA
+ "Can't resolve address" when Kafka in Docker
      Issue
      使用Docker运行Kafka，在produce message时发生Can't resolve address: 7fd4f3dcac6c:9092，其中 7fd4f3dcac6c 为contianer的hostname

      Solution
      vi config/server.properties and SET advertised.host.name=<Your Docker IP,like 192.168.0.100>
