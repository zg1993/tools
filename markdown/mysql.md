### 基本类型

- char(n) n指定长度
- varchar(n) n最大长度
- int
- smallint
- numeric(p,d)
- real, double precision
- float(n)



#### 引擎

MyISAM引擎的索引结构为**B+Tree**，其中B+Tree的**数据域存储的内容为实际数据的地址**，就是说它的索引和实际的数据是分开的，只不过是用索引指向了实际的数据，这种索引就是所谓的**非聚集索引**。

与MyISAM引擎的索引结构同样也是B+Tree，但是Innodb的索引文件本身就是数据文件，即**B+Tree的数据域存储的就是实际的数据**，这种索引就是**聚集索引**。这个索引的key就是数据表的主键，因此InnoDB表数据文件本身就是主索引。

并且和MyISAM不同，InnoDB的**辅助索引数据域存储的也是相应记录主键的值**而不是地址，所以当以辅助索引查找时，会先根据辅助索引找到主键，再根据主键索引找到实际的数据。所以Innodb不建议使用过长的主键，否则会使辅助索引变得过大。建议使用自增的字段作为主键，这样B+Tree的每一个结点都会被顺序的填满，而不会频繁的分裂调整，会有效的提升插入数据的效率

第一个重大区别是InnoDB的数据文件本身就是索引文件。从上文知道，MyISAM索引文件和数据文件是分离的，索引文件仅保存数据记录的地址。而在InnoDB中，表数据文件本身就是按B+Tree组织的一个索引结构，这棵树的叶节点data域保存了完整的数据记录。这个索引的key是数据表的主键，因此InnoDB表数据文件本身就是主索引。

第二个与MyISAM索引的不同是InnoDB的辅助索引data域存储相应记录主键的值而不是地址。换句话说，InnoDB的所有辅助索引都引用主键作为data域。

![img](https://images2015.cnblogs.com/blog/731178/201603/731178-20160320205632724-1223368895.jpg)这里以英文字符的ASCII码作为比较准则。聚集索引这种实现方式使得按主键的搜索十分高效，但是辅助索引搜索需要检索两遍索引：首先检索辅助索引获得主键，然后用主键到主索引中检索获得记录。

## 两种引擎的选择

　　大尺寸的数据集趋向于选择InnoDB引擎，因为它支持事务处理和故障恢复。数据库的大小决定了故障恢复的时间长短，InnoDB可以利用事务日志进行数据恢复，这会比较快。主键查询在InnoDB引擎下也会相当快，不过需要注意的是如果主键太长也会导致性能问题，关于这个问题我会在下文中讲到。大批的INSERT语句(在每个INSERT语句中写入多行，批量插入)在MyISAM下会快一些，但是UPDATE语句在InnoDB下则会更快一些，尤其是在并发量大的时候。了解不同存储引擎的索引实现方式对于正确使用和优化索引都非常有帮助，

例如知道了InnoDB的索引实现后，就很容易明白为什么不建议使用过长的字段作为主键，因为所有辅助索引都引用主索引，过长的主索引会令辅助索引变得过大。再例如，用非单调(可能是指“非递增”的意思)的字段作为主键在InnoDB中不是个好主意，因为InnoDB数据文件本身是一颗B+Tree，非单调(可能是指“非递增”的意思)的主键会造成在插入新记录时数据文件为了维持B+Tree的特性而频繁的分裂调整，十分低效，而使用自增字段作为主键则是一个很好的选择。

### shell操作

- 启动：mysql -u root -p(sql-js: \connect root@127.0.0.1  \sql)
- ; translate \G 按列显示
- systemctl status mysql.service 检查mysql的服务状态
- 数据库：关联表的集合
- mysql -u root -p (password: 123)
- show engines 系统支持存储引擎查看
 + 查看表信息：show table status from db_name where name='t2';
 + 查看建表语句：show create table t3;
- show databases;
- use mysql;
- show tables;
- describe user;
- select *(field) from user;
- insert(插入)：insert into table (field1, field2) values (value1, value2);
- where(有条件的选取数据，and or用来连接多个条件): select * from user where user='root';
- update(修改数据)：update table_name set field1=new_value1, field2=new_value2 where clause;
- delete(删除)：delete from table where clause;(未指定where，删除所有记录)
- like(模糊查询)： select filed1 from table where field1 like '%t';
 + '%': 任意多个字符
 + '_': 任意一个字符
- union(连接两个以上的select语句， 连接不同的表)：
 + distinct(default 删除重复元素), all(返回所有结果)
- order by(排序)：select * from table order by field [ASC(默认升序) [DESC]];
- group by(分组)
- join(多表查询)


### 配置文件
- 跳过密码验证： /etc/mysql/mysql.conf.d/mysqld.cnf
      [mysqld] skip_grant_tables


### 常用语句
- select count(*) 和order by是最频繁的
### msyql的连接操作
- 开放3306端口供局域网内其它机器查看：[csdn](https://blog.csdn.net/freezingxu/article/details/77088506)

### sql
- schema: 模式  类型定义
- relation: 关系（表） 变量声明
- instance: 实例  变量赋值


### python
##### MySQLdb(C模块，使用mysql客户端中的mysql协议实现相连接，更快，需要c库才能工作)
##### mysql-connector（python模块，在python中重新实现mysql协议，比较慢，不需要c库，安装方便）
#### pymysql (python3 连接mysql 取代mysqldb)

### practice
- 每个系的平均工资(3.7.2分组聚集)
- 每个系在2010年春季学期讲授一门课程的教师人数 *(distinct)
- 教师平均工资超过42000美元的系(having, 嵌套子查询) r
- 找出所有的教师的姓名,以及他们所在系的名称和系所在的建筑物 (多关系查询, 用和不用自然连接及join using)
- 对于大学所有讲授课程的老师,找出他们的姓名以及所讲述的所有课程标识
- 找出满足下面条件的所有教师姓名,他们的工资至少比Biology系的某一个教师的工资要高(比Biology系教师的最低工资要高)(更名运算, 嵌套子查询)
- 找出所在建筑名称中包含watson子串的所有系名(like mysql 默认不区分大小写, 区分:like binary )
- 工资90000 - 10000的教师姓名 (between)
- union,intersect,except(默认都是distinct) all重复
 + 2009年秋季, 2010年春季或者两个学期都开课的所有课程 *
 + intersect *
 + except *
- 2009秋季和2010年春季同时开课的所有课程(**嵌套子查询**)
- 平均工资最高的系 **
- exists , 关系Ａ包含关系Ｂ:not exists (B except A) **
 + 2009秋季和2010年春季同时开课的所有课程
 + 找出选修了Biology系开设所有课程的学生 **
- 找出所有在2009年最多开设一次的课程 *
- 找出所有在2009年最少开设两次的课程
- 所有系工资最大的系
- 打印每位教师的名字,以及他们的工资和所在系的平均工资(lateral, 自然连接)
- 找出最大预算的系
- 列出所有的系和他们拥有的教师数(标量子查询)
