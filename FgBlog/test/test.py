import requests
import json
from pyquery import PyQuery as pq


d = pq(filename='../paragraph/htscHomeSwiper.html')
print(type(d('body').html()))
print(d('body').html())
