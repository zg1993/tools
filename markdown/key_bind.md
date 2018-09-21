# 1、Atom
- 同步配置
 1. apm install sync-settings
 1. paste gitid and personalaccesstoken
 2. sync-setting:restore
### 1.1、Key Binding:
  - 查找文件 ctrl-t
  - 窗口切换(两个窗口) ctrl-k ctrl-n(p)
  - 多窗口切换 ctrl-k ctrl-direction
  - custom
     - save ctrl-i

### 1.2、MarkDown基本语法：

加粗、斜体
- *dan*
- _data_
- **double**
- __double__

列表
- order
   1. item1
   1. item2
   1. item3
- disorder
   * item1
   * item2
   * item3

多级列表(+ front space)
* itkem1
 + itme1.1
* item2
 + item2.1

列表项目有多个段落
* one

    正文skkkkkkkkkkk

* two

    acticle

链接、图片
- this is [an example](http://baidu.com) inlink link.
- ![import picture](/home/zhou/Pictures/jinmubiao.)


# 2、Emacs
### 2.1 Key Binding
- switch Shell: alt+x shell
- split screen: alt+x 3
- switch screen: ctrl+x o
- manual: ctrl+h t
- pageup: ctrl+v
- set-mark-command: ctrl+i (copy)
 + set-mark-command
 + move
 + alt+w(copy)/ctrl+w(cut)
 + ctrl+y (paste)
- 重复上一个命令: ctrl-x z
# 3、Sublime
### 3.1 Key Binding
- split screen: alt+Shift+2
- switch screen: ctrl+k ctrl+p(n) (like Atom)
- pageup: ctrl+k ctrl+f

# 4、Git
### 4.1 Command
- 添加一个远程库：git remote add origin git@github.com:name/project.git
- 第一次push：git push -u origin master
- 新建分支后关联远程分支：
 + git branch -u origin/dev
 + git branch --set-upstream-to origin/dev
- 查看本地分支和远程的关联情况：git branch -vv
- 撤销分支关联：git branch --unset-upstream
- 合并分支
  + 直接合并：git merge dev
  + 根据commit_id合并：git cherry-pick commid_id
  + conflict HEAD 本地的内容
- 删除分支：git branch -d dev
