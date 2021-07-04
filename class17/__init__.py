'''
@author:lvming
@time:2021/7/4
'''
'''
GIT的介绍与安装：
   目前在企业中对于项目管理应用最为广泛的是SVN和GIT，我们的所有项目在实际生成过程中是会有非常多的产出物
   配置管理是整个项目管理过程中非常关键的一个环节，将整个项目中的产出物进行对应的配置，在过程中还会建立有一个基线库。
   需要有一个独立的空间，用于存放所有的产出物，并进行配置管理。
   git环境搭建：
	1.下载git安装包，win.exe的文件，建议在下载的时候启动梯子
	2.直接双击安装，在安装页面下第一页会有git的安装路径选择，依照你的需要进行设置即可。剩余的内容全部直接点击next即可。
	3.安装完成以后，点击鼠标邮件看到有git相关的功能，表示安装成功
更新git到最新版本：git update-git-for-windows
或者brew upgrade git
git config --list查看git的配置内容
git config —global user.name 修改个人信息，包括name和email即可
git init 创建本地仓库
Git相关指令详解：
   git管理所有的内容都是基于分支来进行管理的，一个仓库下可以有多个分支，分别进行管理
   git add 文件名称,后缀名 添加文件到暂存区
   git commit -m “这是第一次提交”
   git status 检查暂存区是否存有内容待操作
   git restore —staged file.txt 从缓存区撤回
    git restore -- 文件名称.后缀名 撤销本次的修改行为
   git log 可以用于查看历史提交记录，所有的备注信息也会显示在记录之中，可以添加参数：git log --pretty=oneline 只显示一行信息
   git reset --hard HEAD^ 将当前内容回退到上一个版本，也可以不输入HEAD^，直接输入版本号选择指定的版本回退
  git reset --hard HEAD~100 回退到100个版本
  git reflog   获取每一个版本号信息的相关日志
  git reset --hard b87e17d 回归到指定版本
git remote add origin https://github.com/421312525/lvming.git 连接到指定的远程仓库，远程仓库基于url来进行定位，基于ssh进行链接
git push -u origin master 将本地仓库内容直接提交至远程仓库
git push origin master 将本地仓库新增的内容提交至远程仓库
git clone https://github.com/421312525/lvming01 从指定远程仓库下载内容到本地仓库
git checkout -b 分支名  创建并切换至新的分支
git branch 查看所有分支，并以*显示当前使用的分支
git checkout 分支名 切换至指定的分支
git merge temp01 合并指定的分支
git branch -d temp01 删除指定的分支
'''