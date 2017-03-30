#-*- coding: UTF-8 -*-
import os
import time
import unittest
from appium import webdriver
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
        desired_caps['app'] = PATH('F:\\wanghailongworkspace\\apk_package\\app_v(20170113)_2017-01-19_yingyongbao_debug')#被测试的App在电脑上的位置
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
 
#如果知道被测试对象的apppage，appActivity可以加上下面这两个参数，如果不知道，可以注释掉，不影响用例执行
#      desired_caps['appPackage']='com.join.yaxin'
#      desired_caps['appActivity']='.MainActivity'

        self.driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
        time.sleep(6)


    def tearDown(self):
        self.driver.quit()
        time.sleep(2)
   
    def test_login(self):
        time.sleep(2)
#登录注册

        #电话号码
        self.driver.find_element_by_id('com.join.yaxin:id/userName').send_keys('18307552006')
        time.sleep(1)
        #密码
        self.driver.find_element_by_id('com.join.yaxin:id/userPwd').send_keys('123456')
        time.sleep(1)
        #登录
        self.driver.find_element_by_id('com.join.yaxin:id/btn_login').click()
        time.sleep(4)

  
#七彩芯
# 开发优化代码将name android.widget.ImageView替换为id  com.join.yaxin:id/tv_back

    #扫码开门
        self.driver.find_element_by_id('com.join.yaxin:id/function_layout_1').click()
        time.sleep(2)
        #导航信息
        #向左滑动
        swipetestaction.swipeLeft(self,1000)
        time.sleep(1)
        #向右滑动
        swipetestaction.swipeRight(self,1000)
        time.sleep(1)
        #关闭导航
        self.driver.find_element_by_id('com.join.yaxin:id/iv_dismiss_dialog').click()
        time.sleep(1)
        #查找二维码
        self.driver.find_element_by_id('com.join.yaxin:id/qr_img')
        #刷新二维码
        self.driver.find_element_by_id('com.join.yaxin:id/qr_refresh_btn').click()
        time.sleep(2)
        #返回首页
        self.driver.find_element_by_id('com.join.yaxin:id/tv_back').click()
        time.sleep(2)        
    #指纹管理
        self.driver.find_element_by_id('com.join.yaxin:id/function_layout_5').click()
        time.sleep(2)
        #去录入
        self.driver.find_element_by_id('com.join.yaxin:id/item_zhiwen_new_check').click()
        time.sleep(2)
        #self.driver.find_element_by_name('正在查询...')
        #time.sleep(12)
        #选择闸机
        #self.driver.find_element_by_id('com.join.yaxin:id/item_gate_manage_state').click()
        #time.sleep(2)
        #下一步
        self.driver.find_element_by_id('com.join.yaxin:id/gate_manage__ok').click()
        time.sleep(2)
        #返回首页
        self.driver.find_element_by_id('com.join.yaxin:id/tv_back').click()
        time.sleep(2)
        self.driver.find_element_by_id('com.join.yaxin:id/tv_back').click()
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
        #返回首页           
        for num in range(0,2):
            self.driver.find_element_by_id('com.join.yaxin:id/tv_back').click()
            time.sleep(3)      
    #投诉 进入投诉
        self.driver.find_element_by_id('com.join.yaxin:id/function_layout_3').click()
        time.sleep(2)
        #投诉小区选择
        self.driver.find_element_by_id('com.join.yaxin:id/common_tousunew2_xiaoquaddress').click()
        time.sleep(2)       
        self.driver.find_element_by_id('com.join.yaxin:id/authed_select_xiaoqu_ok').click()
        time.sleep(2)
        #投诉地址填写
        self.driver.find_element_by_id('com.join.yaxin:id/common_tousunew2_address_et').send_keys(u'投诉address testts')
        time.sleep(2)
        #投诉内容填写
        self.driver.find_element_by_id('com.join.yaxin:id/common_tousunew2_desc').send_keys(u'投诉内容coment for test')
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
        #投诉提交
        self.driver.find_element_by_id('com.join.yaxin:id/common_tousunew2_ok').click()
        time.sleep(5)        
        #查看投诉
        self.driver.find_element_by_id('com.join.yaxin:id/item_tousuhistory_tousudescribe').click()
        time.sleep(3)
        #返回首页
        for num in range(0,2):
            self.driver.find_element_by_id('com.join.yaxin:id/tv_back').click()
            time.sleep(3)

    #新闻活动
        self.driver.find_element_by_id('com.join.yaxin:id/function_layout_6').click()
        time.sleep(2)
      #社区新闻#打开新闻
        self.driver.find_element_by_id('com.join.yaxin:id/communitynews_itemsTitle').click()
        time.sleep(2)
         #向上滑动
        swipetestaction.swipeUp(self,100)
        time.sleep(1)
        swipetestaction.swipeUp(self,100)
        time.sleep(1)
        #返回新闻活动
        self.driver.find_element_by_id('com.join.yaxin:id/tv_back').click()
        time.sleep(2)
      #活动报名
        self.driver.find_element_by_name('活动报名').click()
        time.sleep(2)
        #选择活动
        self.driver.find_element_by_id('com.join.yaxin:id/huodong_itemsTitle').click()
        time.sleep(2)
        #向上滑动
        swipetestaction.swipeUp(self,1000)
        time.sleep(2)     
        #我要报名
        self.driver.find_element_by_xpath('//android.widget.TextView[contains(@content-desc,我要报名)]')
        time.sleep(2) 
        #self.driver.find_element_by_class_name('android.view.View').click()
        #time.sleep(2)
        #返回新闻活动
        self.driver.find_element_by_id('com.join.yaxin:id/tv_back').click()
        time.sleep(2)
      #问卷调查
        self.driver.find_element_by_name('问卷调查').click()
        time.sleep(3)
        #选择问卷
        self.driver.find_element_by_id('com.join.yaxin:id/wenjuan_itemsTitle').click()
        time.sleep(2)
        #返回新闻活动
        self.driver.find_element_by_id('com.join.yaxin:id/tv_back').click()
        time.sleep(2)
      #热门投票
        self.driver.find_element_by_name('热门投票').click()
        time.sleep(3)
        #选择投票
        self.driver.find_element_by_id('com.join.yaxin:id/toupiao_itemsTitle').click()
        time.sleep(2)
        #返回新闻活动
        self.driver.find_element_by_id('com.join.yaxin:id/tv_back').click()
        time.sleep(2)
      #议事大厅
        self.driver.find_element_by_name('议事大厅').click()
        time.sleep(3)
        #选择议事
        self.driver.find_element_by_id('com.join.yaxin:id/yishidating_itemsTitle').click()
        time.sleep(3)        
        #填写评论
        self.driver.find_element_by_class_name('android.widget.EditText').send_keys('coment for test议事意见。')
        time.sleep(5)
        #提交评论
        self.driver.find_element_by_class_name('android.widget.Button').click()
        time.sleep(5)
        #确认提交
        self.driver.find_element_by_xpath('//android.widget.TextView[contains(@content-desc,确定)]').click()
        time.sleep(2)                                
        #返回新闻活动
        self.driver.find_element_by_id('com.join.yaxin:id/tv_back').click()
        time.sleep(3)        
        #返回首页
        #self.driver.find_element_by_id('com.join.yaxin:id/tv_back').click()
        #time.sleep(2)        
    #家政服务
        self.driver.find_element_by_id('com.join.yaxin:id/function_layout_7').click()
        time.sleep(2)
        #返回首页
        self.driver.find_element_by_id('com.join.yaxin:id/tv_back').click()
        time.sleep(2)        
    #房产信息        
        self.driver.find_element_by_id('com.join.yaxin:id/function_layout_8').click()
        time.sleep(2)
        #房产详情
        self.driver.find_element_by_id('com.join.yaxin:id/housesource_itemsTitle').click()
        time.sleep(2)
        #返回房产
        self.driver.find_element_by_id('com.join.yaxin:id/tv_back').click()
        time.sleep(2)
        #房产详情
        self.driver.find_element_by_id('com.join.yaxin:id/housesource_itemsDiZhi').click()
        time.sleep(2)
        #返回房产
        self.driver.find_element_by_id('com.join.yaxin:id/tv_back').click()
        time.sleep(2)
        #联系电话
        self.driver.find_element_by_id('com.join.yaxin:id/housesource_phonetext').click()
        time.sleep(2)
        #点击确定
        self.driver.find_element_by_id('android:id/button1').click()
        time.sleep(2)
        #返回首页
        self.driver.find_element_by_id('com.join.yaxin:id/tv_back').click()
        time.sleep(2)
    #新房产信息
        #房产详情
        self.driver.find_element_by_id('com.join.yaxin:id/housesource_itemsIcon').click()
        time.sleep(2)
        #返回首页
        self.driver.find_element_by_id('com.join.yaxin:id/tv_back').click()
        time.sleep(2)
        #房产详情
        self.driver.find_element_by_id('com.join.yaxin:id/housesource_itemsText').click()
        time.sleep(2)
        #返回首页
        self.driver.find_element_by_id('com.join.yaxin:id/tv_back').click()
        time.sleep(2)
        #联系电话
        self.driver.find_element_by_id('com.join.yaxin:id/housesource_phonelayout').click()
        time.sleep(2)
        #点击确定
        self.driver.find_element_by_id('android:id/button1').click()
        time.sleep(2)             

    #生活缴费
        self.driver.find_element_by_id('com.join.yaxin:id/function_layout_4').click()
        time.sleep(2)
        #缴费房间
        self.driver.find_element_by_id('com.join.yaxin:id/tv_pay_address').click()
        time.sleep(2)
        #确认提交
        self.driver.find_element_by_id('com.join.yaxin:id/authed_select_xiaoqu_ok').click()
        time.sleep(2)
        #缴费历史
        self.driver.find_element_by_id('com.join.yaxin:id/iv_state').click()
        time.sleep(2)
        #向上滑动
        swipetestaction.swipeUp(self,1000)
        time.sleep(2)
        #返回缴费页面
        self.driver.find_element_by_id('com.join.yaxin:id/tv_back').click()
        time.sleep(2)
        #去缴费
        self.driver.find_element_by_id('com.join.yaxin:id/tv_go_pay').click()
        time.sleep(2)
        #手机返回键
        self.driver.keyevent(4)
        time.sleep(2)
        #返回首页
        self.driver.find_element_by_id('com.join.yaxin:id/tv_back').click()
        time.sleep(2)

        print("七彩芯模块脚本跑完了")
        time.sleep(5)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
    LoginAndroidTests

