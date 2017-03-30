__author__ = 'Administrator'


# -*-coding:utf-8 -*-
import unittest
from interfaceproject.papi.httprequest import SendHttpRequest
from interfaceproject.papi.dataparse import jsonprase, xmlprase
import json

class TestSingleRequest(unittest.TestCase):
    def setUp(self):
        self.url = "http://114.55.40.35:806/V1/api/Sys/GetUKeySecAndUtcDiff?clientUtcDiff=1476352997"

    def test_Single_right(self):
        data = SendHttpRequest(self.url).get()
        print(data)
        json_data = jsonprase(data)
        value_a = json_data.json_exit()
        print(value_a)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSingleRequest)
    unittest.TextTestRunner(verbosity=1).run(suite)
