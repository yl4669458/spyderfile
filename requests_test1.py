#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 21 10:06:52 2020

@author: yl
"""

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

url = 'https://movie.douban.com'

import requests

r = requests.get(url, headers = headers)

print(r.status_code == requests.codes.ok)

#print(r.raise_for_status())
print(r.cookies)
print(r.history)

r2 = requests.get('https://github.com')
print(r2.status_code)
print(r2.url)
print(r.history)

from bs4 import BeautifulSoup