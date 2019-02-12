## 1.str unicode operation

```python
# format 特殊字符
In [839]: u"^[\u4e00-\u9fff\w]{{{0},{1}}}$".format(1,3)
Out[839]: u'^[\u4e00-\u9fff\\w]{1,3}$'
```


## 2. Test
#### 2.1 unittest


## 3. time, datetime
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
 - from __future__ import absolute_import
 - python -O 忽略assert执行
 - python 关键字参数和可变参数在元编程时不可避免
 - s1 = {0, 1, 2} s2 = {1, 4}
  + 差集：s1 - s2 = {0, 2}
  + 对称差集：s1 ^ s2 = {0, 2, 4}

 #### 模块和包相关
 - 和包在同一目录的py可以使用包
 - 在包内，既可以使用相对路径也可以使用绝对路径来导入
 - 包相对模块的使用：python3 -m mypackage.A.spam # Relative imports work
