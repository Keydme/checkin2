#!/usr/bin/env python3
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import requests,re,json,os,random

# 代理池
proxy_arr = [
    None#,'--proxy-server=http://127.0.0.1:7890'
 ]
proxy = random.choice(proxy_arr)
print(proxy)
bvid = 'BV1iC4y1g75v'
url = f'https://www.bilibili.com/video/{bvid}/'

base_info = ''
#这一部分用于转化BV号->AV号
table = 'fZodR9XQDSUm21yCkr6zBqiveYah8bt4xsWpHnJE7jL5VG3guMTKNPAwcF'
tr = {}
for i in range(58):
    tr[table[i]] = i
s = [11, 10, 3, 8, 4, 6]
xor = 177451812
add = 8728348608

def bv2av(x):
    r = 0
    for i in range(6):
        r += tr[x[s[i]]] * 58 ** i
    return (r - add) ^ xor

def get_aid(bvid):
    if 'BV' in bvid:
        return bv2av(bvid)
    else:
        return bvid

def get_base_info(aid):
    global base_info,url
    print(aid)
    base_info_url = url
    try:
        base_info = requests.get(base_info_url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}).text
    except:
        print('Error')
    return base_info

def click():
    time.sleep(3)
    driver.find_element_by_xpath('//*[@class="bpx-player-video-wrap"]').click()
    time.sleep(0.5)

def open_windows(url):
    js = 'window.open("{}")'.format(url)
    driver.execute_script(js)

chrome_options = Options()

chrome_options.add_argument('--no-sandbox') #让Chrome在root权限运行

chrome_options.add_argument('--disable-dev-shm-usage') #不打开图形界面

chrome_options.add_argument('--headless') #浏览器不提供可视化页面

chrome_options.add_argument('blink-settings=imagesEnabled=false') #不加载图片, 提升速度

chrome_options.add_argument('--disable-gpu') #谷歌文档提到需要加上这个属性来规避bug

if proxy:
    chrome_options.add_argument(proxy)

driver = webdriver.Chrome(options=chrome_options, service=Service('/opt/google/chrome/chromedriver')) #Chrome驱动的位置，此学习记录中安装到了Chrome程序根目录，该路径为绝对路径

p1 = '"bvid":"'+bvid+'".*?"stat":{(.*?)},'
print(p1,'\t',url)
## 以下全塞一起了
view = json.loads('{'+re.findall(p1,get_base_info(get_aid(bvid)),re.S)[0]+'}')['view']

for i in range(110-view+1,0,-1):
    driver.get(url)
    print(i)
    time.sleep(188)
driver.quit()


view = json.loads('{'+re.findall(p1,get_base_info(get_aid(bvid)),re.S)[0]+'}')['view']
with open('/tmp/test',mode='a') as f:
    f.write('up.py is ok\t'+str(view)+'\n')
    
print(view)
os.system("cat /tmp/test")


