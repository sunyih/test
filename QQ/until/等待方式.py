#!/usr/bin/python
#-*-coding:utf-8-*-
"""
appium 的三种等待
1、sleep---->强制等待  工作的线程会停止一段时间
2、隐性等待--->implictly_wait(time_to_wait)设置最大等待时间，
关键字参数：time_to_wait，超过最大等待时间过抛出异常
3、第三种：安卓独有---->wait_activity（）
等待某个activity出现，设置最大等待时间，超出最大等待时间，就会抛出异常
self.dr.wait_activity(activity=".activity.SplashActivity'', timeout=10)
只能用于等待activity
4、智能等待

"""
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# WebDriverWait ：等待某一个元素加载出来
# expected_conditions ：selenium的异常处理类   预期条件
# By ：指的是通过什么方式来定位  例如：By.id---->通过Id方式定位

WebDriverWait("参数一","参数二","参数三").until(EC.presence_of_all_elements_located("参数四"))

"""
参数一：我们与手机建立的会话---->dr
参数二：最大等待时间，单位：秒
参数三：刷新的页面的时间间隔，单位：秒
until(EC.presence_of_all_elements_located("参数四"))  
until：直到某个元素被找到，停止等待
参数四：一个由定位方法，和元素组成的元组,例如：(By.ID,"元素")
"""
