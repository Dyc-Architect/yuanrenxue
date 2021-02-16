# -*- coding: utf-8 -*-
# @Time: 2020/10/22 20:42
# @Author: dyc
# @File: 第2题.py
import requests
import hashlib
import time
import base64

str_time = 1587102734000
md = hashlib.md5()
md.update(str(base64.b64encode(("aiding_win" + str(int(str_time/1000))).encode()), encoding='utf-8').encode())
md = md.hexdigest()
token = str(base64.b64encode(("aiding_win" + str(str_time)).encode()), encoding='utf-8')
params_1_1_1 = "sign=1587102734~" + token + "|"
sign = params_1_1_1 + md
