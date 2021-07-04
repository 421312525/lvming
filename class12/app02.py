'''
@author:lvming
@time:2021/6/28
'''
'''
    appium安装部分
        2种方式：1.appium命令安装 检测appium -v
        2.appium -desktop 只要提示一路下一步
        
        adb命令：
        Adb：是安卓sdk自带的一款工具  Android debug bridge 安卓调试桥
        作用：电脑上面通过命令去操作手机
        
        准备工作：要让电脑和手机建立连接
        1.打开开发者选项（设置-点击版本号）
        2.开启usb调试
        3.建立连接 adb connect 127.0.0.1:62001
        4.检测有没有建立连接：adb devices
        
        进入手机内部 adb shell  里面命令跟linux
        退出输入exit
        安装程序：adb install 安装文件
        覆盖安装：adb install -r 安装文件
        卸载：adb uninstall 包名 com.kugou.android
        包名：开发给的
        1.aapt dump badging 安装位置
        2.adb shell中 pm list package
        3.当前应用窗口的包名：adb shell dumpsys window|findstr mCurrentFocus
        mac电脑用：adb shell dumpsys window w |grep name=
        4.日志adb logcat>d:\aa.txt   日志中搜索displayed
        日志文件：日志生成时间  adb logcat -v time  日志级别 debug info waning  标签  1443进程  日志信息
        关键字error  crash  anrin查找日志中的问题
        
        推送文件
        把电脑上的文件推送到手机上去
        Adb push 电脑存放的位置  手机位置
        adb push /Users/v_lvming/Downloads/tsss.txt /sdcard 
        
        手机的内容推送到电脑上去
        adb pull 手机路径 电脑路径  电脑的不要放在根目录c盘，d盘
        手机屏幕截图 adb shell screencap /sdcard/11.png
        Adb shell screencap 存放位置/名称
com.baidu.wenku
        monkey测试
        Monkey：猴子  瞎点，瞎测 主要是压力稳定性测试。
        有很多用户，长时间使用去使用。检测长时间运行是否有问题。模拟用户的真实的行为， 点击触摸滑动按键行为
        Monkey  什么时间会去测试？
        一般是项目稳定后 做 Monkey测试  一做就是一晚上，然后看日志文件，有没有crash anr
        
        启动monkey  adb shell monkey
        我想对于手机随机测试100次    adb shell monkey 100  公司里都是万起步
        
        次数，万起步
        自己算，比如说  1个小时  60分钟 ，1分钟，60秒            一小时3600秒
        1秒钟3个事件 1小时10800*9=97200
        
        如果想对某个程序随机点100次
        -p 包名
        adb shell monkey -p com.tal.kaoyan 10800
        模拟用户真实的行为  事件之间间隔 —throttle 时间  毫秒单位 1000ms=1s
        adb shell monkey -p com.tal.kaoyan —throttle 1000 100 d:\hh.txt
        adb shell monkey -p com.baidu.wenku --throttle 1000 -v-v-v-v 100 >/Users/v_lvming/Downloads/wenku.txt
        
        详细日志 -v-v-v 详细程度
        adb shell monkey -p com.tal.kaoyan —throttle 1000 -v-v-v 100 d:\hh.txt
        adb shell monkey -p com.tal.kaoyan -s 110 
        -s seed值 一般用于复现bug，把之前的事件再走一遍
        adb shell monkey -p com.baidu.wenku --throttle 1000 -v-v-v-v 100 -s 1625071911060 >/Users/v_lvming/Downloads/wenku1.txt
        
        ***
        adb shell monkey -p com.baidu.wenku --pct-touch 40 --pct-motion 15 --pct-rotation 10 --pct-appswitch 10 -s 1118 --throttle 1000 -v-v-v-v 100 --ignore-crashs >/Users/v_lvming/Downloads/2wenku.txt
        
        monkey命令不会自己停止，需要找到进程kill掉
        adb shell             top|grep monkey   kill进程号
        exit
        十一大事件
        —pct-touch 触摸时间 down up
        —pct-motion 手势事件 down move up
        —pct-pinchzoom 二指缩放事件
        —pct-trackball 轨迹事件
        —pct-rotation 屏幕旋转事件
        —pct-nav 基本导航事件
        —pct-majornav 主要导航事件
        —pct-syskeys 系统按键事件
        —pct-appswitch app 切换事件
        —pct-flip 键盘事件
        —pct-anyevent 其它类型事件
        
        adb shell monkey -p com.tal.kaoyan —pct-touch 100 -v-v-v 100
        adb shell monkey -p com.tal.kaoyan —pct-touch 40 —pct-motion 50 -v-v-v 100
        
        忽略崩溃
        —ignore-crashes
        超时
        —ignore-timeouts
        
        做个题目：分析
        测试考研帮，模拟用户真实的行为
        -p 指定一下包名
        模拟用户真实的行为，调整百分比
        触摸，手势
        —pct-touch 40  —pct-motion 25
        屏幕切换 —pct-rotation 10
        应用切换 —pct-appswitch 10
        -s 重现bug
        —throttle 间隔时间
        -v-v 日志
        
        200个事件 每个事件之间间隔500ms
        adb shell monkey -p com.tal.kaoyan —pct-touch 40  —pct-motion 25 —pct-rotation 10 —pct-appswitch 10 -s 1118 —throttle 500 -v-v-v 200>   
        
        命令的写法
        
        自动化脚本的写法
        针对一个功能去测试
        固定写法
        type = raw events
        count = 10 
        speed = 1.0
        start data >>
        
        设置-开发者选项-指针位置
        
        1.写脚本
        2.把脚本推送到手机中去
        adb push c:\user\xxx.txt  sdcard
        3.执行命令
        4.adb shell monkey -f /sdcard/xxx.txt -v 1
        
'''
from appium import webdriver