### csapp
##### 1. cache 写策略
    写命中：直写(write-through)、写回(write-back)
    写不命中：写分配(write-allocate)、非写分配(not-write-allocate)
    直写高速缓存通常是非写分配，写回高速缓存通常是写分配
- 直写：更新高速缓存，然后立即将高速缓存的块写到低一层
- 写回：更新高速缓存，将对应的缓存块标记为dirty。当替换算法要驱逐对应的块时，才将其写到低一层。
- 写分配： 加载低一层的块到高速缓存，然后更新这个高速缓存
- 非写分配： 避开高速缓存，直接更新低一层

**write-through cache with not write allocation**
![](assets/markdown-img-paste-20181011145745996.png)

**A write-back cache with write allocation**
![](assets/markdown-img-paste-20181011145752643.png)

##### 并发流

![](assets/markdown-img-paste-20181015154409113.png)

- 逻辑流: PC值的序列
- 并发流: 一个逻辑流的执行在时间上与另一个流重叠(A and B, A and C)
- 并行流: 并发流的一个真子集,如果俩个流并发运行在不同的处理器或者计算机上,称为**并行流**

### scheme
#### 基本语法
- [教程](https://www.ibm.com/developerworks/cn/linux/l-schm/index1.html)
- 过程定义的一般形式: (define (<name> <formal parameters>) <body>)
- 条件表达式: (cond (<p1> <e1>)(<p2> <e2>))
- if表达式: (if <predicate> <consequent> <alternative>)
- 基本谓词: > < =
- 逻辑复合谓词：　and or not
- let表达式:
       (let ((<var><exp>)
             (<var1><exp1>))
             <body>)
- 代换模型:
 + 应用序求值:　先求值参数而后应用
 + 正则序求值:　完全展开而后归约
#### mit-scheme
- 进入控制台(eidt 'console)
- alias edwin=$'mit-scheme -eval "(edit \'console)"'
#### 1.构造过程抽象
##### 1.1 程序设计的基本元素
- 基本表达形式: 语言最简单的个体
- 组合的方法: 构造复合的元素
- 抽象的方法: 为复合对象命名, 并将其当做单元去操作
- 概率算法: 费马检查


### math
#### 取余(rem)和取模(mod)
- 取余商值向零舍入
```
5 mod 3 = 2
5 rem 3 = 2
-5 mod 3 = 1
-5 rem 3 = -2
```

### redis实战
进程同时获取到锁
      然而，锁超时时，我们不能简单地使用 DEL 命令删除键 lock.foo 以释放锁。考虑以下情况，进程P1已经首先获得了锁 lock.foo，然后进程P1挂掉了。进程P2，P3正在不断地检测锁是否已释放或者已超时，执行流程如下：

      P2和P3进程读取键 lock.foo 的值，检测锁是否已超时（通过比较当前时间和键 lock.foo 的值来判断是否超时）
      P2和P3进程发现锁 lock.foo 已超时
      P2执行 DEL lock.foo命令
      P2执行 SETNX lock.foo命令，并返回1，即P2获得锁
      P3执行 DEL lock.foo命令将P2刚刚设置的键 lock.foo 删除（这步是由于P3刚才已检测到锁已超时）
      P3执行 SETNX lock.foo命令，并返回1，即P3获得锁
      P2和P3同时获得了锁
      ---------------------
      作者：haozlee
      来源：CSDN
      原文：https://blog.csdn.net/lihao21/article/details/49104695
      版权声明：本文为博主原创文章，转载请附上博文链接！

### 软件开发相关
#### 开发过程
1. 需求分析
2. 设计
3. 编码
4. 测试

#### 开发方法
任何一个软件项目都可以从四个方面入手进行改善：加强交流；从简单做起；寻求反馈；勇于实事求是 - 百度百科.极限编程
- 极限编程
