#!/usr/bin/python
#-*-coding:utf-8-*-
from selenium import webdriver
from  time import sleep
import pytest
import  yaml

with open(file=r"E:\网页自动化\Element\login.yaml",mode="r",encoding="utf-8") as fb:
  e=yaml.load(fb,Loader=yaml.FullLoader)

def test_1(lian):
    lian.find_element_by_class_name(e['denglu']).click()
    sleep(2)
    lian.find_element_by_link_text(e["zhanghao"]).click()
    sleep(2)
    lian.find_element_by_class_name(e['shuru']).send_keys("15837808007")
    sleep(2)
    lian.find_element_by_id(e["mima"]).send_keys("qaz123456")
    sleep(10)
    lian.find_element_by_id(e["jinru"]).click()
    sleep(10)





