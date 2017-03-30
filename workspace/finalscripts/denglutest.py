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
from testdriver import AppiumTest
from testelement import Element

PATH=lambda p:os.path.abspath(
os.path.join(os.path.dirname(__file__),p)
)

class LoginAndroidTests(unittest.TestCase):
    p = AppiumTest()
    TestDrive = p.get_driver()

    def tearDown(self):
        self.TestDrive.quit()
        time.sleep(2)

    def test_login(self):

#登录注册
        for i in range(1, 1000):
            #电话号码
            self.TestDrive.find_element_by_id('com.join.yaxin:id/userName').send_keys('18307552003')
            time.sleep(1)
            #密码
            self.TestDrive.find_element_by_id('com.join.yaxin:id/userPwd').send_keys('123456')
            time.sleep(1)
            #登录
            self.TestDrive.find_element_by_id('com.join.yaxin:id/btn_login').click()
            time.sleep(6)
            #进入抽奖页面
            #self.TestDrive.find_element_by_class_name('android.widget.RelativeLayout').click()
            #def getSize(self):
            xx = self.TestDrive.get_window_size()['width']
            yy = self.TestDrive.get_window_size()['height']
            #ll = self.TestDrive.swipetestaction.getSize(self)
            print(xx)
            print(yy)
            #self.TestDrive.isDisplay()
            self.TestDrive.tap([(100, 200), (100, 300), (100, 100)], 500)
            print(xx)
            print(yy)
            #self.TestDrive.tap([(a*X, b*Y)],)
            time.sleep(40)
            for i in range(1,4):
                self.TestDrive.tap([(100, 680), (100, 700), (100, 100)], 500)
                #self.TestDrive.get_name('开始抽奖').click()
                time.sleep(6)
                self.TestDrive.get_name('确定').click()
                time.sleep(2)

            #设置
            self.TestDrive.find_element_by_name('设置').click()
            time.sleep(2)
            #退出
            self.TestDrive.find_element_by_name('退出').click()
            time.sleep(2)
            self.TestDrive.find_element_by_id('com.join.yaxin:id/quit_app_cancel').click()
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


