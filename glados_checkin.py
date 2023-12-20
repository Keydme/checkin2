#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests,json,os
# server酱开关，填off不开启(默认)，填on同时开启cookie失效通知和签到成功通知
sever = 'on'
# 填写server酱sckey,不开启server酱则不用填
sckey = ''
# 填入glados账号对应cookie
cookie = ''
ok = None
def start(cookie):
    global ok;
    url= "https://glados.rocks/api/user/checkin"
    url2= "https://glados.rocks/api/user/status"
    referer = 'https://glados.rocks/console/checkin'
    #checkin = requests.post(url,headers={'cookie': cookie ,'referer': referer })
    #state =  requests.get(url2,headers={'cookie': cookie ,'referer': referer})
    origin = "https://glados.rocks"
    useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
    payload={
        'token': 'glados.one'
    }
    checkin = requests.post(url,headers={'cookie': cookie ,'referer': referer,'origin':origin,'user-agent':useragent,'content-type':'application/json;charset=UTF-8'},data=json.dumps(payload))
    state = requests.get(url2,headers={'cookie': cookie ,'referer': referer,'origin':origin,'user-agent':useragent})
    #print(state.text)
    #print(checkin.text)
    data = {
        'title':'',
        'desp':'',
        'short':''
    }
    if 'message' in checkin.text:
        mess = checkin.json()['message']
        time = state.json()['data']['leftDays']
        try: 
            had_check = str(len(checkin.json()['list']))+' day(s)'
            tot_points = checkin.json()['list'][0]['balance']
            change = checkin.json()['list'][0]['change']
            data['code'] = checkin.json()['code']
        except:
            had_check = 'No list'
        traffic = state.json()['data']['traffic']/1024/1024/1024
        time = time.split('.')[0]
        print(time)
        data['title'] = mess
        data['short'] = 'you have '+time+' days left!'
        data['desp'] = 'you have '+time+' days left!\n' + had_check + '\nYou have used '+str(traffic)[:5]+'/200GB\n'+tot_points[:tot_points.index('.')]+'.0 cumulatived!\n'+change[:change.index('.')]+'.0 points today gets.'
        print(data['desp'])
        ok = 1
        
                # pass
                # requests.post('https://sc.ftqq.com/' + sckey + '.send',data=data)
                # requests.get('https://sc.ftqq.com/' + sckey + '.send?text='+mess+'，you have '+time+' days left

    else:
        print('ok')
        ok = 0
        data['code'] = -1
        data['title'] = 'cookie过期'
        data['desp'] = cookie

    return data
            # requests.post('https://sc.ftqq.com/' + sckey + '.send',data=data)
            # requests.get('https://sc.ftqq.com/' + sckey + '.send?text=cookie过期'+cookie)


def main_handler(event, context):
    return start()

 
msg = start(cookie)
