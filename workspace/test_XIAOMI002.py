#-*- coding: UTF-8 -*-
import os
import time
import unittest
from appium import webdriver
from selenium.webdriver.common.keys import Keys
from lib2to3.pgen2.driver import Driver
from lib2to3.tests.support import driver
from autoteskwork import swipetestaction
 
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
        desired_caps['version']='4.4.4 KTU84P'
        desired_caps['deviceName']='HM 2LTE-CMCC'#这是测试机的型号，可以查看手机的关于本机选项获得
        desired_caps['app'] = PATH('F:\\wanghailongworkspace\\app_v(20161104)_2016-11-11.apk')#被测试的App在电脑上的位置
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
 
#如果知道被测试对象的apppage，appActivity可以加上下面这两个参数，如果不知道，可以注释掉，不影响用例执行
#      desired_caps['appPackage']='com.join.yaxin'
#      desired_caps['appActivity']='.MainActivity'

        self.driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
        time.sleep(6)


#    def getSize(self):
#        x = self.driver.get_window_size()['width']
#       y = self.driver.get_window_size()['height']
#        return (x, y)
    #向上滑动
#    def swipeUp(self,t):
#        l=self.getSize()
#        x1=int(l[0]*0.5)
#        y1=int(l[1]*0.75)
#        y2=int(l[1]*0.25)
#        self.driver.swipe(x1,y1,x1,y2,t)

    def tearDown(self):
        self.driver.quit()
        time.sleep(2)
   
    def test_login(self):
        time.sleep(2)
#登录注册

        #电话号码
        self.driver.find_element_by_id('com.join.yaxin:id/userName').send_keys('18307551189')
        time.sleep(1)
        #密码
        self.driver.find_element_by_id('com.join.yaxin:id/userPwd').send_keys('123456')
        time.sleep(1)
        #登录
        self.driver.find_element_by_id('com.join.yaxin:id/login_layout').click()
        time.sleep(4)
    #进入呼叫中心
        self.driver.find_element_by_class_name('android.widget.ImageView').click()
        time.sleep(4)
        
        self.driver.find_element_by_name('呼叫中心')
        time.sleep(2)
        
        self.driver.find_element_by_class_name('android.widget.ImageView').click()
        time.sleep(2)
    #进入我的小区住址
        self.driver.find_element_by_class_name('android.widget.Button').click()
        time.sleep(2)
	#业主认证
        self.driver.find_element_by_id('com.join.yaxin:id/moreBtn2').click()
        time.sleep(2)
	#选择小区
        self.driver.find_element_by_id('com.join.yaxin:id/authowner_xiaoqu_layout').click()
        time.sleep(2)
        self.driver.find_element_by_name('橄榄城柏林印象').click()
        time.sleep(2)
	#楼栋号
        self.driver.find_element_by_id('com.join.yaxin:id/authowner_loudong_layout').click()
        time.sleep(2)
        self.driver.find_element_by_id('com.join.yaxin:id/options1')
        time.sleep(2)
        swipetestaction.swipeUp(self,100)
        time.sleep(1)
        self.driver.find_element_by_id('com.join.yaxin:id/btnSubmit').click()
        time.sleep(2)	
	#房间号
        self.driver.find_element_by_id('com.join.yaxin:id/authowner_roomid_layout').click()
        time.sleep(2)
        self.driver.find_element_by_id('com.join.yaxin:id/options1').click()
        time.sleep(2)
        swipetestaction.swipeUp(self,100)
        time.sleep(1)
        self.driver.find_element_by_id('com.join.yaxin:id/btnSubmit').click()
        time.sleep(2)
        #身份选择
        self.driver.find_element_by_id('com.join.yaxin:id/authenticate_owner_radioId1').click()
        time.sleep(2)
        #生成预览
        self.driver.find_element_by_id('com.join.yaxin:id/authowner_ok').click()
        time.sleep(2)
        #提交认证
        self.driver.find_element_by_name('提交认证').click()
        time.sleep(2)
        #家属认证
        self.driver.find_element_by_id('com.join.yaxin:id/moreBtn2').click()
        time.sleep(2)
	#选择小区
        self.driver.find_element_by_id('com.join.yaxin:id/authowner_xiaoqu_layout').click()
        time.sleep(2)
        self.driver.find_element_by_name('橄榄城柏林印象').click()
        time.sleep(2)
	#楼栋号
        self.driver.find_element_by_id('com.join.yaxin:id/authowner_loudong_layout').click()
        time.sleep(2)
        self.driver.find_element_by_id('com.join.yaxin:id/options1')
        time.sleep(1)
        swipetestaction.swipeUp(self,100)
        time.sleep(1)
        self.driver.find_element_by_id('com.join.yaxin:id/btnSubmit').click()
        time.sleep(2)	
	#房间号
        self.driver.find_element_by_id('com.join.yaxin:id/authowner_roomid_layout').click()
        time.sleep(2)
        self.driver.find_element_by_id('com.join.yaxin:id/options1')
        time.sleep(2)
        swipetestaction.swipeUp(self,100)
        time.sleep(1)
        self.driver.find_element_by_id('com.join.yaxin:id/btnSubmit').click()
        time.sleep(2)
        #身份选择
        self.driver.find_element_by_id('com.join.yaxin:id/authenticate_owner_radioId2').click()
        time.sleep(1)
        #生成预览
        self.driver.find_element_by_id('com.join.yaxin:id/authowner_ok').click()
        time.sleep(2)
        #提交认证
        self.driver.find_element_by_name('提交认证').click()
        time.sleep(2)
        #租客认证
        self.driver.find_element_by_id('com.join.yaxin:id/moreBtn2').click()
        time.sleep(2)
	#选择小区
        self.driver.find_element_by_id('com.join.yaxin:id/authowner_xiaoqu_layout').click()
        time.sleep(2)
        self.driver.find_element_by_name('橄榄城柏林印象').click()
        time.sleep(2)
	#楼栋号
        self.driver.find_element_by_id('com.join.yaxin:id/authowner_loudong_layout').click()
        time.sleep(2)
        self.driver.find_element_by_id('com.join.yaxin:id/options1')
        time.sleep(1)
        swipetestaction.swipeUp(self,100)
        time.sleep(1)
        self.driver.find_element_by_id('com.join.yaxin:id/btnSubmit').click()
        time.sleep(2)	
	#房间号
        self.driver.find_element_by_id('com.join.yaxin:id/authowner_roomid_layout').click()
        time.sleep(2)
        self.driver.find_element_by_id('com.join.yaxin:id/options1')
        time.sleep(2)
        swipetestaction.swipeUp(self,100)
        time.sleep(1)
        self.driver.find_element_by_id('com.join.yaxin:id/btnSubmit').click()
        time.sleep(2)
        #身份选择
        self.driver.find_element_by_id('com.join.yaxin:id/authenticate_owner_radioId3').click()
        time.sleep(1)
        #生成预览
        self.driver.find_element_by_id('com.join.yaxin:id/authowner_ok').click()
        time.sleep(2)
        #提交认证
        self.driver.find_element_by_name('提交认证').click()
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
#进入报修
        self.driver.find_element_by_id('com.join.yaxin:id/function_layout_2').click()
        time.sleep(2)
        #报修小区选择
        self.driver.find_element_by_id('com.join.yaxin:id/common_baoxiunew2_xiaoquaddress').click()
        time.sleep(2)
        
        self.driver.find_element_by_id('com.join.yaxin:id/authed_select_xiaoqu_ok').click()
        time.sleep(2)
        #报修地址填写
        self.driver.find_element_by_id('com.join.yaxin:id/common_baoxiunew2_address_et').send_keys(u'中address testts')
        time.sleep(2)
        #报修内容填写
        self.driver.find_element_by_id('com.join.yaxin:id/common_baoxiunew2_desc').send_keys('coment for test')
        time.sleep(2)
        #点击添加图片
        self.driver.find_element_by_id('com.join.yaxin:id/iv_photo').click()
        time.sleep(2)
        #选择图片
        self.driver.find_element_by_id('com.join.yaxin:id/v_selected').click()
        time.sleep(2)
        #图片上传
        self.driver.find_element_by_id('com.join.yaxin:id/done').click()
        time.sleep(2)
        #向上滑动
        swipetestaction.swipeUp(self,1000)
        #报修提交
        self.driver.find_element_by_id('com.join.yaxin:id/common_baoxiunew2_ok').click()
        time.sleep(5)
        
        #查看报修
        self.driver.find_element_by_id('com.join.yaxin:id/item_baoxiuhistory_baoxiutype').click()
        time.sleep(3)
        #返回
        for num in range(0,2):
            self.driver.find_element_by_class_name('android.widget.ImageView').click()
            time.sleep(3)
        #else:
        #   print ("返回出错了")

        print("脚本跑完了")
        time.sleep(10)
#扫码开门
        self.driver.find_element_by_id('com.join.yaxin:id/function_layout_1').click()
        time.sleep(2)
        self.driver.find_element_by_id('com.join.yaxin:id/qr_img')
        #刷新二维码
        self.driver.find_element_by_id('com.join.yaxin:id/qr_refresh_btn').click()
        time.sleep(2)
        self.driver.find_element_by_class_name('android.widget.ImageView')
        time.sleep(2)
        
#指纹管理
        self.driver.find_element_by_id('com.join.yaxin:id/function_layout_5').click()
        com.join.yaxin:id/item_zhiwen_new_check
        self.driver.find_element_by_id('com.join.yaxin:id/function_layout_5').click()
        
        
        
        
        #投诉
#生活缴费

#新闻活动
#家政服务
#房产信息
#我的

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
    LoginAndroidTests

        
