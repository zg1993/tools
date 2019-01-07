## linux 一、系统管理
#### 1.1 文件系统目录
- [b](http://laiguowei2004.blog.163.com/blog/static/368290002011126115625904/)
- [b](https://blog.csdn.net/Alvern_Zhang/article/details/48392895)
#### 1.2 系统相关命令（systemd）
http://www.ruanyifeng.com/blog/2016/03/systemd-tutorial-commands.html
- hostnamectl: 当前主机的信息

#### 1.3 系统内存管理
- 缓存释放 echo 3 > /proc/sys/vm/drop_caches
 + 0 – 不释放
 + 1 – 释放页缓存
 + 2 – 释放dentries和inodes
 + 3 – 释放所有缓存

## linux 系统安装
#### ubuntu-server:
 - rufus(制作工具) :　
  + [百度知道](https://baijiahao.baidu.com/s?id=1616490790245132419&wfr=spider&for=pc)
  + [2](https://baijiahao.baidu.com/s?id=1615083412157188758&wfr=spider&for=pc)




### 1.Command frequent
- Find
    1. find . | xargs grep -ri "IBM"
    2. find . | xargs grep -ri "IBM"
    3. 查找目录 find / -name "IBM" -type d
    4. find / -name "IBM" -print
- awk
    1. ls -l | awk '{if($5>4096){print $0}}'
    2. ls -l | awk 'BEGIN {size=0;} {size+=size;} END{print size}'
    3. ls | awk 'BEGIN {size=0;} {cmd="docker image ls|grep "$0;system(cmd);} END{print size}' (awk执行命令)
    4. ls | awk '{cmd="docker image ls|grep java";system(cmd);}'
- other
 + 十进制二进制的转换
 + 10->2 echo "obase=2;3"|bc 11
 + 2->10 echo "obase=10;ibase=2;11"|bc 3
- 特殊字符的含义
  +  #: super user
  +  $: user
  +  单引号被视为字符串
  +  $? 状态值 (status variable)

    一般来说，UNIX(linux) 系统的进程以执行系统调用exit()来结束的。这个回传值就是status值。回传给父进程，用来检查子进程的执行状态。
   一般指令程序倘若执行成功，其回传值为 0；失败为 1。
  +  $$ 当前shell的PID

### 2.进程相关
- jobs: 查看后台运行进程
- fg %jobnumber: 将后台运行的命令掉至前台

### 3.常用功能
- 查看局域网内的所有ip
  + cat /proc/net/arp 查看arp缓存表
  + nmap -sP 192.168.1.0/24 进行ping扫描
    + 其它主机端口开放情况：nmap ip(nmap -sS ip)
- 访问共享文件：smb://ip
- 查看软件安装位置： which virtualbox， locate VBox
- 通过端口号查找进程： lsof -i:port
 + fd: 111u (u表示文件被打开并处于读取/写入模式 大写的w应用程序对整个文件的写锁)
- scp文件拷贝
 + 远程到本地： scp root@tmqtt:/root/soft/hadoop-2.8.0.tar.gz
 + /home/zhou/software/

#### 3.2 ip 域名 端口 网络相关
 - 域名对应ip：nslookup ip

 ##### nmap
 ##### netstat
 ##### iptables
 ##### nslookup
 ##### nc

### 4.expand
- /sbin/: 基本的系统命令 （只有管理员能运行）
- /bin/：普通的基本命令


### 5.磁盘相关
- lsblk -f: 显示分区基本信息
- du:　查看文件和文件夹大小
  * du -sh　可以指定路径默认当前路径: s:sum  h:human 查看当前文件的总大小
  * --max-depth=1 指定遍历目录深度: du --max-depth=1 -h


- df: 磁盘空间查看
- 磁盘分区相关: [blog](https://blog.csdn.net/hejiamian/article/details/52031910)

### 文件
##### 文件移动,拷贝
- cp -r lua csapp/lua: 在csapp目录下创建lua目录,将lua下的内容copy

### 系统配置
#### /proc
```
# 总核数 = 物理CPU个数 X 每颗物理CPU的核数
# 总逻辑CPU数 = 物理CPU个数 X 每颗物理CPU的核数 X 超线程数

# 查看物理CPU个数
cat /proc/cpuinfo| grep "physical id"| sort| uniq| wc -l

# 查看每个物理CPU中core的个数(即核数)
cat /proc/cpuinfo| grep "cpu cores"| uniq

# 查看逻辑CPU的个数
cat /proc/cpuinfo| grep "processor"| wc -l

查看CPU信息（型号）
cat /proc/cpuinfo | grep name | cut -f2 -d: | uniq -c
查看内 存信息
# cat /proc/meminfo
```
### 脚本
##### １．文件测试 　字符串测试

    =	等于则为真
    !=	不相等则为真
    -z 字符串	字符串的长度为零则为真
    -n 字符串	字符串的长度不为零则为真

    -文件名	如果文件存在则为真
    -r 文件名	如果文件存在且可读则为真
    -w 文件名	如果文件存在且可写则为真
    -x 文件名	如果文件存在且可执行则为真
    -s 文件名	如果文件存在且至少有一个字符则为真
    -d 文件名	如果文件存在且为目录则为真
    -f 文件名	如果文件存在且为普通文件则为真
    -c 文件名	如果文件存在且为字符型特殊文件则为真
    -b 文件名	如果文件存在且为块特殊文件则为真

### 正则
![正则](assets/markdown-img-paste-2018103112094450.png)
![POSIX](assets/markdown-img-paste-2018103112112796.png)
