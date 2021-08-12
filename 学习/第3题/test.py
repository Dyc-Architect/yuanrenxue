import requests
import execjs
count = 0
for i in range(1, 101):
    with open('md5.js') as r:
        js_str = r.read()
    m = execjs.compile(js_str).call('m')
    headers = {

        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://www.python-spider.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.python-spider.com/challenge/3',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'cookie': f'sessionid=13xae0y78xzm7jeiufytjvv6g7bw6qax;m={m}',
    }

    data = {
      'page': f'{i}'
    }

    response = requests.post('https://www.python-spider.com/api/challenge3', headers=headers, data=data).json()
    value_list = response.get('data')
    for value in value_list:
        count += int(value.get('value').replace(r'\r', ''))
print(count)