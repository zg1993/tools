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
- 跳转到指定行: M-g M-g
- 替换: M-%
# 3、Sublime
### 3.1 Key Binding
- split screen: alt+Shift+2
- switch screen: ctrl+k ctrl+p(n) (like Atom)
- pageup: ctrl+k ctrl+f
- 回到上一个页面: alt+-

# 4、Git
### /etc/hosts
```
#github
151.101.185.194  github.global.ssl.fastly.net
192.30.253.112   github.com
```
修改生效
```bash
 /etc/init.d/networking restart
```
### 4.1 Command
```bash
$ git config --global user.name "John Doe"
$ git config --global user.email johndoe@example.com
```
- ssh-keygen copy pub->setting ssh key
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
- 本地已存在分支关联远程分支： git pull origin master, git branch --upstream-to=...
- 创建dev分支并且推送到远程：git push origin dev
- 拉取远程分支并创建本地分支
 + (其他人使用 git fetch origin, git checkout -b dev origin/dev)
 + git fetch origin 远程分支:本地分支
- 从本地仓库里移除: git rm -r --cached lisp/derby.log
- git reflog 查看分支的所以操作记录（包括已经被删除的提交记录
- git log：
 * --author='zhou.gang'
 * --grep='docker'  commit的内容
 * -p 显示详情
 * -2 显示最近两次的更新
 * 按文件：-- for.py bar.py
 * 按范围：master..dev
 * 按日期：--after="2019-1-1" --before=""

### 4.2 概念
- 工作区域：working directory, staging area ,git directory(repository)
- 文件的状态：modified(作了修改没有放到暂存区), staged(已修改并已提交到暂存区), commited（git 目录保存着特定版本的文件）

### 查看提交记录
- git log --oneline --graph -- dir

### 分支合并
- 衍合：git checkout dev, git rebase master, solve conflict, add , git rebase --continue, finally git commit -m "rebase", git checkout dev, git reset --hard commit_id, git checkout master ,git merge dev

### 常用技巧
- 快速提交：git commit -a
-

### 分支管理 与 合并
 - merge 后撤消：git reset --hard 【merge前的版本号】
 - git checkout master 1.c: 1.c 文件改成master分支head版本

### 4.3 远程分支的管理
 - 查看：git remote show origin(本地分支的查看：git branch -vv)
 - 删除远程分支：git push origin :delete_branch

### 4.4 撤销操作
- 暂存：git stash list --date=local
- add后：git reset HEAD file_name
- commit后（回到上一步，git reset --soft HEAD^）:
 + 追加提交：git add file_name; git commit --amend
 + 提交重置：　git reset --hard HEAD~3
 + 回退到某个版本：git reset --hard commit-id
 + 回退到上版本：git reset --hard HEAD^
   + git reset –mixed：此为默认方式，不带任何参数的git reset，即时这种方式，它回退到某个版本，只保留源码，回退commit和index信息
   + git reset –soft：回退到某个版本，只回退了commit的信息，不会恢复到index file一级。如果还要提交，直接commit即可
   + git reset –hard：彻底回退到某个版本，本地的源码也会变为上一个版本的内容
