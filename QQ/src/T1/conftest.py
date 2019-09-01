#!/usr/bin/python
#-*-coding:utf-8-*-
import pytest
from appium import webdriver
from time import sleep
import  yaml
"""
# @pytest.fixture(scope="module")
# def lian():
#     d={
#       "platformName": "Android",
#      "platformVersion": "5.1.1",
#     "deviceName": "emulator-5554",
#     "appPackage": "com.tencent.mobileqq",
#     "appActivity": ".activity.SplashActivity",
#     "noReset": "true",
#     "unicodeKeyboard":"true"
# }
#     dr = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=d)
#     sleep(10)
#     return dr
"""

@pytest.fixture(scope="module")
def pifu():
    d={
      "platformName": "Android",
      "platformVersion": "5.1.1",
      "deviceName": "emulator-5554",
      "appPackage": "com.baidu.input",
      "appActivity": ".ImeAppMainActivity",
      "noReset": "true"
    }
    dr = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_capabilities=d)
    sleep(10)
    return dr

