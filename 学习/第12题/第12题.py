# -*- coding: utf-8 -*-
# @Time: 2021/2/13 14:37
# @Author: dyc
# @File: 第12题.py
import requests
from fontTools.ttLib import TTFont

font = requests.get('http://www.python-spider.com/static/font/challenge12/aiding.woff').content
with open('font.woff', 'wb') as f:
    f.write(font)
font = TTFont('font.woff')
number_list = font['cmap'].tables[0].ttFont.getGlyphOrder()
font_dict = {}
for i in range(1,11):
    if i == 10:
        font_dict[number_list[i].replace('uni','&#x')] = 0
        continue
    font_dict[number_list[i].replace('uni','&#x')] = i
print(font_dict)
url = 'http://www.python-spider.com/api/challenge12'

headers = {
    'cookie':'sessionid=w3xa1t5k9rkaegwm53s46dache7n1zcf'
}
value_list = []
for i in range(1,101):
    data = {
        'page': '{}'.format(i)
    }
    resp = requests.post(url=url, data=data, headers=headers).json().get('data')
    for data in resp:
        number_str = ''
        for i in data.get('value').strip().split(' '):
            number_str += str(font_dict.get(i))
        value_list.append(number_str)
count = 0
for i in value_list:
    count += int(i)
print(count)