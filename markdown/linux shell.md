### 1.Command frequent
- Find
    1. find . | xargs grep -ri "IBM"
    2. find . | xargs grep -ri "IBM"
    3. 查找目录 find / -name "IBM" -type d
    4. find / -name "IBM" -print
- awk
    1. ls -l | awk '{if($5>4096){print $0}}'
    2. ls -l | awk 'BEGIN {size=0;} {size+=size;} END{print size}'
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
