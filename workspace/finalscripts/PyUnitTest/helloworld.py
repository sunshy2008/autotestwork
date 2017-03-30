# -*- coding: utf-8 -*-
import unittest

def sumnum(a,b):
    return a + b

def delnum(a,b):
    return a - b

def hello():
    return "hello world"

def chengfa(a,b):
    return a * b

class testNum(unittest.TestCase):
    def setUp(self):
        print ("初始化")

    def tearDown(self):
        print ("结束")
    def testSum(self):
        self.assertEqual(2,sumnum(1,1))

    def testDel(self):
        self.assertEqual(0,delnum(1,1))

    def testHello(self):
        self.assertEqual("hello world",hello())


class testChengFa(unittest.TestCase):
    def testChengFa(self):
        self.assertEqual(1,chengfa(1,1))

if __name__ == '__main__':
    #比如上面这一串代码，要怎么样同时测试testNum和testChengFa这两个类呢？
    #我们可以建立两个suite，然后放到一个列表里面，再直接运行即可，代码如下
    suite1 = unittest.TestLoader().loadTestsFromTestCase(testNum)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(testChengFa)
    alltest = unittest.TestSuite([suite1,suite2])
    unittest.TextTestRunner(verbosity=2).run(alltest)