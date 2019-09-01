#!/usr/bin/python
#-*-coding:utf-8-*-
from appium import webdriver
# 获取手机屏幕的大小
# l=dr.get_window_size()
# # 放缩屏幕
# x1 = l["width"]*0.5
# x2 = l["width"]*0.75
# y1 = l["height"]*0.25
# y2 = l["height"]*0.5

# 左滑动
# dr.swipe(x2,y1,x1,y1,t=500)
#
# # 右滑动
def swipe_left(driver,t=500):
    l = driver.get_window_size()
    x1 = l["width"] * 0.5
    x2 = l["width"] * 0.75
    y1 = l["height"] * 0.25
    driver.swipe(x2,y1,x1,y1,duration=t)
def swipe_right(driver,t=500):
    l = driver.get_window_size()
    x1 = l["width"] * 0.5
    x2 = l["width"] * 0.75
    y1 = l["height"] * 0.25
    driver.swipe(x1, y1, x2, y1, duration=t)
def swipe_up(driver,t=500):
    l = driver.get_window_size()
    y1 = l["height"] * 0.25
    y2 = l["height"] * 0.5
    x2 = l["width"] * 0.75
    driver.swipe(x2,y2 ,x2, y1, duration=t)
def swipe_down(driver,t=500):
    l = driver.get_window_size()
    y1 = l["height"] * 0.25
    y2 = l["height"] * 0.5
    x2 = l["width"] * 0.75
    driver.swipe(x2, y1, x2, y2, duration=t)