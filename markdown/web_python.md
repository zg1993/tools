### 1.http请求相关的模块
##### urllib, urllib2
- 是urllib提供urlencode方法用来GET查询字符串的产生，而urllib2没有
- urllib2可以接受一个Request类的实例来设置URL请求的headers
##### urllib3
* Thread safety.
* Connection pooling.
* Client-side SSL/TLS verification.
* File uploads with multipart encoding.
* Helpers for retrying requests and dealing with HTTP redirects.
* Support for gzip and deflate encoding.
* Proxy support for HTTP and SOCKS.
* 100% test coverage.
##### requests



### 2.django
##### occurence questions:
- 使用pymysql(project/__init__.py):
      import pymysql
      pymysql.install_as_MySQLdb()
- 初始化数据库：python manage.py migrate
- (1054, u"Unknown column 'focus_article.num_favorites' in 'field list'"): model里字段名和数据库不一致
##### migrate
- python manage.py makemigrations: model层转为迁移文件migration
- python manage.py showmigrations: 查看迁移文件的执行状态
- python manage.py migrate: 通过迁移文件更新数据库


##### read source code
- metaclass
- functools.total_ordering (比较函数)
- property
  * inspect: isclass
- importlib
