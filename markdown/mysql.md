### shell操作
- 启动：mysql -u root -p
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
- union(连接两个以上的select语句，可以连接不同的表)：
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
- 每个系在2010年春季学期讲授一门课程的教师人数
- 教师平均工资超过42000美元的系(having, 嵌套子查询) r
- 找出所有的教师的姓名,以及他们所在系的名称和系所在的建筑物 (多关系查询, 用和不用自然连接及join using)
- 对于大学所有讲授课程的老师,找出他们的姓名以及所讲述的所有课程标识
- 找出满足下面条件的所有教师姓名,他们的工资至少比Biology系的某一个教师的工资要高(比Biology系教师的最低工资要高)(更名运算, 嵌套子查询)
- 找出所在建筑名称中包含watson子串的所有系名(like)
- 工资90000 - 10000的教师姓名 (between)
- union,intersect,except(默认都是distinct) all重复
 + 2009年秋季, 2010年春季或者两个学期都开课的所有课程
 + intersect
 + except
- 2009秋季和2010年春季同时开课的所有课程(**嵌套子查询**)
- 平均工资最高的系
- exists , 关系Ａ包含关系Ｂ:not exists (B except A)
 + 2009秋季和2010年春季同时开课的所有课程
 + 找出选修了Biology系开设所有课程的学生
- 找出所有在2009年最多开设一次的课程
- 找出所有在2009年最少开设两次的课程
- 所有系工资最大的系
- 打印每位教师的名字,以及他们的工资和所在系的平均工资(lateral, 自然连接)
- 找出最大预算的系
- 列出所有的系和他们拥有的教师数(标量子查询)
