#!/usr/bin/python
#-*-coding:utf-8-*-

"""
from appium import webdriver
from time import sleep
import yaml
import pytest
from until.ReadData import s
# from selenium.common.exceptions import NoSuchElementException
from until.Mylog import get_logger
# log=get_logger(filename="test_1.py")
# 
# 
# with open(file=r"D:\QQ\element\login.yaml",mode="r",encoding="utf-8") as fb:
#   e=yaml.load(fb,Loader=yaml.FullLoader)
# print(e)
# d={
#   "platformName": "Android",
#   "platformVersion": "5.1.1",
#   "deviceName": "emulator-5554",
#   "appPackage": "com.tencent.mobileqq",
#   "appActivity": ".activity.SplashActivity",
#   "noReset": "true"
# }
#
# # 建立连接并开启QQ程序
# dr = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=d)
# # 等待程序启动
# sleep(3)
# # 执行退出账号的操作
# dr.find_element_by_xpath(e["tou"]).click()
# sleep(1)
# dr.find_element_by_id(e["seting"]).click()
# sleep(1)
# dr.find_element_by_id(e["zhanghao"]).click()
# sleep(1)
# dr.find_element_by_id(e["tuihao"]).click()
# sleep(1)
# dr.find_element_by_id(e["tuichu"]).click()
# sleep(1)
# dr.find_element_by_id(e["tuichu"]).click()
# sleep(1)


# # text=dr.find_element_by_accessibility_id(e["tuichu"]).click()
# # print(text)
# # dr.find_element_by_accessibility_id(e["quxiao"]).click()
# # sleep(1)

#
#
# def test_1(lian):
#     lian.find_element_by_xpath(e["tou"]).click()
#     sleep(1)
#     lian.find_element_by_id(e["seting"]).click()
#     sleep(1)
#     lian.find_element_by_id(e["zhanghao"]).click()
#     sleep(1)
#     lian.find_element_by_id(e["tuihao"]).click()
#     sleep(1)
#     lian.find_element_by_id(e["tuichu"]).click()
#     sleep(1)
#     text=lian.find_element_by_accessibility_id(e["xinyonghu"]).text
#     assert text=="用户注册"
    # lian.quit()

# def test_2(lian):
#   # 先清除之前输入的数据
#   lian.find_element_by_accessibility_id(e["haoba"]).clear()
#   sleep(1)
#   # 再向输入框内数=输入账号
#   lian.find_element_by_accessibility_id(e["haoba"]).send_keys("3053742597")
#   sleep(1)
#   lian.find_element_by_id(e["password"]).clear()
#   sleep(1)
#   lian.find_element_by_id(e["password"]).send_keys("092900810sn.")
#   sleep(1)
#   lian.find_element_by_id(e["login"]).click()
#   sleep(1)



# with open(file=r"D:\QQ\data\数据.txt",mode="r",encoding="utf-8") as fb:
#     data=fb.read().split(";")
# s=[]
# for i  in  data:
#    k=i.replace("\n"," ").split(",")
#    s.append(tuple(k))
# print(s)

# @pytest.mark.parametrize("z,m",s)
# def test_3(z,m,lian):
#     lian.find_element_by_accessibility_id(e["haoba"]).clear()
#     log.info(f"账号是{z},密码是{m}")
#     lian.find_element_by_accessibility_id(e["haoba"]).send_keys(z)
#     lian.find_element_by_id(e["password"]).clear()
#     log.info(f"输入的密码是{m}")
#     lian.find_element_by_id(e["password"]).send_keys(m)
#     lian.find_element_by_id(e["login"]).click()


    # try:
    #     text = lian.find_element_by_accessibility_id(e["xinyonghu"]).text
    #     assert text=="用户注册"
    # except:
    #     text = lian.find_element_by_id(e["queding"]).text
    #     assert text == "确定"
    # else:
    #     f=lian.find_elements_by_id(e["queding"]).click()
    #     g=lian.find_elements_by_id(e["xiaoxi"]).text
    #     assert  f=="消息"
    # # except:
"""

import pytest
from time import  sleep
import yaml
with open(file=r"D:\QQ\element\shuru.yaml",mode="r",encoding="utf-8") as f:
    e=yaml.load(f,Loader=yaml.FullLoader)
def test_1(pifu):
    pifu.find_element_by_id(e["pi"]).find_element_by_class_name(e["jing"][2]).click()
    sleep(2)

