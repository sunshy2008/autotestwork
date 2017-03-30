__author__ = 'Administrator'
__author__ = 'Administrator'
#-*- coding: UTF-8 -*-
import os
import time
import unittest
from appium import webdriver
from selenium.webdriver.common.keys import Keys
from autoteskwork import swipetestaction
from TestCase import common
from View import BestTestCase
#from testelement import Element
from selenium.webdriver.common.by import By

PATH=lambda p:os.path.abspath(
os.path.join(os.path.dirname(__file__),p)
)

class LoginAndroidTests(unittest.TestCase):
    def test_login(self):
        common.WebDdriver.find_element(*(By.ID,'com.join.yaxin:id/userName'))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
    BestTestCase
    LoginAndroidTests



