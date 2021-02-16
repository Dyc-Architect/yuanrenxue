# coding=utf-8
# Copyright (c) 2019  - Beijing Intelligent Star, Inc.  All rights reserved
"""
文件名：第11题.py
功能：
代码历史：2021/2/7: 杜艺创
"""
# 方法一
import requests
import re
import execjs
from lxml import etree

url = 'http://www.python-spider.com/challenge/11'
headers = {
    'Cookie':'sessionid=0fzrjvda2irlj0yhg522gzkbjvt58eio;'
}
resp = requests.get(url=url,headers=headers).text
x = re.findall('x=[\"\'](.*?)[\"\']',resp)[0]
y = re.findall('y=[\"\'](.*?)[\"\'],f=function',resp)[0]
js_content = ''
with open('11.js','r') as f:
    js_content += f.read()
js_content = execjs.compile(js_content)
jsl = js_content.call('get_csl',x,y)
headers = {
    'Cookie':'sessionid=0fzrjvda2irlj0yhg522gzkbjvt58eio;' + jsl
}
resp = requests.get(url=url,headers=headers).text
data = etree.HTML(resp)
numbers = data.xpath('''//td[contains(@class,'info')]//text()''')
count = 0
for i in numbers:
    count += int(i.strip())
print(count)
# 方法二 补环境
url = 'http://www.python-spider.com/challenge/11'
headers = {
    'Cookie':'sessionid=0fzrjvda2irlj0yhg522gzkbjvt58eio;'
}
resp = requests.get(url=url,headers=headers).text
js_text = re.findall('<script>(.*)</script>',resp)[0]
js_content = '''
function cookie(js_text) {
    window = global;
    window.addEventListener = function(){}
    document = {
        addEventListener : function (a,b,c) {b()},
        attachEvent : function () {},

    }
    setTimeout  =function(){}
    location = {
        'pathname':"/challenge/12",
        'search':'',
    }
    document.createElement = function () {
        return {
            'innerHTML':'',
            'firstChild':{
                'href':'http://www.python-spider.com/'
            }
        }
    }
    eval(js_text)
    return document.cookie
}
'''
result = execjs.compile(js_content).call('cookie',js_text)
print(result)