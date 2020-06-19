
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

html = etree.HTML(text)
result = etree.tostring(html)
# print("result>>>", result)
# print(result.decode('utf-8'))

print("\n华丽的分界线~~~~~~~~~~~~\n")

html = etree.parse("./test.html", etree.HTMLParser())
# result = etree.tostring(html)
# print(result.decode("utf-8"))

result = html.xpath('//*')
# print(result)


result = html.xpath('//li')
# print(result)

result = html.xpath('//li/a')
# print(result)

result = html.xpath('//a[@href="link4.html"]/../@class')
# print(result)

result = html.xpath('//a[@href="link4.html"]/parent::*/@class')
# print(result)

result = html.xpath('//li[@class="item-0"]')
# print(result)


result = html.xpath('//li[@class="item-0"]/text()')
print(result)


def featureScaling(arr):
    min_value = min(arr)
    max_value = max(arr)
    if min_value == max_value:
        return min_value

    X = None
    for item in arr:
        if item != min_value and item != max_value:
            X = item
            break
    X_new_scale = (X - min_value) / (max_value - min_value)
    return X_new_scale


# tests of your feature scaler--line below is input data
data = [115, 140, 175]
print(featureScaling(data))









