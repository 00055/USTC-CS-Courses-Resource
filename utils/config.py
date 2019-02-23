# coding: utf-8
import os.path

HOST = 'https://raw.githubusercontent.com/'
OWNER = 'mbinary' #'USTC-Courses'  #'mbinary'#
REPO = 'USTC-CS-Courses-Resource'
BRANCH = 'master'


PATH = os.path.join(HOST,OWNER,REPO,BRANCH)


WALKDIR = os.path.abspath('.')

TARDIR = '/mnt/d/blogfile/blog/source/ustc-cs'
if not os.path.exists(TARDIR):
    TARDIR = 'docs'

IGNORE = ['utils','docs','__pycache__']

HTML = '''
---
title: ustc-cs-courses-resource
---

<!--
<head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8">
  </head>
  -->
  <body>
     	<div><h2>
                <a href="../index.html">&nbsp;&nbsp;<i class="fa fa-level-up"></i>&nbsp;&nbsp;</a>:
                /{cur}
            </h2>
        <div><span> 根据拼音排序</span></div>
        </div>
        <h2>Directories</h2>
        <ul>
        {dirLst}
        </ul>

        <h2>Files</h2>
        <ul>
        {fileLst}
        </ul>

        <div style="text-decration:underline;display:inline">
        <a href="https://github.com/mbinary/USTC-CS-Courses-Resource.git" target="_blank" rel="external"><i class="fa fa-github"></i>&nbsp; Github</a>
        <a href="mailto:&#122;huheqin1@gmail?subject=反馈与建议" style="float:right" target="_blank" rel="external"><i class="fa fa-envelope"></i>&nbsp; Feedback</a>
        </div>

        {readme}
    </body>
'''

#* 非zip, 非以'.'开头的文件多于 3 个的目录下都有个 zip 文件：`-DIRECTORY 目录下的\d+个文件.zip`,包含当前目录下的一些文件, 这样方便大家一键下载. (在 git commit前, 运行 `./before__commit.sh`可以自动生成)

README=r'''
# 中国科学技术大学课程资源
[![Stars](https://img.shields.io/github/stars/mbinary/USTC-CS-Courses-Resource.svg?label=Stars&style=social)](https://github.com/mbinary/USTC-CS-Courses-Resource/stargazers)
[![Forks](https://img.shields.io/github/forks/mbinary/USTC-CS-Courses-Resource.svg?label=Fork&style=social)](https://github.com/mbinary/USTC-CS-Courses-Resource/network/members)
[![repo-size](https://img.shields.io/github/repo-size/mbinary/USTC-CS-Courses-Resource.svg)]()
[![Contributors](https://img.shields.io/github/contributors/mbinary/USTC-CS-Courses-Resource.svg)](https://github.com/mbinary/USTC-CS-Courses-Resource/graphs/contributors)
[![License](https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png)](http://creativecommons.org/licenses/by-nc-sa/4.0/)

>这是一个收集 中国科学技术大学课程资源的（主要是计算机学院的,也有其他课程,公选课,自由选修等）的 repo, 包括课程电子版 书籍，参考书，slides(ppt), 考试试卷，学习心得，某些书的答案。


# 目录
<!-- vim-markdown-toc GFM -->

* [公告](#公告)
* [资料下载](#资料下载)
* [课程结构](#课程结构)
* [课程目录](#课程目录)
* [贡献投稿](#贡献投稿)
    * [投稿方式](#投稿方式)
        * [帮忙上传](#帮忙上传)
        * [网页操作](#网页操作)
        * [用命令行](#用命令行)
    * [投稿建议](#投稿建议)

<!-- vim-markdown-toc -->

# 公告
* 欢迎 star,fork. 欢迎反馈与建议（通过 [issue](https://github.com/mbinary/USTC-CS-Courses-Resource/issues/new),<a href="mailto:&#122;huheqin1@gmail.com?subject=%E5%8F%8D%E9%A6%88%E4%B8%8E%E5%BB%BA%E8%AE%AE">mail</a>, 或者 [qq](http://wpa.qq.com/msgrd?v=3&uin=414313516&site=qq&menu=yes))
* 可以通过在此页面搜索课程名快速定位,下面的课程目录是经过**拼音排序**过的,方便查找
* 可以添加其他计算机非课程资源, 欢迎大家的参与与贡献 (。・∀・)ノ

# 资料下载
## FTP
1. FTP/FTPS:
   - 地址：ftp.ustclug.org；
   - 路径：/ebook/USTC-CS-Courses-Resource；
   - 用户名：ftp；
   - 密码：ftp；
2. SFTP (Secure File Transfer Protocol):
   - 地址：ftp.ustclug.org；
   - 路径：/ebook/USTC-CS-Courses-Resource；
   - 用户名：ftp；
   - 密码：ftp；
3. AFP (Apple Filing Protocol)
   - 地址：afp://ftp.ustclug.org/；
   - 路径：/ebook/USTC-CS-Courses-Resource；
   - Connect As Guest

感谢 @USTC-LUG, @[volltin](https://github.com/volltin), @[zzh1996](https://github.com/zzh1996)

## HTTPS
- [github 网页](#课程目录)
- [脚本生成的网页](https://mbinary.xyz/ustc-cs/)

脚本生成的网页中直接包含了下载链接, 比 github 方便一点. 而且在移动端下载二进制文件, 在github 需要点击两次(第一次显示`This file is binary and cannot be displayed inline`,需要再点`open binary file`/`Download`才行),后者只需要一次即可下载, 对于大的二进制文件, github 移动端的不能直接下载, 需要切换成 `Desktop Version` 才有 下载按钮.

FTP 更快, 可以下载整个目录, 是最好的选择

# 课程结构
每门课程大致结构如下，有些栏目可能没有，也可以自己添加认为合理的栏目

* 教材, 答案在课程目录下
* 参考书, 参考资料在 reference 下
* 复习试卷, 习题课, 作业解答 在 review 下
* 建立文件夹 homework-teacher1, homework-teacher2 ..., lab-teacher1, 每个文件夹中如果有不同年份的, 就再建立不同年份的文件夹
* 课程主页及其他链接资源记在 README.md 中
* slides: 主要是 ppt 文件类型, **将所有 slides** 打包成 zip, 放在 课程目录下（若有多个老师，则在课程目录建立slides-teacherName1.zip, slides-teacherName2.zip...）
* students（同学们上传的自己的一些资料,作品，每个同学新建一个目录)


如 编译原理和技术 课程
```
├ lab-张昱
│   ├ c1interpreter
│   ├ c1recognizer
│   ├ Homework
│   ├ lab-1-2-answer
│   ├ lab2
│   ├ sa
│   └ teamwork
├ lab-李诚
│   ├ lab-1
│   ├ lab-2
│   ├ lab-3
│   ├ lab-4
│   ├ pre
│   ├ README.md
│   └ Server_Guide.pdf
├ lab-郑启龙
│   ├ lab1-declarationParser
│   └ lab2-pl0
├ README.md
├ reference
│   ├ 201801CompilerPractice.pdf
│   ├ Programming_Language_Pragmatics(b-ok.xyz).pdf
│   ├ The garbage collection handbook  the art of automatic memory management.PDF
│   ├ 垃圾回收的算法与实现---文字版.pdf
│   ├ 程序设计语言实践之路_d98f6.pdf
│   ├ 编译原理术语中英文对照表.pdf
│   └ 高级编译器设计与实现(虎书).pdf
├ review
│   ├ 2014期末试卷.pdf
│   ├ 2017习题课-张昱.pdf
│   ├ 2018-final-review.pdf
│   ├ 2018习题课-李诚.pdf
│   ├ 2018习题课-郑启龙.pdf
│   ├ 2018期中考试试题与参考答案.pdf
│   └ ex_on_PL0.pdf
├ slides-张昱.zip
├ slides-李诚.zip
├ slides-郑启龙.zip
├ 编译原理_第二版_(陈意云_著)_高等教育出版社_课后答案(完善版).pdf
└ 编译原理 陈意云 第3版.pdf
```

# 课程目录
**根据拼音字母排序**

{index}

# 贡献投稿
欢迎大家的参与与贡献

## 投稿方式

### 帮忙上传
可以发给我或者其他同学帮忙上传, 或者提 issue

### 网页操作
* 用网页或者[桌面版](https://desktop.github.com/)直接操作，fork and pull request, 
   操作方式可以参考 [这里](https://blog.csdn.net/qq_29277155/article/details/51048990)和[这里](https://blog.csdn.net/zhangw0_0/article/details/50667891) ,[介绍pr操作](https://blog.csdn.net/huutu/article/details/51018317)

### 用命令行
对于用命令行的同学,提醒一下这个仓库很大（2019-1-25 时已有 7G 左右）
所以如果直接 clone 很慢。
可以使用 sparse-checkout, 只下载你指定的目录

首先用网页操作，创建你想要的目录（已有的可以直接用）, 如在公选课目录下创建`人工智障`,
然后在 cli 执行
```shell
mkdir ustc-courses  #文件夹名可以自己取
cd ustc-courses
git init
git remote add -f origin  git@github.com:mbinary/USTC-CS-Courses-Resource.git
git config core.sparsecheckout true
echo "公选课/人工智障"  >> .git/info/sparse-checkout  #这里工作目录就是在那个 repo 主页下

#如果还有其他目录，都像上面一样加入即可，如 `echo  "大二上/ICS/ppt" >> .git/info/sparse-checkout`
#只需记住的是 加入的目录应该在远程仓库存在，否则报错“error: Sparse checkout leaves no entry on the working directory”

git pull origin master
git remote add upstream git@github.com:mbinary/USTC-CS-Courses-Resource.git
```
建议: 如果没有较大的改动, 或者在改动之前,可以删除掉以前 fork 的仓库 重新 fork

更新内容后
```shell
git fetch upstream/master
git merge upstream/master
```

## 投稿建议
* github 上不能直接上传大于 100mb 的文件. 对于超过 100 mb 的文件, 可以存在云盘，然后将链接写在[这里](网盘资源/README.md)
* 若是自己原创的作品，可以在文件名后加上后缀，如`-16- 计 - 王小二`, 文件里也可以写上联系方式，当然不写也行。
* 注意资源大多是二进制文件, 多次改动会使 git 重新上传, 即使 `mv`, 也会使本地仓库重新上传到远程仓库,所以在没有必要的情况下, 不要对二进制文件做任何改动.

'''
