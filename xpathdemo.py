
from lxml import etree

text = '''
<div>
<ul>
<li class="item-0"><a href="link1.html">first item</a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a>
</ul>
</div>
'''
# html = etree.HTML(text)
# result = etree.tostring(html)
# print(result.decode('utf-8'))


html = etree.parse('./test.html', etree.HTMLParser())
result = etree.tostring(html)
# print(result)
print(result.decode('utf-8'))

result = html.xpath('//li/a')
print("获取所有li节点的所有直接a子节点：", result)

result = html.xpath('//ul//a')
print("获取ul节点下的所有子孙a节点", result)

result = html.xpath('//a[@href="link4.html"]/../@class')
print("选中href属性为link4.html的a节点，然后再获取其父节点，然后再获取其class属性", result)

result = html.xpath('//a[@href="link4.html"]/parent::*/@class')
print("通过parent::来获取父节点", result)

