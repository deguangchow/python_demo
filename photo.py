#!/usr/bin/python
# coding=utf-8
import urllib
import re

page = urllib.urlopen('http://www.jshtgz.com.cn/')  # 打开网页
htmlCode = page.read()  # 获取源码
data = htmlCode.decode('utf-8')
# data = htmlCode.decode('gb2312')

reg = r'src="(.+?\.jpg)"'  # 正则表达式
reg_img = re.compile(reg)  # 编译一下，运行更快
imglist = reg_img.findall(data)  # 进行匹配

x = 0
for img in imglist:
    print(img)
    urllib.urlretrieve(img, '%s.jpg' % x)
    x += 1
