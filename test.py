#!/usr/bin/python
# coding=utf-8
import time

timeStamp       = time.time()
timeLocal       = time.localtime(timeStamp)
timeLocalFormat = time.strftime("%Y-%m-%d %H:%M:%S", timeLocal)
print timeStamp
print timeLocal
print timeLocalFormat
