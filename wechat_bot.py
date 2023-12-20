import requests
import time
import os
import random
import re
from urllib.parse import quote
'''
url = r'https://work.weixin.qq.com/wework_admin/im/getConverse'
limit = 10
vid = 1688855133433511
appid = 5629500840598833
mark_readed = True

url = url+'?limit={}&vid={}&appid={}&mark_readed={}&random={}'.format(
    limit, vid, appid, mark_readed, random.random())

headers = {'cookie':'pgv_pvid=1603519616; pac_uid=0_b9cf0aa887124; RK=yocB6FuMex; ptcz=9bc99376d94293d16d8db0157644cc9f57133c2c78dc9723e389ba0178f66284; pgv_info=ssid=s2447047125; _qpsvr_localtk=0.5939612844575592; wwrtx.c_gdpr=0; wwrtx.ref=direct; wwrtx.refid=266115175726661; wwrtx.vst=4pm36Ek0amWli71NPDX6Tj2HQ3--noC5z0e9DTVAS2Lx_pYfAH_d9RRii2PwPpLTA6DvueyGwAYQ9x_B7VtJzF_4_zvJbLL7gzDCjyAWcCzm1faxeen4_ougo3RKuUmIeSd0E598-VrhLDtk40Bq-TAYu-zb14N2oEXvU5BHdU4DI8XFjQkb3W_m7euEJun2DNfXD5LOyST4YAgMEs8LQDOjiknjuJDCtKRHbakqX_tgGEiDzeE7d3yBkle_ly9RjRf_iXRVVDMl6W2aUKk2iQ; wwrtx.d2st=a7487373; wwrtx.sid=Cl4HLwR-_c2ysu3tNPV3EODWoVM7tO-yieUVggn_tPIrzqa_GomhYE1x96dEKhH2; wwrtx.ltype=1; wwrtx.vid=1688855133433511; wxpay.corpid=1970325141983030; wxpay.vid=1688855133433511; wwrtx.cs_ind=; wwrtx.logined=true; wwopen.open.sid=wLW5uBzyn8G02CJjB_b82H4n2uPkki9DrSVpb9Jkme5U; ptui_loginuin=2567223430; uin=o2567223430; skey=@N8BmoriQs; wwrtx.ltypes=1; wwrtx.vst2=AQAA4ngvNgJOl0I5giC1sIw4wULiRycbYtKVOLoKMiKfP8pX5MBTOCV0AuafdaYOCkVZMU4KxAvUgJRqklV5G4XmsobRPaUFAoqEEGZfn2wOl7Rcckzml85CHozAAX2frTmzgu5O3nN7KDxVG_SPD87-jFh8r8F22EPZp-ttley5rSGaEubIef7D_86Ds4z6jcTj05acX4DeV2CsU5szvInnQENSeCUjcMIoKvHHBoBfsHhRzodWwAIoFL_lLe7PJBvjVBGS7Ml_LpotjGqCoxMpLQ; wwrtx.i18n_lan=zh',
           'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',}
res = requests.get(url,headers=headers).json()['data']['item']



t = time.time()

print('ok')
'''


class WeChat():

    def __init__(self):
        self.gurl = r'https://work.weixin.qq.com/wework_admin/im/getConverse'
        self.surl = r'https://work.weixin.qq.com/wework_admin/message/sendmsg'
        self.t = time.time()
        self.gap = 60*20
        self.cookie = 'pgv_pvid=1603519616; pac_uid=0_b9cf0aa887124; RK=yocB6FuMex; ptcz=9bc99376d94293d16d8db0157644cc9f57133c2c78dc9723e389ba0178f66284; pgv_info=ssid=s2447047125; _qpsvr_localtk=0.5939612844575592; wwrtx.c_gdpr=0; wwrtx.ref=direct; wwrtx.refid=266115175726661; wwrtx.ltype=1; wwrtx.vid=1688855133433511; wxpay.corpid=1970325141983030; wxpay.vid=1688855133433511; wwrtx.cs_ind=; wwrtx.logined=true; wwopen.open.sid=wLW5uBzyn8G02CJjB_b82H4n2uPkki9DrSVpb9Jkme5U; ptui_loginuin=2567223430; uin=o2567223430; skey=@N8BmoriQs; wwrtx.ltypes=1; wwrtx.vst2=AQAA4ngvNgJOl0I5giC1sIw4wULiRycbYtKVOLoKMiKfP8pX5MBTOCV0AuafdaYOCkVZMU4KxAvUgJRqklV5G4XmsobRPaUFAoqEEGZfn2wOl7Rcckzml85CHozAAX2frTmzgu5O3nN7KDxVG_SPD87-jFh8r8F22EPZp-ttley5rSGaEubIef7D_86Ds4z6jcTj05acX4DeV2CsU5szvInnQENSeCUjcMIoKvHHBoBfsHhRzodWwAIoFL_lLe7PJBvjVBGS7Ml_LpotjGqCoxMpLQ; wwrtx.i18n_lan=zh; wwrtx.vst=46Zv7l2bCh71M3B1Lylu7W3g-sfQfHbY1MDCmtro7K_5v1sUIHjxmcDmbl-s9z7LV0s29Biw-Z2FlBbyLE1A9s52o01LUBh4HkOBSHLrFXOGxyza2sCtv3GuK8Wkl-pM2QV39OjDVq6vWD77gaUK_jXLI8AU1DulIj6gC1U_E99EMLBgqqV3cDka_RZMYasmAaCAOz6uHlXPaJWBfm6gzDpY35UOTFy8LfQj5qGRhmgLODriC3ay9P9rbd0pnZtVkpF3o0hXtJFHZSAFaFB-Lg; wwrtx.d2st=a2990322; wwrtx.sid=Cl4HLwR-_c2ysu3tNPV3EF3n9I6bxGwZVuC7kDK77tHYAVSjRLM1qA4xx90LIQGY'
        self.contents = []
        self.get_msg()
        self.command = {
            'points': self.points,
        }
        self.progress()

    def get_msg(self):
        limit = 10
        vid = 1688855133433511
        appid = 5629500840598833
        mark_readed = True
        self.gurl = self.gurl + '?limit={}&vid={}&appid={}&mark_readed={}&random={}'.format(
            limit, vid, appid, mark_readed, random.random())
        headers = {
            'cookie':
            self.cookie,
            'user-agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
        }
        res = requests.get(self.gurl, headers=headers).json()['data']['item']
        data = [i for i in res if self.t - i['send_time'] < self.gap]
        self.msgl = [i['msg']['text']['content'] for i in data]

    def send_msg(self, content):
        datt = ['zh_CN', 'json', '1', '-8', random.random()]
        self.surl = self.surl + '?lang={}&f={}&ajax={}&timeZoneInfo%5Bzone_offset%5D={}&random={}'.format(
            datt[0], datt[1], datt[2], datt[3], datt[4])
        '''            ':authority':
            'work.weixin.qq.com',
            ':method':
            'POST',
            ':path':
            '/wework_admin/message/sendmsg' +
            '?lang={}&f={}&ajax={}&timeZoneInfo%5Bzone_offset%5D={}&random={}'.
            format(datt[0], datt[1], datt[2], datt[3], datt[4]),
            ':scheme':
            'https','''
        headers = {
            'accept':
            'application/json, text/javascript, */*; q=0.01',
            'accept-encoding':
            'gzip, deflate, br',
            'accept-language':
            'zh-CN,zh;q=0.9,en;q=0.8',
            'content-length':
            '161',
            'content-type':
            'application/x-www-form-urlencoded',
            'cookie':
            self.cookie,
            'dnt':
            '1',
            'origin':
            'https://work.weixin.qq.com',
            'referer':
            'https://work.weixin.qq.com/wework_admin/frame',
            'sec-ch-ua':
            '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
            'sec-ch-ua-mobile':
            '?0',
            'sec-ch-ua-platform':
            '"Windows"',
            'sec-fetch-dest':
            'empty',
            'sec-fetch-mode':
            'cors',
            'sec-fetch-site':
            'same-origin',
            'user-agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
            'x-requested-with':
            'XMLHttpRequest',
        }
        data = {   #  按照企业微信数据抓包可知道其大致格式
            'msgTypeStr': 'text',
            'appid': '5629500840598833',
            'encrypt': '0',
            'textMsg[content]': content,
            'oper': 'Send',
            'hasNoShareGroup': 'true',
            'check_all': 'true',
            'msgtype': '1',
            '_d2st': 'a7487373',
        }
        XX = requests.post(self.surl, headers=headers, data=data)
        pass

    def progress(self):
        for i in self.msgl:
            if '/' in i:
                i = i.replace('/', '')
                command, i = i.split(' ')
                self.command[command](i)

    def points(self, s):
        url = r'https://ddnet.org/players/?json2={}'.format(quote(s))
        res = requests.get(url).json()
        formatt = '''player: {}
points: {},rank: {},total: {}
'''.format(res['player'], res['points']['points'], res['points']['rank'],
           res['points']['total'])
        for key, value in res['types'].items():
            if value['points']['rank'] != None:
                formatt += '\n' + key + ': \n' + 'points: {},rank: {},total: {}'.format(
                    value['points']['points'], value['points']['rank'],
                    value['points']['total'])

        self.contents.append(formatt)

    def send(self):
        for i in self.contents:
            self.send_msg(i)


X_23 = WeChat()
X_23.send()
###目前只有/points指令，以后会慢慢加
