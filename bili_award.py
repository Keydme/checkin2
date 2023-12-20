from requests import post
import time

headers = {
    'Accept':'application/json, text/plain, */*',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control':'no-cache',
    'Content-Length':'315',
    'Content-Type':'application/x-www-form-urlencoded',
    'Cookie':'buvid3=3712717B-FB68-BA63-F1DA-DA13AAB1CB9501098infoc; b_nut=1697298901; _uuid=DDE432D9-BB910-F1EE-64B10-B3A62A7F917D02097infoc; buvid4=DA1EE91E-7A09-287F-E559-88C6AA3A2D8802064-023101423-SaYJELBQG7PYHaRrTmH3YvCWdaWrjd%2F%2FSCB2JxBzZeKuhVpky%2FpcJg%3D%3D; buvid_fp=1579ce54014b8f6eab445d3440861de3; SESSDATA=e3bd6c8c%2C1712850969%2Cea462%2Aa2CjBKCpdbvtitfy6oGuxXrA9Z9mSny172HvGSGLZEwUFoNF_0slGJJs84A3ArZ7-dHlQSVlhDNXVhUmpDQUtfSlUzdUlISGxEMUo5YUMzUXZHenJpMHhqbnU2Nk1DX0VUZ040UElFZ25uWUFQc0NJeExuaXZTUWEtT0J2Q3l5YUQ1ZVhHN055QmlRIIEC; bili_jct=e23eed5e9e1ec3b803fb3c226170b797; DedeUserID=3546557704046966; DedeUserID__ckMd5=82008402ce30656a; enable_web_push=DISABLE; header_theme_version=CLOSE; home_feed_column=4; browser_resolution=1358-620; CURRENT_FNVAL=4048; rpdid=0zbfAGL40E|j6UMb1H2|3et|3w1QSjMO; innersign=0; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTc3MDcyODUsImlhdCI6MTY5NzQ0ODAyNSwicGx0IjotMX0.wawNt09xrHS2Lj35BezGilfKY9hJct-UzuaispDG_Ac; bili_ticket_expires=1697707225; bp_video_offset_3546557704046966=852995649044480025; sid=nvfcgyae; b_lsid=10C2B71019_18B3937362E',
    'Dnt':'1',
    'Origin':'https://www.bilibili.com',
    'Pragma':'no-cache',
    'Referer':'https://www.bilibili.com/blackboard/activity-award-exchange.html?task_id=48e196fb&spm_id_from=333.967.b_4d7a357430327068504c43.1',
    'Sec-Ch-Ua':'"Chromium";v="118", "Microsoft Edge";v="118", "Not=A?Brand";v="99"',
    'Sec-Ch-Ua-Mobile':'?0',
    'Sec-Ch-Ua-Platform':'"Windows"',
    'Sec-Fetch-Dest':'empty',
    'Sec-Fetch-Mode':'cors',
    'Sec-Fetch-Site':'same-site',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.46'
    }
data = {
    'csrf': 'e23eed5e9e1ec3b803fb3c226170b797',
    'act_id': '840',
    'task_id': '3514',
    'group_id': '0',
    'receive_id': '2082338',
    'receive_from': 'missionPage',
    'act_name': '崩坏星穹铁道1.4视频侧',
    'task_name': '累计投稿3天',
    'reward_name': '星琼*100',
    'gaia_vtoken': ''
    }

url = 'https://api.bilibili.com/x/activity/mission/task/reward/receive'
for i in range(100):
    response = post(url=url, data=data, headers=headers)
    time.sleep(0.1)

import datetime

with open('/tmp/test','a') as f:
    f.write(str(datetime.datetime.now())+'\t'+'bili finished\n')
