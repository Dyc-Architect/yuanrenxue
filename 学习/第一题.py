# -*- coding: utf-8 -*-
# @Time: 2020/10/20 21:38
# @Author: dyc
# @File: 第一题.py
import json

import requests
import time
import base64
from hashlib import sha1,md5
import hmac



# def get_token(time_stamp):
#     sign = '9622'
#     time_stamp = str(time_stamp)
#     token = str(base64.b64encode((sign + time_stamp).encode()), encoding='utf-8')
#     md5 = hashlib.md5()
#     md5.update(token.encode('utf-8'))
#     tokens = md5.hexdigest()
#     return tokens


# def main():
#     global count
#     for i in range(1, 86):
#         time_stamp = int(time.time())
#         url = 'http://www.python-spider.com/challenge/api/json'
#         headers = {
#             'safe': get_token(time_stamp),
#             'timestamp': str(time_stamp),
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
#             'Referer': 'http://www.python-spider.com/challenge/1',
#             'Host': 'www.python-spider.com'
#         }
#         params = {
#             'page': str(i),
#             'count': '14'
#         }
#         resp = requests.get(url=url, headers=headers, params=params).text
#         parser(resp)
#     return count


def parser(data):
    global count
    data = json.loads(data)
    infos = data.get('infos')
    for i in infos:
        title = i.get('message')
        if '招' in title:
            count += 1


if __name__ == '__main__':
    count = 0
    # print(main())
    # str1 = 'GET&%2Fapi%2Fv2%2Fgroup%2Frec_groups_by_tag&1603517969'
    # str2 = 'bf7dddc7c9cfe6f7'
    str1 = bytearray('GET&%2Fapi%2Fv2%2Fgroup%2Frec_groups_by_tag&1603547880', encoding='utf-8')
    str2 = bytearray('bf7dddc7c9cfe6f7', encoding='utf-8')
    hmac_code = hmac.new(str2, str1, sha1)
    code = hmac_code.digest()
    print(base64.encodestring(code).decode('utf-8'))
    # code = hmac_code.digest().0pe2encode('base64')[:-1]
    # print(base64.encodestring(code))
    # print([i for i in bytearray(code,encoding='utf-8')])
