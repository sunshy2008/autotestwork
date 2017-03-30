# ecoding=utf-8
__author__ = "Sven_Weng"
from appium import webdriver
import os
import time

PATH=lambda p:os.path.abspath(
os.path.join(os.path.dirname(__file__),p)
)
class AppiumTest:
    def __init__(self):
        desired_caps={}
        desired_caps['device'] = 'android'
        desired_caps['platformName']='Android'
        desired_caps['browserName']=''
        desired_caps['version']='4.4.2'
        desired_caps['deviceName']='127.0.0.1:62001'#这是测试机的型号，可以查看手机的关于本机选项获得
        #desired_caps['app'] = PATH('F:\\wanghailongworkspace\\apk_package\\app_v(20170113)_2017-01-13_yingyongbao_debug.apk')#被测试的App在电脑上的位置
        #如果知道被测试对象的apppage，appActivity可以加上下面这两个参数，如果不知道，可以注释掉，不影响用例执行
        desired_caps['appPackage']='com.join.yaxin'
        desired_caps['appActivity']='com.join.yaxin.main.activity.MainActivity'
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(30)
    def get_driver(self):
        return self.driver
