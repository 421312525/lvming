'''
@author:lvming
@time:2021/6/21
'''
#发送邮箱 (三)

#发送附件 pytest+jenkins下载工具就行 json文件
import smtplib
#发送附件
from email.mime.multipart import MIMEMultipart
#发送正文
from email.mime.text import MIMEText
#头部
from email.header import Header

con=smtplib.SMTP_SSL('smtp.qq.com','465')
con.login('421312525@qq.com','vzvzaftwntutbgbh')
sender='421312525@qq.com'
recevier=['v_lvming@baidu.com']

#发送附件
#创建一个信封
message=MIMEMultipart()
#先找到文件
content=open('file/1.html','rb').read()
#写信
file1=MIMEText(content,'plain','utf-8')
#信封取个名字 附件名 有个html文件发送
file1['Content-Disposition']='attachment;filename="a.html"'
#把信放在信封中
message.attach(file1)


#发送人
message['Form']=Header('喔嚯<421312525@qq.com>')
#收件人
message['To']=Header('小朋友')
#标题
message['Subject']=Header('今天是个好日子')

#发送邮件
con.sendmail(sender,recevier,message.as_string())

#先压缩文件 zip包  把zip包以附件的形式发送给负责人 负责人再去下载，解压再看
# pytest allure测试报告  界面  链接,点击链接 再登录就可以看到了

