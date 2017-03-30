__author__ = 'Administrator'
__author__ = 'Administrator'
#-*- coding: UTF-8 -*-
import os
import time
import unittest
from appium import webdriver
from selenium.webdriver.common.keys import Keys
from lib2to3.pgen2.driver import Driver
from lib2to3.tests.support import driver
from autoteskwork import swipetestaction
from testelement import Element

PATH=lambda p:os.path.abspath(
os.path.join(os.path.dirname(__file__),p)
)

class LoginAndroidTests(unittest.TestCase):
    p = Element()

    def tearDown(self):
        self.p.driver.quit()
        time.sleep(2)
    def test_login(self):

#登录注册
        for i in range(1, 1000):
            #电话号码
            self.p.get_id('com.join.yaxin:id/userName').send_keys('18307552003')
            time.sleep(1)
            #密码
            self.p.get_id('com.join.yaxin:id/userPwd').send_keys('123456')
            time.sleep(1)
            #登录
            self.p.get_id('com.join.yaxin:id/login_layout').click()
            time.sleep(4)
            #设置
            self.p.get_name('设置').click()
            time.sleep(2)
            #退出
            self.p.get_name('退出').click()
            time.sleep(2)
            self.p.get_id('com.join.yaxin:id/quit_app_cancel').click()
            time.sleep(2)
            print("登录次数为：", i)
            time.sleep(1)
        else:
            print("出错了")

        print("共运行了1000次")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
    LoginAndroidTests


