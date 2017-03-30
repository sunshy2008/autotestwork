# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest,time,re
import HTMLTestRunner

class Baidu(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url="http://www.baidu.com"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_baidu_search(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").send_keys("selenium webdriver")
        driver.find_element_by_id("su").click()
        time.sleep(2)
        driver.close()

    def test_baidu_set(self):
        driver = self.driver
        driver.get(self.base_url+"/gaoji/preferences.html")
        driver.find_element_by_xpath('//*[@id="nr"]/option[2]').click()
        time.sleep(2)

        driver.find_element_by_xpath("//*[@id='save']").click()
        time.sleep(2)
        driver.switch_to_alert().accept()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verificationErrors)


if __name__ == '__main__':
    testunit = unittest.TestSuite()
    testunit.addTest(Baidu('test_baidu_search'))
    testunit.addTest(Baidu('test_baidu_set'))
    filename = 'F:\\wanghailongworkspace\\autotest\\htmlreport\\result.html'
    file_result = open(filename,'wb')

    runner = HTMLTestRunner.HTMLTestRunner(
        stream = file_result,
        title = 'Baidu Test Report',
        description = 'testcase demo'
        )
    runner.run(testunit)
