### 1.java
tar -zxvf jdk.tar.gz -C /usr/jdk
/etc/profile
```
export JAVA_HOME=/usr/jdk/jdk1.8.0_144
export JRE_HOME=${JAVA_HOME}/jre
export CLASSPATH=.:${JAVA_HOME}/lib:${JRE_HOME}/lib
```


### 1.linux相关软件
- [rar](https://blog.csdn.net/scorpio3k/article/details/49006603)


### atom 插件安装
- 查看已安装插件:　apm ls
- 通过atom直接安装
- 通过命令行下载安装1:
  1. -->打开终端
  1. -->输入cd ~/.atom/packages，切换到atom安装包目录。
  2. apm install markdown-table-editor
- 通过命令行安装2:
  1. -->在[atom安装包搜索页面](https://atom.io/packages)搜索插件，例如:vim.搜索vim结果列表展示页面.
  2. -->终端输入git clone [代码托管地址]
  3. cd markdown-table-editor
  4. apm install

### common lisp
- sudo apt-get install emacs sbcl lisp slime
- .emacs.d/init.el
```lisp
(setq inferior-list-program "/usr/bin/sbcl")
(add-to-list 'load-path "/usr/share/emacs24/site-lisp/slime/")
(require 'slime)
```
- 进入 M-X slime
