#!/usr/bin/python
#-*-coding:utf-8-*-
from until.ReadData import s
from until.滑屏 import swipe_left
from until.滑屏 import swipe_right
from  time import sleep

import pytest
def test_1(lian):
    swipe_left(lian)
    sleep(10)

def test_2(lian):
    swipe_right(lian)