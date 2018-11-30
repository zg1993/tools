## 1.str unicode operation

```python
# format 特殊字符
In [839]: u"^[\u4e00-\u9fff\w]{{{0},{1}}}$".format(1,3)
Out[839]: u'^[\u4e00-\u9fff\\w]{1,3}$'
```


## 2. Test
### 2.1 unittest


## 3. time, datetime
- 时间戳转化字符串

      time.strftime(format, time.localtime(timestamp))
      datetime.utcfromtimestamp(timestamp).strftime(format)

- 字符串转化为时间戳

      time.mktime(time.strptime('18-10-23 16-12-32', '%y-%m-%d %H-%M-%S'))

## site-packages dist-packages
- site-packages: 通过python setup.py install(通过源码安装)
- dist-packages:
 + /usr/lib/python2.7/dist-packages: sudo
 + /usr/local/lib/python2.7/dist-packages:
