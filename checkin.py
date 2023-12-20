import hifini_sign as hif
import datetime
from wecom_chan import *
import glados_checkin as gla


check_lis = [2,1]
cid = ''#同下
aid = ''#同下
secret = ''#填入你自己的

def check(check_lis):
    global msg
    for i in check_lis:
        if i == 1:
            try:
                msg['short'] += str(gla.ok)+','
                msg['desp'] += gla.msg['desp']
            except Exception as e:
                print('error:',e)
        elif i == 2:
            try:
                msg['desp'] += trans_json_to_line(hif.msg)
                msg['short'] += str(hif.ok)+','
            except Exception as e:
                print('error:',e)
    msg['short'] = msg['short'][:-1]
    return msg['short']
def trans_json_to_line(dic):
    temp = ''
    for key, value in dic.items(): 
        temp += "\n\"%s\":\"%s\""%(key, value)
    return temp+'\n-----------------------------------------------\n'

msg = {
    'title':'',
    'desp':'',
    'short':''
}
check(check_lis)

if not(gla.msg['code']==1 and hif.msg['code']=='-1'):
    # print(not(gla.msg['code']==1 and hif.msg['code']==-1))
    send_to_wecom(msg['short']+'\n  '+msg['desp'],cid,aid,secret)

with open('/tmp/test','a') as f:
    f.write(str(datetime.datetime.now())+'\t'+'checkin.py is ok\n')

