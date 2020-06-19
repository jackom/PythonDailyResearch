
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'

import requests
response = requests.get('https://www.baidu.com/')
print(type(response))
print(response.status_code)
print(type(response.text))
print(response.text)
print(response.cookies)

print('\n')

r = requests.get('http://httpbin.org/get')
# print(r.text)

data = {
    'name': 'jackom',
    'age': 28
}
r = requests.get('https://httpbin.org/get', params=data)
print(r.text)
print(r.json())
print(type(r.json()))


import re

headers = {
    'User-Agent': USER_AGENT
}
r = requests.get('https://www.zhihu.com/explore', headers=headers)
pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
titles = re.findall(pattern, r.text)
print(titles)

print('\n')

r = requests.get('https://github.com/favicon.ico')
# print(r.text)
# print(r.content)

with open('favicon.ico',  'wb') as f:
    f.write(r.content)


files = {
    'file': open('favicon.ico', 'rb')
}
r = requests.post('http://httpbin.org/post', files=files)
print(r.text)


str = 'a=2'
print(str.split('=', maxsplit=1))


requests.get('http://httpbin.org/cookies/set/number/123456789')
r = requests.get('http://httpbin.org/cookies')
print(r.text)


s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/123456789')
r = s.get('http://httpbin.org/cookies')
print(r.text)


r = requests.get('https://www.12306.cn', verify=True)
print(r.status_code)


from requests import Request, Session

url = 'http://httpbin.org/post'
data = {
    'name': 'jackom'
}
headers = {
    'User-Agent': USER_AGENT
}
s = requests.Session()
req = Request('POST', url, headers=headers, data=data)
prepared_request = s.prepare_request(req)
r = s.send(prepared_request)
print(r.text)




