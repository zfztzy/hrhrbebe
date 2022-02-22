from pyquery import PyQuery as pq


url = 'https://www.baidu.com'


a = pq(url=url, encoding='utf-8').html()
print(a)
