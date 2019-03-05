## 1.str unicode operation

```python
# format 特殊字符
In [839]: u"^[\u4e00-\u9fff\w]{{{0},{1}}}$".format(1,3)
Out[839]: u'^[\u4e00-\u9fff\\w]{1,3}$'
```


## 2. Test
#### 2.1 unittest


## 3. time, datetime, dateutils模块
- datetime模块 datetime date 相互转化()
  ```python
  # convert date to datetime (int python)
  dt = datetime.now()
  d = date.today()
  datetime(year=d.year, month=d.month,day=d.day)  # 338 ns per loop
  datetime.fromordinal(d.toordinal())             # 248 ns per loop
  datetime(*d.timetuple()[:-4])                   # 826 ns per loop
  datetime.combine(d, datetime.min.time())        # 348 ns per loop

  # convert datetiem to date
  dt.date()
  ```
- dateutils 获取给定时间段的每一天

- 时间戳转化字符串

      time.strftime(format, time.localtime(timestamp))
      datetime.utcfromtimestamp(timestamp).strftime(format)

- 字符串转化为时间戳

      time.mktime(time.strptime('18-10-23 16-12-32', '%y-%m-%d %H-%M-%S'))


## anacoda and pyenv
#### anacoda
- 查找包并安装
 + anaconda search -t conda package-name
 +

## 4. standard library
#### 4.1 uuid

#### 4.2 itertools 内置的迭代器

## 5. site-packages dist-packages
- site-packages: 通过python setup.py install(通过源码安装)
- dist-packages:
 + /usr/lib/python2.7/dist-packages: sudo
 + /usr/local/lib/python2.7/dist-packages:


## 常用知识



- MixIn多重继承时父类方法相同，继承最前面的 A(B, C)
- from __future__ import absolute_import
- python -O 忽略assert执行
- python 关键字参数和可变参数在元编程时不可避免
- s1 = {0, 1, 2} s2 = {1, 4}
  + 差集：s1 - s2 = {0, 2}
  + 对称差集：s1 ^ s2 = {0, 2, 4}
- 过滤掉list里面的无效值
```python
In [38]: filter(None, [None, False, 0, [], {}, 1])
Out[38]: [1]
```

 #### 模块和包相关
 - 和包在同一目录的py可以使用包
 - 在包内，既可以使用相对路径也可以使用绝对路径来导入
 - 包相对模块的使用：python3 -m mypackage.A.spam # Relative imports work



## 问题
### 常用术语：
- 归约函数：接收可迭代对象返回单个结果
### 常用技巧：
- 匿名函数捕获变量值
```python
>>> x = 10
>>> a = lambda y, x=x: x + y
>>> x = 20
>>> b = lambda y, x=x: x + y
>>> a(10)
20
>>> b(10)
30
>>>
```
 + 如果需要在定义是绑定变量，通过使用函数默认值参数
 ```python
 >>> funcs = [lambda x, n=n: x+n for n in range(5)]
>>> for f in funcs:
... print(f(0))
...
0
1
2
3
4
>>>
 ```

#### 1.python2 python3区别
- 统一了字符编码的支持：
    + 默认编码的改变2sys.getdefaultencoding(): ascii python3 为utf8
    + 2里字符串unicode（文本字符串）, str（字节序列）3里str表示字符串，byte表示字节序列，任何需要写入文本或者网络传输的数据都只接收字节序列，这就从源头上阻止了编码错误的问题
- python3里旧式类的去除，经典类（旧）和新式类的区别：
   + 继承搜索顺序发生改变，经典类深度优先，新式类广度优先
   + 旧类 a=A() type(a) 显示为 <type 'instance'> 新式：__main__.A
- print 变成了函数
- python2 中很多返回列表对象的函数在3里都改成了返回类似于迭代器的对象，**迭代器的惰性加载特性**操作数据更有效率

#### 2.python闭包
- 介绍：闭包指延伸了作用域的函数，其中包含函数定义体中的引用、但是不在定义体中定义的非全局变量，关键是它能访问定义体之外的非全局变量。
- 总结：闭包是一种函数，它会保留定义函数时存在的自由变量的绑定，这样调用函数时，虽然定义作用域不可用了，但是仍能使用那些绑定。（nonlocal python3 解决闭包内不可变类型的更新操作）
#### 3.GIL golbal interpreter lock
- GIL是cpython解释器的局限，与python语言无关，Jython和Ironpython没有这种限制
