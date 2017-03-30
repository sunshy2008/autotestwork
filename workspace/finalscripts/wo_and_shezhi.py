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
        desired_caps['app'] = PATH('F:\\wanghailongworkspace\\apk_package\\app_v(20170114)_2017-02-13_join_debug.apk')#被测试的App在电脑上的位置
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
        self.driver.find_element_by_id('com.join.yaxin:id/userName').send_keys('18307552003')
        time.sleep(1)
        #密码
        self.driver.find_element_by_id('com.join.yaxin:id/userPwd').send_keys('123456')
        time.sleep(1)
        #登录
        self.driver.find_element_by_id('com.join.yaxin:id/login_layout').click()
        time.sleep(4)

 # class_name android.widget.ImageView 替换为 id com.join.yaxin:id/tv_back       
        
#我的
        self.driver.find_element_by_name('我').click()
        time.sleep(2)
    #个人信息
        self.driver.find_element_by_id('com.join.yaxin:id/rl_person_info').click()
        time.sleep(2)
        #头像修改
        self.driver.find_element_by_id('com.join.yaxin:id/personinfo_touxiang_layout').click()
        time.sleep(2)
        #选择图片
        self.driver.find_element_by_id('com.join.yaxin:id/v_selected').click()
        time.sleep(2)
        #点击完成
        self.driver.find_element_by_id('com.join.yaxin:id/done').click()
        time.sleep(2)
        #昵称修改
        self.driver.find_element_by_id('com.join.yaxin:id/personinfo_editnickname').click()
        time.sleep(2)
        #输入昵称
        self.driver.find_element_by_id('com.join.yaxin:id/nickname_nickname').send_keys(u'沙漠1')
        time.sleep(2)
        #确认保存
        self.driver.find_element_by_id('com.join.yaxin:id/nickname_ok').click()
        time.sleep(2)
        #返回“我”
        self.driver.find_element_by_id('com.join.yaxin:id/tv_back').click()
        time.sleep(2)
    #我的账单
        self.driver.find_element_by_id('com.join.yaxin:id/fragment_my_zhangdan_layout').click()
        time.sleep(2)
        #返回“我”
        self.driver.find_element_by_id('com.join.yaxin:id/tv_back').click()
        time.sleep(2)
    #我的活动
        self.driver.find_element_by_id('com.join.yaxin:id/fragment_my_huodong_layout').click()
        time.sleep(2)
        #返回“我”
        self.driver.find_element_by_id('com.join.yaxin:id/tv_back').click()
        time.sleep(2)
    #访客通行
        self.driver.find_element_by_id('com.join.yaxin:id/fragment_my_fangke_layout').click()
        time.sleep(2)
        #添加访客
        self.driver.find_element_by_name('添加新访客').click()
        time.sleep(2)
        #访客姓名
        self.driver.find_element_by_id('com.join.yaxin:id/addfangke_name').send_keys(u'令狐冲')
        time.sleep(2)
        #访客电话
        self.driver.find_element_by_id('com.join.yaxin:id/addfangke_phonenumber').send_keys('18539265780')
        time.sleep(2)
        #访客身份证
        self.driver.find_element_by_id('com.join.yaxin:id/addfangke_shenfenzheng').send_keys('510105199010017999')
        time.sleep(2)
        #拜访时间
        self.driver.find_element_by_id('com.join.yaxin:id/addfangke_visittime').click()
        time.sleep(2)
        #确定访问时间
        self.driver.find_element_by_id('com.join.yaxin:id/btnSubmit').click()
        time.sleep(2)
        #生成访客凭证
        self.driver.find_element_by_id('com.join.yaxin:id/addfangke_ok').click()
        time.sleep(2)
        #查询是否生成凭证
        self.driver.find_element_by_id('com.join.yaxin:id/fangkeqr_img')
        time.sleep(2)
        #保存图片
        self.driver.find_element_by_id('com.join.yaxin:id/fangkeqr_screenshoot').click()
        time.sleep(2)
        #点击分享
        self.driver.find_element_by_id('com.join.yaxin:id/fangkeqr_share').click()
        time.sleep(2)
        #取消分享
        self.driver.find_element_by_id('android:id/button2').click()
        time.sleep(2)
        #检查生成手机号码
        self.driver.find_element_by_name('18539265780')
        time.sleep(2)
        #返回“我”
        self.driver.find_element_by_id('com.join.yaxin:id/tv_back').click()
        time.sleep(2)
        
    #指纹管理
        self.driver.find_element_by_id('com.join.yaxin:id/fragment_my_zhiwen_layout').click()
        time.sleep(2)
        #去录入
        self.driver.find_element_by_id('com.join.yaxin:id/item_zhiwen_new_check').click()
        time.sleep(6)
        #self.driver.find_element_by_name('正在查询...')
        #time.sleep(12)
        #选择闸机
        #self.driver.find_element_by_id('com.join.yaxin:id/item_gate_manage_state').click()
        #time.sleep(2)
        #下一步
        self.driver.find_element_by_id('com.join.yaxin:id/gate_manage__ok').click()
        time.sleep(2)
        #返回“指纹管理”
        self.driver.find_element_by_id('com.join.yaxin:id/tv_back').click()
        time.sleep(2)
        #返回“我”
        self.driver.find_element_by_id('com.join.yaxin:id/tv_back').click()
        time.sleep(2)
    #积分
        self.driver.find_element_by_id('com.join.yaxin:id/ll_current_score').click()
        time.sleep(2)

#设置
        self.driver.find_element_by_name('设置').click()
        time.sleep(2)
    #邀请加入
        self.driver.find_element_by_name('邀请加入').click()
        time.sleep(2)
        #分享app
        self.driver.find_element_by_id('com.join.yaxin:id/invitefriend_share_btn').click()
        time.sleep(2)
        #分享到微信
        self.driver.find_element_by_id('com.join.yaxin:id/invitefriend_share_weixin')
        time.sleep(1)
        #分享到微信朋友圈
        self.driver.find_element_by_id('com.join.yaxin:id/invitefriend_share_weixinquan')
        time.sleep(1)
        #分享到qq
        self.driver.find_element_by_id('com.join.yaxin:id/invitefriend_share_qq')
        time.sleep(1)
        self.driver.keyevent(4)
        time.sleep(2)
        #返回“设置”
        self.driver.find_element_by_id('com.join.yaxin:id/tv_back').click()
        time.sleep(2)            
    #账号与安全
        self.driver.find_element_by_name('账号与安全').click()
        time.sleep(2)
        #修改密码
        self.driver.find_element_by_name('修改密码').click()
        time.sleep(2)
        #原密码
        self.driver.find_element_by_id('com.join.yaxin:id/modifypwd_oldpassword').send_keys('456789')
        time.sleep(1)
        #新密码
        self.driver.find_element_by_id('com.join.yaxin:id/modifypwd_newpassword').send_keys('123456')
        time.sleep(1)
        #新密码
        self.driver.find_element_by_id('com.join.yaxin:id/modifypwd_newpassword1').send_keys('123456')
        time.sleep(1)
        #确认修改（暂时自动化不跑此功能）
        #self.driver.find_element_by_id('com.join.yaxin:id/modifypwd_ok').click()
        #time.sleep(1)
        #返回账号与安全
        self.driver.find_element_by_id('com.join.yaxin:id/tv_back').click()
        time.sleep(2)
        #返回设置
        self.driver.find_element_by_id('com.join.yaxin:id/tv_back').click()
        time.sleep(2)   
               
    #关于七彩芯
        self.driver.find_element_by_name('关于七彩芯').click()
        time.sleep(2)
        #去评分
        self.driver.find_element_by_name('去评分').click()
        time.sleep(2)
        #返回
        self.driver.keyevent(4)
        time.sleep(2)
        #检查新版
        self.driver.find_element_by_id('com.join.yaxin:id/about_checkversion_layout').click()
        time.sleep(1)
        #所有版本
        self.driver.find_element_by_name('所有版本').click()
        time.sleep(2)
        self.driver.find_element_by_name('版本历史')
        time.sleep(2)
        #向上滑动
        swipetestaction.swipeUp(self,1000)
        #返回
        self.driver.find_element_by_id('com.join.yaxin:id/tv_back').click()
        time.sleep(2)
        #帮助与反馈
        self.driver.find_element_by_name('帮助与反馈').click()
        time.sleep(2)
        #填写优化意见
        self.driver.find_element_by_id('com.join.yaxin:id/feedback_message').click()
        time.sleep(2)
        #提交意见
        self.driver.find_element_by_id('com.join.yaxin:id/feedback_send').click()
        time.sleep(2)
        #返回
        self.driver.find_element_by_id('com.join.yaxin:id/tv_back').click()
        time.sleep(2)
        #返回设置
        self.driver.find_element_by_id('com.join.yaxin:id/tv_back').click()
        time.sleep(2)       
        
    #退出
        self.driver.find_element_by_name('退出').click()
        time.sleep(2)
        self.driver.find_element_by_id('com.join.yaxin:id/quit_app_cancel').click()
        time.sleep(2)
        

        print("脚本跑完了")
        time.sleep(10)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
    LoginAndroidTests

        
