# 1.JAVA 基础

## 1.1 安装和执行
 - CLASSPATH 和 -cp 可以指定类搜索路径（解决 错误: 找不到或无法加载主类）

## 1.2 java 关键字
### 继承
- extends
 + 类继承类(java 不支持多继承)
 + 接口继承接口
![](assets/markdown-img-paste-20181010160054285.png)
- implements 类继承接口（变相支持多继承）

```java
public interface A {
    public void eat();
    public void sleep();
}

public interface B {
    public void show();
}

public class C implements A,B {
}
```

### 接口
- interface 抽象方法的集合

### 重写(Override)和重载(Overload)
- Override
 + 子类对父类
 + 参数列表和返回类型不改变
- Overload
 + 发生在一个类里面
 + 参数类表必须改变

### 修饰符
##### (1)访问修饰符
      访问控制修饰符保护对类、变量、方法、构造方法的访问
- default
- public
- private
- protect

##### (2)非访问修饰符
- static
 + 静态变量 又称类变量
 + 静态方法 不能使用类的非静态变量
- final
 + final方法 可以被继承，不能被修改
 + final类 不能被继承
- abstract
- synchronized volatile

### 线程安全
- StringBuffer(synchronized 同步的) StringBuilder
- Hashtable(synchronized) HashMap
