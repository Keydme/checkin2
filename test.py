from wecom_chan import *
import base64
cid = ''#同下
aid = ''#同下
secret = ''#填入自己的
ret = send_to_wecom("推送测试\r\n测试换行", cid, aid, secret);
print( ret );
ret = send_to_wecom_card("111","测试1<hr><br>no!!!",cid, aid, secret);
print( ret );
'''
ret = send_to_wecom('<a href="https://www.github.com/">文本中支持超链接</a>', cid, aid, secret);
print( ret );
ret = send_to_wecom_image(base64.b64encode(open('./1.png','rb').read()), cid, aid, secret);
print( ret );
ret = send_to_wecom_markdown("**Markdown 内容**", cid, aid, secret);
print( ret );
'''
