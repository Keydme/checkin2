import requests

def hifini_check():
    
    headers = {
    'Accept':'text/plain, */*; q=0.01',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control':'no-cache',
    'Connection':'keep-alive',
    'Content-Length':'0',
    'Cookie':'',#填入自己的cookie~
    'DNT':'1',
    'Host':'www.hifini.com',
    'Origin':'https://www.hifini.com',
    'Pragma':'no-cache',
    'Referer':'https://www.hifini.com/',
    'Sec-Fetch-Dest':'empty',
    'Sec-Fetch-Mode':'cors',
    'Sec-Fetch-Site':'same-origin',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'X-Requested-With':'XMLHttpRequest',
    'sec-ch-ua':'"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile':'?0',
    'sec-ch-ua-platform':'"Windows"'
        }
    
    url ='https://www.hifini.com/sg_sign.htm'
    
    
    response = requests.post(url=url, data={}, headers=headers)
    return response.json()
try:
    msg = hifini_check()
except:
    msg = {'msg':'error','code':'-'}

if msg['code'] == '-1' or msg['code'] == '0':
    ok = 1
else:
    ok = 0
