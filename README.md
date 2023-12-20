# checkin
### 高能预警：~~已恢复为每天签到可获得免费延期!~~[已删除]
## glados-checkin
![glados-checkin](https://glados.rocks/images/logo-trans-01.png)

#### 注册地址：

1. 直接注册GLaDOS(注册地址在 https://github.com/glados-network/GLaDOS 实时更新)

成功后输入邀请码:1XTPX-OJR1T-WBAAM-TPZO2 激活,获得3天试用。

2. 通过 https://glados.space/landing/1XTPX-OJR1T-WBAAM-TPZO2 注册, 自动填写激活

3. 通过 https://1xtpx-ojr1t-wbaam-tpzo2.glados.space , 自动填写激活

4. ~~每天手动进行checkin一次，能增加一天。~~

5. 现已更新为积点兑换机制，100点可提现十日BASIC套餐，每日积点数在1~5左右主打一个血亏，但它不时会送礼品卡，大致四五个月送一次，说是upgarde our product,optimized the clash configuration files.

#### 脚本功能：

1、通过Github Action自动定时运行[main.py](https://github.com/Keydme/checkin/blob/main/glados_checkin.py)脚本。

2、通过cookies自动登录（[https://glados.rocks/console/checkin](https://glados.rocks/console/checkin))，脚本会自动进行checkin。

3、~~然后通过“Server酱”（[http://sc.ftqq.com/3.version](http://sc.ftqq.com/3.version))，自动发通知到微信上。~~

3、已修改成用企业微信的自建程序执行消息传递主程序在[checkin.py](https://github.com/Keydme/checkin/blob/main/checkin.py)脚本


#### 食用姿势：

1. 先“Fork”本仓库。（不需要修改任何文件！）

2. 注册GLaDOS，方法见上。

3. 登录GLaDOS后获取cookies。（简单获取方法：浏览器快捷键F12，打开调试窗口，点击“network”获取）

4. 在自己的仓库“Settings”里创建“Secrets”，分别是：（不开启通知，只需要创建一个COOKIE即可）

   - COOKIE（**必填**）
   - cid (可选)
   - secret（可选）
   - aid （可选）
5. 以上设置完毕后，每天零点会自动触发，并会执行自动checkin，如果开启server酱，会自动发通知到微信上。

6. **如果以上都不会的话，注册GLaDOS后，每天勤奋点记得登录后手动进行checkin即可。**

   [*<u>如果是Edu邮箱，可免费升级为360天。</u>*]


## HiFiNi - 音乐磁场

#### 简介
HiFiNi 是一个由音乐爱好者维护的分享平台, 旨在解决问题互帮互助, 如果您有需求, 请注册账号并发布信息、详细描述歌曲信息等, 我们会尽力帮您寻找

HiFiNi MUSIC BBS - HiFiNi.COM

简言之，是一个下高品质音乐的网站，签到领金币，金币换评论下载次数以及VIP，签到前10还有额外金币


#### 注册地址
https://www.hifini.com/user-login.htm

PS: 他在注册时好像锁ip还是啥来着忘了，一开始可能一直无法注册成功

#### 脚本功能
1、很简单的签到并把返回信息放在本地msg全局变量中

2、可直接通过Action一起执行，如有企业微信（且已配置好）可搭配[checkin.py](https://github.com/Keydme/checkin/blob/main/checkin.py)一起食用


## B站刷人数小工具

[up_b_watch_num.py](https://github.com/Keydme/checkin/blob/main/up_b_watch_num.py)
#### 说明
1、极度朴素的selenium进入页面并停留一段时间完成次数的增加

2、本地也行，但此脚本未添加重复执行代码（执行一次观看人数＋1），如有需要自行酌情修改

## 汇率检查
嗯，神奇的欧元与英镑汇率检测，达到预期  可发邮箱

## 企业微信机器人(虚拟)
他是直接利用cookie定时读取网页，来确定有无发送消息并予以响应。

## 发送至企业微信（Wecom__chan）

