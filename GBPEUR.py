import requests
import json

url = r'https://finance.pae.baidu.com/async?srcid=50494&group=huilv_minute&tab_id=5&query=GBPEUR&code=GBPEUR&all=1&isIndex=false&isBk=false&isBlock=false&stockType=foreign&finClientType=pc'

data = requests.get(url)

data = json.loads(data.text)

cur_num = data['data'][0]['cur']['num']

print(cur_num)
### 上方代码实现从百度股市通获取英镑对欧元汇率数据，，，


### 下方实现在汇率达到1.15时发送到邮箱，提醒兑换
### 由于用GitHub托管，可能无法实现全天时时监控
### 敬请谅解
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

### 提示：所有 *****一串都代表可替代项，由自己酌情考虑替代，填入合适数据

def sed_email(a,b,c):
    my_sender='1719285729@qq.com'    # 发件人邮箱账号
    my_pass="hretcrflpupscbih"              # 发件人邮箱密码
    my_user=c      # 收件人邮箱账号，我这边发送给自己
    def mail(text,subject):
        ret=True
        try:
            msg=MIMEText(text,'plain','utf-8')
            msg['From']=formataddr(["*****",my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
            msg['To']=formataddr(["****",my_user])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
            msg['Subject']=subject                # 邮件的主题，也可以说是标题
     
            server=smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
            server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
            server.sendmail(my_sender,[my_user,],msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
            server.quit()  # 关闭连接
        except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
            ret=False
        return ret
     
    ret=mail(a,b)
    if ret:
        print("邮件发送成功")
        return True
    else:
        print("邮件发送失败")
        return False

### 上方实现有复制粘贴实现

text = f'''    根据百度股市通数据得出，英镑兑欧元汇率已达到{cur_num} ！！！


下方是指向英镑兑欧元的链接:


        https://gushitong.baidu.com/foreign/global-GBPEUR
        
'''
subject = f'英镑兑欧元:{cur_num} ！！！'


if float(cur_num) >= 1.18:
    sed_email(text,subject,'s.he18@lancaster.ac.uk')
    sed_email(text,subject,'1719285729@qq.com')
    print(1)
