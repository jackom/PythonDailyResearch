
import re

content = 'Hello 123 4567 World_This is a Regex Demo'
print(len(content))
result = re.match('^Hello\s\d{3}\s\d{4}\s\w{10}', content)
print(result.group())
print(result.span())


content = 'Hello 4567 World_This is a Regex Demo'
result = re.match('^Hello\s(\d+)\sWorld', content)
print(result)
print(result.group())
print(result.group(1))
print(result.span())


content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^He.*(\d+).*Demo$', content)
print(result)
print(result.group(1))


result = re.match('^He.*?(\d+).*Demo$', content)
print(result)
print(result.group(1))


content = '''Hello 1234567 World_This
is a Ragex Demo
'''
result = re.match("^He.*?(\d+).*?Demo$", content)
# print(result.group(1))


result = re.match("^He.*?(\d+).*?Demo$", content, re.S)
print(result.group(1))



html = '''<div id="songs-list">
h2 class="title">经典老歌</h2>
<p class="introduction">
经典老歌列表
</p>
<ul id="list" class="list-group">
<li data-view="2">一路上有你</li>
<li data-view="7">
<a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
</li>
<li data-view="4" class="active">
<a  href="/3.mp3" singer="齐秦">往事随风</a>
</li>
<li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
<li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
<li data-view="5">
<a href="/6.mp3" singer="邓丽君">但愿人长久</a>
</li>
</ul>
</div>'''


pattern = 'li.*?class="active".*?singer=(.*?)\>(.*?)</a>'
result = re.search(pattern, html, re.S)
if result:
    print(result)
    print(result.group(1))
    print(result.group(2))

print('华丽的分界符------------')


pattern = '<li.*?>\s*?(<a.*?>)?(\w+)(</a>)?\s*?</li>'
results = re.findall(pattern, html, re.S)
print(results)

for result in results:
    print(result[1])


sub_pattern = '<a.*?>|</a>'
sub_result = re.sub(sub_pattern, '', html)
print(sub_result)

pattern = '<li.*?>(.*?)</li>'
results = re.findall(pattern, sub_result, re.S)
print(results)

for result in results:
    print(result.strip())


pattern = '\w+'
results = re.match(pattern, '\n')
print(results)



