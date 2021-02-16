# -*- coding: utf-8 -*-
# @Time: 2021/2/15 15:06
# @Author: dyc
# @File: 第10题.py
import requests

session = requests.session()
session.headers = {
    'Host': 'www.python-spider.com',
    'Connection': 'keep-alive',
    'Content-Length': '6',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.68',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'http://www.python-spider.com',
    'Referer': 'http://www.python-spider.com/challenge/10',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cookie': 'sign=1613366744381~054b536e19ca3733111fa4479b438870; Hm_lvt_337e99a01a907a08d00bed4a1a52e35d=1612610580,1613195843,1613347767; sessionid=qh8e5aetxgxs3n0iapyp1acyu1974mjj; no-alert=true; Hm_lpvt_337e99a01a907a08d00bed4a1a52e35d=1613372981'
}
url = 'http://www.python-spider.com/api/challenge10'
value_list = []
for i in range(1,101):
    data = {
        'page': '{}'.format(i)
    }
    resp = session.post(url=url, data=data)
    print('page----------{}'.format(i), resp.json().get('data'))
    for j in resp.json().get('data'):
        value = j.get('value').strip()
        value_list.append(value)
count = 0
for i in value_list:
    count += int(i)
print(count)