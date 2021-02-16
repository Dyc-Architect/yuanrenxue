# -*- coding: utf-8 -*-
# @Time: 2021/2/14 13:34
# @Author: dyc
# @File: 第13题.py
import base64
import re

from fontTools.ttLib import TTFont
import requests

url = 'http://www.python-spider.com/api/challenge13'

headers = {
    'cookie': 'sessionid=w3xa1t5k9rkaegwm53s46dache7n1zcf'
}
value_list = []
for i in range(1, 101):
    data = {
        'page': '{}'.format(i)
    }
    resp = requests.post(url=url, data=data, headers=headers).json()
    woff = resp.get('woff')
    with open('font.woff', 'wb') as f:
        f.write(base64.b64decode(woff))
    font = TTFont('font.woff')
    font.saveXML('13.xml')
    number_ = font.getTableData('post').decode()
    number_list = re.findall('uni\S*?\d+', number_)
    font_dict = {}
    for j in range(0, 10):
        if j == 9:
            font_dict[number_list[j].replace('uni', '&#x')] = 0
            continue
        font_dict[number_list[j].replace('uni', '&#x')] = j + 1
    for data in resp.get('data'):
        number_str = ''
        for m in data.get('value').strip().split(' '):
            number_str += str(font_dict.get(m))
        value_list.append(number_str)
count = 0
for i in value_list:
    count += int(i)
print(count)
