# -*- coding: utf-8 -*-
# @Time: 2021/2/15 9:27
# @Author: dyc
# @File: 第15题.py
import requests
import aiohttp
import asyncio
from concurrent.futures import ThreadPoolExecutor

headers = {
    'cookie': 'sessionid=hn8v76zp087cm6lelof535fy90s2e2nk'
}
value_list = []
for i in range(1, 101):
    url = 'http://81.70.9.39:5602/invoke?group=dyc-group&action=getdata&num={}'.format(i)
    print(url)
    resp = requests.get(url=url, headers=headers)
    print('page----------{}'.format(i), resp.json().get('data'))
    for j in resp.json().get('data'):
        value = j.get('value').strip()
        value_list.append(value)
count = 0
for i in value_list:
    count += int(i)
print(count)


def parser(url):
    headers = {
        'cookie': 'sessionid=hn8v76zp087cm6lelof535fy90s2e2nk'
    }
    print(url)
    resp = requests.get(url=url, headers=headers)
    print('page----------{}'.format(url), resp.json().get('data'))
    for j in resp.json().get('data'):
        value = j.get('value').strip()
        value_list.append(value)


def main(url):
    parser(url)
    count = 0
    for i in value_list:
        count += int(i)
    return count


if __name__ == '__main__':
    value_list = []
    thread_pool = ThreadPoolExecutor(5)
    for i in range(1, 101):
        thread_pool.submit(main, 'http://81.70.9.39:5602/invoke?group=dyc-group&action=getdata&num={}'.format(i))
    thread_pool.shutdown()
