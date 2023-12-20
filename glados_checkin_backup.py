#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import requests,json,os
# server酱开关，填off不开启(默认)，填on同时开启cookie失效通知和签到成功通知
sever = 'on'
# 填写server酱sckey,不开启server酱则不用填
sckey = ''
# 填入glados账号对应cookie
cookie = ''

def sed_email(a,b):
    my_sender=''    # 发件人邮箱账号
    my_pass=""              # 发件人邮箱密码
    my_user=''      # 收件人邮箱账号，我这边发送给自己
    def mail(text,subject):
        ret=True
        try:
            msg=MIMEText(text,'plain','utf-8')
            msg['From']=formataddr(["GlaDos Checkin",my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
            msg['To']=formataddr(["lll",my_user])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
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



def start(cookie):
    url= "https://glados.rocks/api/user/checkin"
    url2= "https://glados.rocks/api/user/status"
    referer = 'https://glados.rocks/console/checkin'
    #checkin = requests.post(url,headers={'cookie': cookie ,'referer': referer })
    #state =  requests.get(url2,headers={'cookie': cookie ,'referer': referer})
    origin = "https://glados.rocks"
    useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
    payload={
        'token': 'glados.network'
    }
    checkin = requests.post(url,headers={'cookie': cookie ,'referer': referer,'origin':origin,'user-agent':useragent,'content-type':'application/json;charset=UTF-8'},data=json.dumps(payload))
    state =  requests.get(url2,headers={'cookie': cookie ,'referer': referer,'origin':origin,'user-agent':useragent})
    print(state.text)
    print(checkin.text)
    data = {
        'title':'',
        'desp':'',
        'short':''
    }
    if 'message' in checkin.text:
        mess = checkin.json()['message']
        time = state.json()['data']['leftDays']
        time = time.split('.')[0]
        print(time)
        data['title'] = mess
        data['short'] = 'you have '+time+' days left!'
        data['desp'] = 'you have '+time+' days left!\n\n\n' + cookie

        if sever == 'on':
            sed_email(data['desp'],data['title'])
                # pass
                # requests.post('https://sc.ftqq.com/' + sckey + '.send',data=data)
                # requests.get('https://sc.ftqq.com/' + sckey + '.send?text='+mess+'，you have '+time+' days left

    else:
        print('ok')
        data['title'] = 'cookie过期'
        data['desp'] = cookie

        sed_email(data['desp'],data['title'])
            # requests.post('https://sc.ftqq.com/' + sckey + '.send',data=data)
            # requests.get('https://sc.ftqq.com/' + sckey + '.send?text=cookie过期'+cookie)


def main_handler(event, context):
    return start()

 
if __name__ == '__main__':
    # sed_email('hallo','test')
    #start(cookie2)
    start(cookie)
