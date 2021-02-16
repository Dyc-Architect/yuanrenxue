# -*- coding: utf-8 -*-
# @Time: 2020/10/25 12:10
# @Author: dyc
# @File: 第6题.py
import requests


def get_resp():
    global count
    url = 'http://www.python-spider.com/api/challenge6'
    for i in range(1, 101):
        data = {
            'page': str(i),
        }
        headers = {
            'cookie': 'sessionid=6yvi51nde7opij0hkz3x6emvcb6ld7iw; sign=1603587605603~f89f6414e6f615617706decd497*'
        }

        resp = requests.post(url=url, data=data, headers=headers).json().get('data')
        for i in resp:
            count += int(i.get('value'))
        print(count)
    return count


if __name__ == '__main__':
    count = 0
    get_resp()
