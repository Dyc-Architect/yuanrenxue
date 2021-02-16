# -*- coding: utf-8 -*-
# @Time: 2021/2/14 18:43
# @Author: dyc
# @File: 第16题.py
import requests
import execjs
import time
url = 'http://www.python-spider.com/api/challenge16'
js_text = ''
with open('第16题.js','r') as f:
    js_text += f.read()
time_stamp = str(int(time.time()))
value_list = []
for i in range(1,101):
    token = execjs.compile(js_text).call('token',time_stamp)
    data = {
        'page': '{}'.format(i)
    }
    headers = {
        'cookie': 'sessionid=5pmx4tgfkxy2vjtx2mr89x0bk5wtqoge',
        'safe':'{}'.format(token)
    }
    resp = requests.post(url=url,headers=headers,data=data)
    print('page----------{}'.format(i),resp.json().get('data'))
    for j in resp.json().get('data'):
        value = j.get('value').strip()
        value_list.append(value)
count = 0
for i in value_list:
    count += int(i)
print(count)