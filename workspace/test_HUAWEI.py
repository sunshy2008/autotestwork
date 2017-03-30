#-*- coding: UTF-8 -*-
import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from lib2to3.pgen2.driver import Driver
from lib2to3.tests.support import driver
#from autoteskwork import swipetestaction

 
PATH=lambda p:os.path.abspath(
os.path.join(os.path.dirname(__file__),p)                            
)
global driver
 
class LoginAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps={}
        desired_caps['device'] = 'android'
        desired_caps['platformName']='Android'
        desired_caps['browserName']=''
        desired_caps['version']='6.0.1'
        desired_caps['deviceName']='HUAWEI RIO-AL00'#这是测试机的型号，可以查看手机的关于本机选项获得
        desired_caps['app'] = PATH('F:\\wanghailongworkspace\\app_v(20161104)_2016-11-11.apk')#被测试的App在电脑上的位置
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
 
#如果知道被测试对象的apppage，appActivity可以加上下面这两个参数，如果不知道，可以注释掉，不影响用例执行
   #      desired_caps['appPackage']='com.join.yaxin'
  #      desired_caps['appActivity']='.MainActivity'

        self.driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
        time.sleep(10)
       
    def tearDown(self):
        self.driver.quit()
        time.sleep(5)

    #获得机器屏幕大小x,y

    def getSize():
        x = dr.get_window_size()['width']
        y = dr.get_window_size()['height']
        return (x, y)

    #屏幕向上滑动

    def swipeUp(t):

        l = getSize()

        x1 = int(l[0] * 0.5)  #x坐标

        y1 = int(l[1] * 0.75)   #起始y坐标

        y2 = int(l[1] * 0.25)   #终点y坐标

        dr.swipe(x1, y1, x1, y2,t)

    #屏幕向下滑动

    def swipeDown(t):

        l = getSize()

        x1 = int(l[0] * 0.5)  #x坐标

        y1 = int(l[1] * 0.25)   #起始y坐标
    
        y2 = int(l[1] * 0.75)   #终点y坐标

        dr.swipe(x1, y1, x1, y2,t)

    #屏幕向左滑动

    def swipLeft(t):

        l=getSize()

        x1=int(l[0]*0.75)

        y1=int(l[1]*0.5)

        x2=int(l[0]*0.05)

        dr.swipe(x1,y1,x2,y1,t)

    #屏幕向右滑动

    def swipRight(t):

        l=getSize()

        x1=int(l[0]*0.05)

        y1=int(l[1]*0.5)

        x2=int(l[0]*0.75)

        dr.swipe(x1,y1,x2,y1,t)
   
    def test_login(self):
        time.sleep(2)
        
        #电话号码
        self.driver.find_element_by_id('com.join.yaxin:id/userName').send_keys('18307551189')
       
        self.driver.find_element_by_id('com.join.yaxin:id/userPwd').send_keys('123456')
        time.sleep(5)
        #登录
        self.driver.find_element_by_id('com.join.yaxin:id/login_layout').click()
        time.sleep(4)

        #调用向上滑动

        swipeUp(1000)
        time.sleep(2)

        #调用向下滑动

        swipeDown(1000)
        time.sleep(2)

        #调用向左滑动

        swipLeft(1000)

        time.sleep(2)

        #调用向右滑动

        swipRight(1000)
        time.sleep(2)
        
        self.driver.find_element_by_class_name('android.widget.ImageView').click()
        time.sleep(4)
        
        self.driver.find_element_by_name('呼叫中心')
        time.sleep(2)
        
        self.driver.find_element_by_class_name('android.widget.ImageView').click()
        time.sleep(2)

        self.driver.find_element_by_class_name('android.widget.Button').click()
        time.sleep(2)
        
        self.driver.find_element_by_name('待审核').click()
        time.sleep(2)
        
        self.driver.find_element_by_name('审核未通过').click()
        time.sleep(2)
        
        self.driver.find_element_by_name('审核过').click()
        time.sleep(2)

        self.driver.find_element_by_name('家属管理').click()
        time.sleep(2)
        
        self.driver.find_element_by_name('已审核家庭成员').click()
        time.sleep(2)

        self.driver.find_element_by_name('待审核家庭成员').click()
        time.sleep(2)

        self.driver.find_element_by_name('驳回').click()
        time.sleep(2)

        self.driver.find_element_by_name('取消').click()
        time.sleep(2)
                
        self.driver.find_element_by_class_name('android.widget.ImageView').click()
        time.sleep(2)
        
        self.driver.find_element_by_name('租客管理').click()
        time.sleep(2)
        
        self.driver.find_element_by_class_name('android.widget.ImageView').click()
        time.sleep(2)
        self.driver.find_element_by_class_name('android.widget.ImageView').click()
        time.sleep(2)
        
        self.driver.find_element_by_id('com.join.yaxin:id/function_layout_2').click()
        time.sleep(2)
        
        self.driver.find_element_by_id('com.join.yaxin:id/common_baoxiunew2_xiaoquaddress').click()
        time.sleep(2)
        
        self.driver.find_element_by_id('com.join.yaxin:id/authed_select_xiaoqu_ok').click()
        time.sleep(2)

        self.driver.find_element_by_id('com.join.yaxin:id/common_baoxiunew2_address_et').send_keys(u'中address testts')
        time.sleep(2)
        
        self.driver.find_element_by_id('com.join.yaxin:id/common_baoxiunew2_desc').send_keys('coment for test')
        time.sleep(2)
        
        self.driver.find_element_by_id('com.join.yaxin:id/iv_photo').click()
        time.sleep(2)
        
        self.driver.find_element_by_id('com.join.yaxin:id/v_selected').click()
        time.sleep(2)
        
        self.driver.find_element_by_id('com.join.yaxin:id/done').click()
        time.sleep(2)
        
        self.driver.find_element_by_id('com.join.yaxin:id/common_baoxiunew2_ok').click()
        time.sleep(2)
        
        self.driver.find_element_by_id('com.join.yaxin:id/item_baoxiuhistory_baoxiutype').click()
        time.sleep(2)

        self.driver.find_element_by_class_name('android.widget.ImageView').click()
        time.sleep(2)

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(LoginAndroidTests)
	unittest.TextTestRunner(verbosity=2).run(suite)

        
