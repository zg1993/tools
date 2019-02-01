#### python 高级编程
###### PEP8
1. 除了模块__init__之外，模块名称都使用不带下划线的小写字母命名
2. 字典命名：key_value example: person_address = {'Bill': 'road '}
3. 如果非要用用id os这样的变量名，请加加后缀下划线id_ os_
- 类名
 + 常见的是使用表示其类型和特性的后缀(SQLEngine, MimeType, StringWidget, TestCase)
 + 基类使用Base或Abstract前缀
- 模块和包的名称： 简短，使用小写字母，不使用下划线
 + 如果实现了一个协议，通常使用lib前缀
- 分解代码
 + 一个函数和方法最好不要超过一个屏幕(25~30)行
 + 类的方法10个左右
 + 一个模块不超过500行


#### 编码大全

##### 选择好的变量名注意事项
- 最重要的命名事项: 完全准确的描述出该变量所代表的事物.

| 变量用途 | 好名字 | 坏名字 |
| -- | -- | -- |
|到期支票累计额 | runningTotal, checktotal| checks|
|高速列车运行速度|vekicity|v|
|当期那日期|currentDate, todayDate|current, date|
|每页行数|linesPage|lines|
- 以问题为导向：表达what而不是how
- 最适当的名字长度
- 变量名字的效果范围
- 变量名中的计算值限定词:
 + total, average, max, min, record, string, pointer限定词加到名字最后(变量名主要含义部分在前面) revenueTotal总收入
 + **num放在变量名开始表示总数numCustomers(复数)员工总数, 放在结束位置表示下标customerNum**
- 变量名字中的常用反义词
 + begin/end
 + first/last
 + locked/unlocked
 + min/max
 + next/previous
 + old/new
 + opened/closed
 + visible/invisible
 + source/target
 + source/destination
 + up/down




##### 为特定类型数据命名
- 循环下标
 + 循环内使用: i, j, k
 + 嵌套循环：使用更有意义的名字
- 状态变量: (status 和 flag定义比较模糊)machinestatus, ReportType
- 临时变量: 使用多次的临时变量取一个比temp更有意义的名字, discriminant
- 布尔变量:　取一个比is has 前缀更有意义的名字
 + done: 某件事情已经完成，由于循环结束或者一些其他的操作完成，完成之前为false
 + success 或者 ok: 某操作是否成功, 失败时为false, **如果可以,使用更具体的名字代替success,
 example 程序执行成功ProcessingComplete表示, 如果是找到某值程序执行成功,用found**
 + found: 表示某值已经找到,
 + error: 表示有错误发生,错误发生之前为false,发生为true


##### 非正式命名规则
- 常见的自定义类型缩写:
 + suf(suffix) 后缀
 + pre(prefix) 前缀
 + src(source)
 + dst(destination)
 + ch(character) 字符
 + doc(document) 文档
 + pa(paragraph) 段落
 + scr(screen region) 屏幕区域
 + sel(selection) 选中范围
 + wn(window) 窗体
