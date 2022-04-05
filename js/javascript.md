### 基本概念

1、node.js 通过JavaScript语言开发web服务端的东西。node.js有非阻塞，事件驱动I/O等特性，从而让高并发在轮询和comet构建的应用中成为可能。（Javascript的运行环境，使其脱离浏览器运行）

2、Ajax不用每次都请求一个完整的新页面，只需获取部分信息就行。

3、ECMAScript：语言标准，JavaScript是对这种标准的实现。

4、.html 和 .js 文件

 - html 通常放到HTML的head里<script>.js代码.</script>
 - js /static/js/abc.js js文件更利于维护代码，并且多个页面可以引用同一份js文件

5、从代码编译的角度说的话，单引号在JS中被浏览器（IE，Chrome，Safari）编译的速度更快（在FireFox中双引号更快）。

6、html css

##### 浏览器版本查看和相关问题

### 数据类型



### ![img](https://pic4.zhimg.com/80/v2-4dbbcf0790529089cc9dde6d716e7397_1440w.jpg)

1、null undefined 都表示无效的值，该类型都只有一个值

- **常见问题：字符串有最大长度吗？** 

  (String 用于表示文本数据。String 有最大长度是 2^53 - 1，这在一般开发中都是够用的，但是有趣的是，这个所谓最大长度，并不完全是你理解中的字符数

  String 的意义并非“字符串”，而是字符串的 UTF16 编码，我们字符串的操作 charAt、charCodeAt、length 等方法针对的都是 UTF16 编码。所以，字符串的最大长度，实际上是受字符串的编码长度影响的  现实中大概没有浏览器允许这么长的字符串。Firefox 的长度限制是(2e + 30) -2 )

- 为什么有的编程规范要求用 void 0 代替 undefined？(主要原因在于避免 undefined 值被重写带来的风险。现代浏览器中，全局变量 undefined 是不可写的，如果不考虑兼容旧的浏览器，那么这个问题就不用太过在意。)

  ```/**
  /**
   * IE8 浏览器
   */
  var value;
  console.log(value === undefined); //true
  // 重写 undefined
  undefined = 'hi';
  console.log(value === undefined); //false
  ```

  

- undefined（undefined 一般都来自于某个表达式最原始的状态值） 四种出现情况

  ```javascript
  // 1
  var a;
  console.log(a); // undefined
  // 2
  Object.foo // 访问不存在的对象
  // 3函数定义了形参，但没有传实参
  function fn(a) {
      console.log(a); // undefined
  }
  fn();
  // 4 使用void对表达式求值
  void 0 ; // undefined
  void false; //undefined
  void []; //undefined
  void null; //undefined
  void function fn(){} ; //undefined
  ```

- null 类型 Null（ 在内存里的表示就是，栈中的变量没有指向堆中的内存对象） null 有属于自己的类型 Null，而不属于Object类型，typeof 之所以会判定为 Object 类型，是因为JavaScript 数据类型在底层都是以二进制的形式表示的，二进制的前三位为 0 会被 typeof 判断为对象类型，而 null 的二进制位恰好都是 0 ，因此，null 被误判断为 Object 类型。 typeof null == 'object'  其实，我们可以通过另一种方法获取 null 的真实类型：

  ```javascript
  Object.prototype.toString.call(null) ; // [object Null]
  Object.prototype.toString.call(undefined) ; // [object Undefined]
  ```

### 原型链

通过一个构造函数创建出来的多个实例，如果都要添加一个方法，给每个实例去添加并不是一个明智的选择。这时就该用上原型了。

在实例的原型上添加一个方法，这个原型的所有实例便都有了这个方法。

```
var M = function (name) { this.name = name; }
var o3 = new M('o3')var 
o5 = new M()
o3.__proto__.say=furnction(){
   console.log('hello world')
}

o3.say()
o5.say()
```

按照JS引擎的分析方式，在访问一个实例的属性的时候，现在实例本身中找，如果没找到就去它的原型中找，还没找到就再往上找，直到找到。这就是原型链。(当我们用`obj.xxx`访问一个对象的属性时，JavaScript引擎先在当前对象上查找该属性，如果没有找到，就到其原型对象上找，如果还没有找到，就一直上溯到`Object.prototype`对象，最后，如果还没有找到，就只能返回`undefined`。)

