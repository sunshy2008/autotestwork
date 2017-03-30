#! /usr/bin/env python
#coding=utf-8
import os
import time
import unittest
from selenium import webdriver
from lib2to3.pgen2.driver import Driver
from lib2to3.tests.support import driver
PATH=lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.4'
desired_caps['deviceName'] = 'hongmiwang'

desired_caps['app'] = PATH('F:\\wanghailongworkspace\\ContactManager2.5.321.apk')
#desired_caps['appPackage'] = 'com.xiangchao.starspace'　　
#desired_caps['appActivity'] = 'com.xiangchao.starspace.activity.SplashActivity'

#如果设置的是app在电脑上的路径，则不需要配appPackage和appActivity，同理反之

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps) #启动app

time.sleep(5)#启动app时，需要一定时间进入引导页，所以必须设置等待时间，不然下面会一直报错定位不到元素

driver.find_element_by_id('com.xiangchao.starspace:id/skip').click()

driver.quit()
