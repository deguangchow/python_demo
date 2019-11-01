#!/usr/bin/python
# coding=utf-8

import urllib

page = urllib.urlopen('http://www.meituba.com/tag/juesemeinv.html')  # 打开网页
htmlCode = page.read()  # 获取网页源码
data = htmlCode.decode('utf-8')

# 打印
# print (data)

# 写到文件
pageFile = open('pageCode.html', 'wb')  # 打开：以写的方式打开pageCode.html
pageFile.write(htmlCode)  # 写入
pageFile.close()  # 关闭
