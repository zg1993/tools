### shell操作
- 数据库：关联表的集合
- mysql -u root -p (password: 123)
- show databases;
- use mysql;
- show tables;
- describe user;
- select *(field) from user;
- insert(插入)：insert info table (field1, field2) values (value1, value2);
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

### sql
- schema: 模式  类型定义
- relation: 关系（表） 变量声明
- instance: 实例  变量赋值
