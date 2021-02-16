# -*- coding: utf-8 -*-
# @Time: 2021/2/14 20:16
# @Author: dyc
# @File: 第7题.py
import requests
value_list = []
for i in range(1,101):
    url = 'http://www.python-spider.com/cityjson'
    headers = {
        'cookie':'sessionid=5pmx4tgfkxy2vjtx2mr89x0bk5wtqoge'
    }
    session = requests.session()
    session.post(url=url,headers=headers)
    url = 'http://www.python-spider.com/api/challenge7'
    data = {
        'page': '{}'.format(i)
    }
    resp = session.post(url=url,headers=headers,data=data)
    print('page----------{}'.format(i), resp.json().get('data'))
    for j in resp.json().get('data'):
        value = j.get('value').strip()
        value_list.append(value)
count = 0
for i in value_list:
    count += int(i)
print(count)