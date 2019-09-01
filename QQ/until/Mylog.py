#!/usr/bin/python
#-*-coding:utf-8-*-
import  logging
import datetime

# 日志文件夹/目录
LOG_DIR='D:\\QQ\\log\\'
# 创建一个日志文件
a= LOG_DIR + str(datetime.datetime.now().date())+".txt"
print(a)

# logging---->python定义日志的库
# 定义日志输出的格式
#                             当前时间     当前时间 日志等级   最大四级            多少行
formatter = logging.Formatter(fmt='%(asctime)s,%(msecs)d %(levelname)-4s [%(filename)s:%(lineno)d] %(message)s',datefmt='%d-%m-%Y:%H:%M:%S')
print(formatter)
# logging的两种输出方式：
# 第一种：输出到pycharm控制台
c=logging.StreamHandler()     #将日志输出到控制台
# 添加日志样式
c.setFormatter(formatter)
# 第二种：输出到文本里
w = logging.FileHandler(a)
# 添加日志样式
w.setFormatter(formatter)
#
def get_logger(filename):
    l= logging.getLogger("filename")    #获取执行日志的脚本名字
    l.addHandler(c)                #添加输出内容到控制台
    l.addHandler(w)                #添加输出内容到文本
    l.setLevel(logging.INFO)       #定义日志的等级：INFO----->最低等级
    return l
# log = get_logger()
# log.info("qazedc")
# log.error("sdfghhhhhhjh")
