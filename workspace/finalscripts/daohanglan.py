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
        desired_caps['version']='4.4.2'
        desired_caps['deviceName']='127.0.0.1:62001'#这是测试机的型号，可以查看手机的关于本机选项获得
        desired_caps['app'] = PATH('F:\\wanghailongworkspace\\apk_package\\app_v(20170113)_2017-01-19_yingyongbao_debug.apk')#被测试的App在电脑上的位置
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True

        
#如果知道被测试对象的apppage，appActivity可以加上下面这两个参数，如果不知道，可以注释掉，不影响用例执行
#      desired_caps['appPackage']='com.join.yaxin'
#      desired_caps['appActivity']='.MainActivity'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
        time.sleep(6)


  #  def tearDown(self):
   #     self.driver.quit()
    #    time.sleep(2)
   
    def test_login(self):
        time.sleep(2)
#登录注册

        #电话号码
        self.driver.find_element_by_id('com.join.yaxin:id/userName').send_keys('18307552003')
        time.sleep(1)
        #密码
        self.driver.find_element_by_id('com.join.yaxin:id/userPwd').send_keys('123456')
        time.sleep(1)
        #登录
        self.driver.find_element_by_id('com.join.yaxin:id/login_layout').click()
        time.sleep(4)

# 开发优化代码将name android.widget.ImageView替换为id  com.join.yaxin:id/tv_back

#消息中心
        self.driver.find_element_by_id('com.join.yaxin:id/iv_state').click()
        time.sleep(2)
        self.driver.find_element_by_name('评论').click()
        time.sleep(2)
        self.driver.find_element_by_name('私信').click()
        time.sleep(2)
        self.driver.find_element_by_name('通知').click()
        time.sleep(2)
        #查看通知
        self.driver.find_element_by_id('com.join.yaxin:id/notice_itemsTitle').click()
        time.sleep(2)
        #self.driver.find_element_by_id('com.join.yaxin:id/check_detail_state')
        #time.sleep(2)
        #返回消息中心
        self.driver.find_element_by_id('com.join.yaxin:id/tv_back').click()
        time.sleep(2)
        #消息筛选
        self.driver.find_element_by_id('com.join.yaxin:id/iv_state').click()
        time.sleep(2)
        self.driver.find_element_by_name('成员审核').click()
        time.sleep(2)
        self.driver.find_element_by_id('com.join.yaxin:id/iv_state').click()
        time.sleep(2)
        self.driver.find_element_by_name('社区公告').click()
        time.sleep(2)
        self.driver.find_element_by_id('com.join.yaxin:id/iv_state').click()
        time.sleep(2)
        self.driver.find_element_by_name('报修反馈').click()
        time.sleep(2)
        self.driver.find_element_by_id('com.join.yaxin:id/iv_state').click()
        time.sleep(2)
        self.driver.find_element_by_name('业主审核').click()
        time.sleep(2)
        self.driver.find_element_by_id('com.join.yaxin:id/iv_state').click()
        time.sleep(2)
        self.driver.find_element_by_name('全部通知').click()
        time.sleep(2)
        #返回首页
        self.driver.find_element_by_id('com.join.yaxin:id/tv_back').click()
        time.sleep(2)


#进入呼叫中心
        self.driver.find_element_by_id('com.join.yaxin:id/iv_menu').click()
        time.sleep(4)
        #标题查找
        self.driver.find_element_by_name('呼叫中心')
        time.sleep(2)
        #一键呼叫
        self.driver.find_element_by_id('com.join.yaxin:id/tv_call').click()
        time.sleep(4)
        self.driver.keyevent(4)
        #返回首页
        self.driver.find_element_by_id('com.join.yaxin:id/tv_back').click()
        time.sleep(2)        
#进入我的小区住址
        self.driver.find_element_by_id('com.join.yaxin:id/tv_title').click()
        time.sleep(2)
    #业主认证
        self.driver.find_element_by_id('com.join.yaxin:id/iv_state').click()
        time.sleep(2)
	#选择小区
        self.driver.find_element_by_id('com.join.yaxin:id/authowner_xiaoqu_layout').click()
        time.sleep(2)
        self.driver.find_element_by_name('橄榄城柏林印象').click()
        time.sleep(2)
        #选择姓名
        self.driver.find_element_by_id('com.join.yaxin:id/authowner_username_tv').click()
        time.sleep(2)
        self.driver.find_element_by_id('com.join.yaxin:id/username_ok').click()
        time.sleep(2)
        #选择身份证号
        self.driver.find_element_by_id('com.join.yaxin:id/authowner_cardid_tv').click()
        time.sleep(2)
        self.driver.find_element_by_id('com.join.yaxin:id/shenfenzheng_ok').click()
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
        self.driver.find_element_by_id('com.join.yaxin:id/iv_state').click()
        time.sleep(2)
	#选择小区
        self.driver.find_element_by_id('com.join.yaxin:id/authowner_xiaoqu_layout').click()
        time.sleep(2)
        self.driver.find_element_by_name('橄榄城柏林印象').click()
        time.sleep(2)
        #选择姓名
        self.driver.find_element_by_id('com.join.yaxin:id/authowner_username_tv').click()
        time.sleep(2)
        self.driver.find_element_by_id('com.join.yaxin:id/username_ok').click()
        time.sleep(2)
        #选择身份证号
        self.driver.find_element_by_id('com.join.yaxin:id/authowner_cardid_tv').click()
        time.sleep(2)
        self.driver.find_element_by_id('com.join.yaxin:id/shenfenzheng_ok').click()
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
        self.driver.find_element_by_id('com.join.yaxin:id/iv_state').click()
        time.sleep(2)
	#选择小区
        self.driver.find_element_by_id('com.join.yaxin:id/authowner_xiaoqu_layout').click()
        time.sleep(2)
        self.driver.find_element_by_name('橄榄城柏林印象').click()
        time.sleep(2)
        #选择姓名
        self.driver.find_element_by_id('com.join.yaxin:id/authowner_username_tv').click()
        time.sleep(2)
        self.driver.find_element_by_id('com.join.yaxin:id/username_ok').click()
        time.sleep(2)
        #选择身份证号
        self.driver.find_element_by_id('com.join.yaxin:id/authowner_cardid_tv').click()
        time.sleep(2)
        self.driver.find_element_by_id('com.join.yaxin:id/shenfenzheng_ok').click()
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
    #审核情况
        self.driver.find_element_by_name('待审核').click()
        time.sleep(2)       
        self.driver.find_element_by_name('审核未通过').click()
        time.sleep(2)        
        self.driver.find_element_by_name('审核过').click()
    #家属管理
        time.sleep(2)
        self.driver.find_element_by_name('家属管理').click()
        time.sleep(2)
        self.driver.find_element_by_name('已审核家庭成员').click()
        time.sleep(2)
        self.driver.find_element_by_name('待审核家庭成员').click()
        time.sleep(2)
        #self.driver.find_element_by_name('驳回').click()
        #time.sleep(2)
        #self.driver.find_element_by_name('取消').click()
        #time.sleep(2)               
        self.driver.find_element_by_id('com.join.yaxin:id/tv_back').click()
        time.sleep(2)
    #租客管理
        self.driver.find_element_by_name('租客管理').click()
        time.sleep(2)        
        self.driver.find_element_by_id('com.join.yaxin:id/tv_back').click()
        time.sleep(2)
     #搬离此住处
    #  self.driver.find_element_by_name('搬离此住处').click()
     # time.sleep(2)
     # #取消
     # self.driver.find_element_by_id('android:id/button2').click()
     # time.sleep(2)
    #返回首页
        self.driver.find_element_by_id('com.join.yaxin:id/tv_back').click()
        time.sleep(2)
 
        print("导航栏脚本跑完了")
        time.sleep(10)       
        
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
