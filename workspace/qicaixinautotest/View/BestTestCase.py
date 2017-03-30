__author__ = 'Administrator'
import unittest
from appium import webdriver
import config
import os
import time

PATH=lambda p:os.path.abspath(
os.path.join(os.path.dirname(__file__),p)
)

class AppTestCase(unittest.TestCase):
    def setUp(self):
        desired_caps = {
            'device': config.CONNECT['device'],
            'platformName': config.CONNECT['platformName'],
            'platformVersion': config.CONNECT['platformVersion'],
            'deviceName': config.CONNECT['deviceName'],
            'appPackage': config.CONNECT['appPackage'],
            'appActivity': config.CONNECT['appActivity'],
            'unicodeKeyboard': True,
            'resetKeyboard': True
        }
        self.driver = webdriver.Remote(config.CONNECT['baseUrl'], desired_caps)
        #self.driver.implicitly_wait(30)
    def get_driver(self):
        return self.driver
    def tearDown(self):
        self.driver.quit()

