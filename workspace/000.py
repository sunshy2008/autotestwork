#!/usr/bin/python3
import time
import unittest
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from lib2to3.pgen2.driver import Driver
from lib2to3.tests.support import driver
#from autoteskwork import swipetestaction
 
PATH=lambda p:os.path.abspath(
os.path.join(os.path.dirname(__file__),p)                            
)
global driver
 
desired_caps={}
desired_caps['device'] = 'android'
desired_caps['platformName']='Android'
desired_caps['browserName']=''
desired_caps['version']='6.0.1'
desired_caps['deviceName']='HUAWEI RIO-AL00'#这是测试机的型号，可以查看手机的关于本机选项获得
desired_caps['app'] = PATH('F:\\wanghailongworkspace\\app_v(20161104)_2016-11-11.apk')#被测试的App在电脑上的位置
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True

dr=driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
time.sleep(10)
        
def hello():
    print("Hello World!")

hello()

def getSize():
    x = dr.get_window_size()['width']
    y = dr.get_window_size()['height']
    return (x, y)

def tearDown(self):
    self.driver.quit()
    time.sleep(5)
def test_login(self):
    time.sleep(2)
        
        #电话号码
self.driver.find_element_by_id('com.join.yaxin:id/userName').send_keys('18307551189')
time.sleep(2)
self.driver.find_element_by_id('com.join.yaxin:id/userPwd').send_keys('123456')
time.sleep(4)
        #登录
self.driver.find_element_by_id('com.join.yaxin:id/login_layout').click()
time.sleep(4)
l = getSize()
print(l)

x1 = int(l[0] * 0.5)  #x坐标
print(x1)

y1 = int(l[1] * 0.75)   #起始y坐标
    
y2 = int(l[1] * 0.25)   #终点y坐标

dr.swipe(x1, y1, x1, y2,1000)
time.sleep(5)

