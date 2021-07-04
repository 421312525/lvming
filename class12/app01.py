'''
@author:lvming
@time:2021/6/28
'''
'''
    移动端基础内容

    app分类
    原生应用：官方语言
    手机上面’设置’
    可以访问手机所有功能，
    运行速度快
    怎么看混合和原生应用：设置-开发者选项。。。边界
    
    混合应用：
    原生+h5
    开发周期短
    功能发布比较快
    
    Web版app：
    在浏览器上运行的
    
    APP自动化流程
    1.JDK ：安卓开发语言是java,java的核心是jdk
    2.SDK：开发人员工具库，测试adb命令包名，元素定位
    3.模拟器：夜神模拟器62001雷电模拟器，逍遥模拟器
    4.Appium自动化工具：robotium,macaca
    支持语言：java,python语言，php
    跨平台：安卓，ios测试
    跨应用
    
    1.jdk安装
    检测：java -version
    
    2.sdk
    Adb version
    
    3.模拟器会和sdk的版本产生冲突：
    sdk中的adb取出来
    
    4.appium自动化工具：
    1.命令行安装2015就没有更新了
    第一步：要装nodejs
    第二步：设置镜像npm config set registry http://registry.npm.taobao.org/
    第三步：安装最新包，npm install appium -g
    
    报错：不要指定版本
    最简单粗暴  就是卸载nodejs然后重新安装
    
    2，appium-desktop工具
    两者方式任取一种，两种都可安装
    
    5..python库，在cmd中输入
    pip.ext install Appium-Python-Client
'''