### 1.docker 安装
  - [官网链接](https://docs.docker.com/install/linux/docker-ce/ubuntu/)


### 2.镜像制作

```bash
# moses:pro
cd ~/moses/docker
docker build -f Dockerfile -t moses:pro /home/server/moses/
docker tag
docker push

# kafka
cd ~/software
docker build -t "kafka:`date +%Y%m%d`" -f ~/moses/docker/kafka_Dockerfile .
```

### 3.镜像下载
#### 3.1 linux
 - 创建 /etc/docker/certs.d/tdocker.mgm-iot.com/ca.crt 文件(文件内容同测试服/etc/nginx/conf.d/domain.crt,无法登录测试服请求管理员发送证书)
 - 镜像查看: curl -X GET https://admin:admin@tdocker.mgm-iot.com/v2/_catalog -k
 - 获取证书后登录docker仓库: docker login -u=admin https://tdocker.mgm-iot.com 输入密码:amdin
 - 镜像下载:
   +  docker pull tdocker.mgm-iot.com/moses:m11 (tdocker.mgm-iot.ocm: hbase redi kafka moses)
   +  docker pull eclipse-mosquitto:latest
 - U盘安装镜像:
   + 镜像保存为本地文件: docker save -o moses tdocker.mgm-iot.com/moses:m11
   + 从文件载入镜像: docker load --inpurt moses

### 4.运行镜像
#### linux
  - docker-compose 安装
  - 运行
      ```bash
      cd $path # docker-compose.yml 所在的目录下
      docker-compose up -d
      ```
  - 进入servers 执行建表操作和创建后台超级用户
      ```bash
      docker exec -it servers  bash
      python back/web/create_table.py --env=docker
      python back/bms/create_admin.py --env=docker
      ```

  - 镜像更新后重启
  ```
  docker-compose stop servers
  docker-compose rm servers
  docker-compose create servers
  docker-compose start servers
  ```
docker-compose.yml文件

```yml
version: '2'
services:
  kafka:
    image: tdocker.mgm-iot.com/kafka:v1
    container_name: kafka
    hostname: kafka
    command: start-kafka.sh
    expose:
      - 9092
    depends_on:
      - mqtt

  servers:
    image: tdocker.mgm-iot.com/moses:m11
    container_name: servers
    command: supervisord
    # command:
    #   - /bin/sh
    #   - -c
    #   - |
    #      /usr/local/bin/python /root/moses/back/web/create_table.py --env=docker
    #      /usr/local/bin/python /root/moses/back/bms/create_admin.py --env=docker
    #      /usr/bin/supervisord
    depends_on:
      - kafka
      - redis
      - hbase
      - mqtt
    ports:
      - "0.0.0.0:8000:8000"
      - "0.0.0.0:8100:8100"
      - "0.0.0.0:8200:8200"
      - "0.0.0.0:8600:8600"
      - "0.0.0.0:8800:8800"
      - "0.0.0.0:8900:8900"

  redis:
    image: tdocker.mgm-iot.com/redis:apline
    container_name: redis
    ports:
      - "6380:6379"

  hbase:
    image: tdocker.mgm-iot.com/hbase:v1
    # image: hadoop:v2
    container_name: hbase
    command: ./entrypoint.sh
    expose:
      - 8001
    volumes:
      - /home/zhou/n:/root/hbase-data # 本地hbase数据存储地址
  mqtt:
    image: eclipse-mosquitto:latest
    container_name: mqtt
    ports:
      - "1883:1883"
```
