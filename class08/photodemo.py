'''
@author:lvming
@time:2021/6/21
'''
#发送图片 (三)
import smtplib
#附件
from email.mime.multipart import MIMEMultipart
#图片
from email.mime.image import MIMEImage
#头部
from email.header import Header
#正文
from email.mime.text import MIMEText

con=smtplib.SMTP_SSL('smtp.qq.com','465')
con.login('421312525@qq.com','vzvzaftwntutbgbh')

sender='421312525@qq.com'
recevier=['v_lvming@baidu.com']

#创建实例
message=MIMEMultipart()

#把图片拿出 路径
image1=open('file/img.png','rb').read()
#把图片放到附件中
image_da=MIMEImage(image1)
#图片设置名字
image_da['Content-Disposition']='attachment;filename="qq.png"'
#把附件放到邮件对象中去
message.attach(image_da)

# 邮件的内容 _text文本内容 正文 _subtype 文件类型 plain 文本 txt html base64
cc=MIMEText(_text='今天是2021年6月21日,我发的图片',_subtype='plain',_charset='utf-8')
message.attach(cc)

#发送人
message['Form']=Header('喔嚯<421312525@qq.com>')
#收件人
message['To']=Header('小朋友')
#标题
message['Subject']=Header('这是我发的图片')

#发送邮件
con.sendmail(sender,recevier,message.as_string())

