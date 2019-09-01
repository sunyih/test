#!/usr/bin/python
#-*-coding:utf-8-*-
# from selenium import webdriver
# from  time import sleep
# import pytest
# import yaml
# @pytest.fixture(scope="module")
# def lian():
#     dr=webdriver.Chrome()
#     dr.get("http://www.jd.com")
#     sleep(2)
#     return dr

# json是一种轻量级的数据交互格式，是javascript语言中的一种数据表现形式
# python中没有json  格式和字典一样

# import json
# a={'name':123,'age':456}
# print(a)
# # 将字典转换成json字符串
# b=json.dumps(a)
# print(type(b))
# # 将json字符串转化成字典
# c=json.loads(b)
# print(type(c))


import re
url=""
bb=requests.get(url)
# 以自借的方式接收结果   content
# 以字符串的方式接收结果   text
# 以json的方式接受结果    json
cc=bb.json    #json.loads(cc)
print(cc[""])


