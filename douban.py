#!/usr/bin/python
# coding=utf-8

from bs4 import BeautifulSoup
import requests

url = "https://movie.douban.com/chart"  # 豆瓣电影排行榜
f = requests.get(url)
soup = BeautifulSoup(f.content, "lxml")  # type: BeautifulSoup

for k in soup.find_all('div', class_='pl2'):
    a = k.find_all('span')  # type: object
    print(a[0].string)
