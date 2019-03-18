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
- uuid1(): 基于时间戳
- uuid2(): 基于分布式计算环境 python没有
- uuid3(): 基于名字的md5散列
- uuid4(): 基于随机数
- uuid5(): 基于名字的sha-1散列


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
- 可迭代对象，迭代器，生成器(所有的生成器都是迭代器)
 + 可迭代对象(可直接作用于for循环的对象)
            使用 iter 内置函数可以获取迭代器的对象。如果对象实现了能返
        回迭代器的__iter__方法,那么对象就是可迭代的。序列都可以迭
        代;实现了 __getitem__ 方法,而且其参数是从零开始的索引,这种
        对象也可以迭代。

   + from collections import Iterable; isinstance('abc', Iterable) # True

 + 迭代器(可以被next()函数调用并不断返回下一个值，list, str, dict都不是迭代器，没有__next__或者next方法)
         标准的迭代器接口有两个方法。
        __next__
        返回下一个可用的元素,如果没有元素了,抛出 StopIteration
        异常。
        __iter__
        返回 self,以便在应该使用可迭代对象的地方使用迭代器,例如
        在 for 循环中。

         为什么list、dict、str等数据类型不是Iterator？
        这是因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。
        Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。
   + from collections import Iterator; isinstance('abc', Iterator) # False
   + Iterable->Iterator 使用iter for循环本质上就是通过不断调用next()函数实现的
               内置的 iter 函数有以下作用。
            (1) 检查对象是否实现了 __iter__ 方法,如果实现了就调用它,获取
            一个迭代器。
            (2) 如果没有实现 __iter__ 方法,但是实现了 __getitem__ 方法,
            Python 会创建一个迭代器,尝试按顺序(从索引 0 开始)获取元素。
            (3) 如果尝试失败,Python 抛出 TypeError 异常,通常会提示“C object
            is not iterable”(C 对象不可迭代),其中 C 是目标对象所属的类。
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
- except handler
 + 错误只能被捕获一次
 + finally 一定会执行，前面return 无效

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

### TLS,SSL,HTTPS
