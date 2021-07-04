'''
@author:lvming
@time:2021/6/21
'''
#发送html文件  （二）
import smtplib

from email.mime.text import MIMEText
from email.header import Header
con=smtplib.SMTP_SSL('smtp.qq.com','465')

con.login('421312525@qq.com','vzvzaftwntutbgbh')
sender='421312525@qq.com'
recevier=['v_lvming@baidu.com']

#html的文件内容
htmlconnext='''
<!DOCTYPE html>
<html >
<body>
	<a href=‘http://www.baidu.com’>我是百度点我点我</a>
</body>
</html>
'''
# message=MIMEText(_text='htmlconnext',_subtype='plain',_charset='utf-8')

#html会写内容出来 css会把内容摆放整齐  s动态的效果 前端课程  写出一个简单html的页面
#了解页面层级 css js 加样式  css表达式 元素定位

#邮箱正文
message=MIMEText(_text=htmlconnext,_subtype='html',_charset='utf-8')
#邮箱头部
# 设置头部 设置标题
message['Subject']=Header('这是我的邮件头~')
# 发件人
message['From']=Header('夜幕降临℃<lvming_421312525@qq.com>')
# 接收人
message['To']=Header('ming<v_lvming@baidu.com>')

#发送邮件
con.sendmail(sender,recevier,message.as_string())

#测试报告 unittest生成测试报告html形式 邮件不支持js