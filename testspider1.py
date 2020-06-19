

# from selenium import webdriver
# browser = webdriver.Chrome()
import socket
/*import urllib.request*/

response = urllib.request.urlopen("https://www.python.org")
# response = urllib.request.urlopen("http://localhost:5000/")
# print(response.read().decode('utf-8'))

import urllib.parse

data = bytes(urllib.parse.urlencode({"word": "hello"}), encoding='utf8')
response = urllib.request.urlopen('http://httpbin.org/post', data=data)
# print(response.read())


import urllib.error

try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
except urllib.error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')
except urllib.error.URLError as e:
    print(e.reason)
    if isinstance(e.reason, socket.timeout):
        print('TIME_OUT')
else:
    print('Request Successfully!')


url = 'http://httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Host': 'httpbin.org'
}
dict = {
    'name': 'jackom'
}
data = bytes(urllib.parse.urlencode(dict), encoding='utf8')
req = urllib.request.Request(url, data=data, headers=headers, method='POST')
response = urllib.request.urlopen(req)
# print(response.read().decode('utf-8'))



from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
from urllib.error import URLError

username = 'username'
password = 'password'
url = 'http://localhost:5000/'

p = HTTPPasswordMgrWithDefaultRealm()
p.add_password(None, url, username, password)
auth_handler = HTTPBasicAuthHandler(p)
opener = build_opener(auth_handler)

try:
    result = opener.open(url)
    html = result.read().decode('utf-8')
    print(html)
except URLError as e:
    print(e.reason)


import http.cookiejar, urllib.request

cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open("http://www.baidu.com")
# for item in cookie:
#     print(item.name + "=" + item.value)


filename = 'cookies.txt'
cookie = http.cookiejar.MozillaCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)


lwp_filename = 'lwpcookies.txt'
cookie = http.cookiejar.LWPCookieJar(lwp_filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)


cookie = http.cookiejar.LWPCookieJar()
cookie.load(lwp_filename, ignore_discard=True, ignore_expires=True)
handler = urllib.request.HTTPCookieProcessor()
opener = urllib.request.build_opener(handler)
response = opener.open('http://baidu.com')
# print(response.read().decode('UTF-8'))


from urllib import request, error

try:
    response = request.urlopen('https://cuiqingcai.com/index.htm')
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')


from urllib.parse import urlparse
result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
# print(type(result), result, sep='\n')

result = urlparse('www.baidu.com/index.html;user?id=5#comment', scheme='https')
# print(type(result), result, sep='\n')


from urllib.parse import urlencode

base_url = 'http://www.baidu.com?'
params = {
    'name': 'jackom',
    'age': 28
}
url = base_url + urlencode(params)
print(url)

from urllib.parse import quote
keyword = '壁纸'
url = 'https://www.baidu.com/s?wd=' + quote(keyword)
print(url)

from urllib.parse import unquote
print(unquote(url))

from urllib.parse import urljoin

from urllib.robotparser import RobotFileParser

rp = RobotFileParser()
base_url = 'http://www.jianshu.com/'
params = {
    'q': 'python',
    'page': 1,
    'type': 'collections'
}
rp.set_url(urljoin(base_url, 'robots.txt'))
rp.read()
print(rp.mtime())
print(rp.modified())
print(rp.can_fetch('*', urljoin(base_url, 'p/b67554025d7d')))
print(rp.can_fetch('*', urljoin(base_url, 'search?' + urlencode(params))))





