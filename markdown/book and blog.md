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
