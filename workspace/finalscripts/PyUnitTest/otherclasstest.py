
# -*- coding: utf-8 -*-
import unittest
from testclass import testnum
import HTMLTestRunner
class testNum(unittest.TestCase):
    def setUp(self):
        print("初始化")
        self.testmodel = testnum()
    def tearDown(self):
        print("结束")
        pass
    def testSum(self):
        self.assertEqual(2,self.testmodel.sumnum(1,1))
        self.assertEqual(0,self.testmodel.delnum(1,1))
if __name__ == '__main__':
    suite1 = unittest.TestLoader().loadTestsFromTestCase(testNum)
    unittest.TextTestRunner(verbosity=3).run(suite1)