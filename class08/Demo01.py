'''
@author:lvming
@time:2021/6/21
'''
#邮件
#1.用python代码发送邮件 文本邮件
#2.发送html邮件
#3.发送附件和图片
# （一）
#smtplib smtp进行封装
import smtplib
#发送邮件正文
from email.mime.text import MIMEText
#发送头部
from email.header import Header

#创建邮箱服务器  SMTP_SSL(邮箱链接地址，端口)
#163邮箱  网易邮箱  qq邮箱SMTP的端口号是465或587
con=smtplib.SMTP_SSL('smtp.qq.com','465')
#登录邮箱 用户名和密码
#QQ邮箱-设置-账户-POP3/SMTP服务开启
#163邮箱 qq邮箱 设置一下 用户名是邮箱名 密码：授权密码 vzvzaftwntutbgbh
con.login('421312525@qq.com','vzvzaftwntutbgbh')
# print(con)

# 发送者账号
sender='421312525@qq.com'
# 接受者账号
recevier=['v_lvming@baidu.com']

# 邮件的内容 _text文本内容 正文 _subtype 文件类型 plain 文本 txt html base64
message=MIMEText(_text='今天是2021年6月21日',_subtype='plain',_charset='utf-8')

# 设置头部
message['Subject']=Header('这是我的邮件头~')
# 发件人
message['From']=Header('夜幕降临℃<lvming_421312525@qq.com>')
# 接收人
message['To']=Header('ming<v_lvming@baidu.com>')

try:
    #发送邮件 由谁发送 邮局发送 con 发送邮件失败捕获
    con.sendmail(sender,recevier,message.as_string())
    print('邮件发送成功')
except Exception as e:
    print('无法发送邮件')

# 文本邮件  封装邮件 服务器链接 init方法

#发送html文件
