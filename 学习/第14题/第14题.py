# -*- coding: utf-8 -*-
# @Time: 2021/2/14 17:27
# @Author: dyc
# @File: 第14题.py
import requests


import base64
from Crypto.Cipher import AES
import time

class EncryptDate:
    def __init__(self, key):
        self.key = key  # 初始化密钥
        self.length = AES.block_size  # 初始化数据块大小
        self.aes = AES.new(self.key.encode("utf8"), AES.MODE_ECB)  # 初始化AES,ECB模式的实例
        # 截断函数，去除填充的字符
        self.unpad = lambda date: date[0:-ord(date[-1])]

    def pad(self, text):
        """
        #填充函数，使被加密数据的字节码长度是block_size的整数倍
        """
        count = len(text.encode('utf-8'))
        add = self.length - (count % self.length)
        entext = text + (chr(add) * add)
        return entext

    def encrypt(self, encrData):  # 加密函数
        res = self.aes.encrypt(self.pad(encrData).encode("utf8"))
        msg = str(base64.b64encode(res), encoding="utf8")
        return msg

    def decrypt(self, decrData):  # 解密函数
        res = base64.decodebytes(decrData.encode("utf8"))
        msg = self.aes.decrypt(res).decode("utf8")
        return self.unpad(msg)
aes = EncryptDate('wdf2ff*TG@*(F4)*YH)g430HWR(*)wse')
time_stamp = int(time.time())
url = 'http://www.python-spider.com/api/challenge14'
headers = {
    'cookie':'sessionid=5pmx4tgfkxy2vjtx2mr89x0bk5wtqoge',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.68'
}
value_list = []
for i in range(92,101):
    data = {
        'page': '{}'.format(i),
        'uc':'{}'.format(aes.encrypt('{}|{}'.format(time_stamp,i)))
    }
    resp = requests.post(url=url,data=data,headers=headers)
    try:
        for j in resp.json().get('data'):
            value = j.get('value').strip()
            value_list.append(value)
    except:
        print('page-----{} failed'.format(i))
count = 0
for i in value_list:
    count += int(i)
print(count)
# 1199720
# 1152172
# 1185596
# 1147053
# 490596