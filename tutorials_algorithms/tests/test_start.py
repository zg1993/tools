# coding: utf8


import unittest


class StartTest(unittest.TestCase):
    def test_case56(self):
        print ('test_case1')

    def test_acase4(self):
        print ('test_case2')

    def test_case55(self):
        print ('test_case3')

if __name__ == '__main__':
    # unittest.main()

    # suite = unittest.TestSuite()
    # suite.addTest(StartTest.test_case3)
    # suite.addTest(StartTest.test_case2)
    runner = unittest.TextTestRunner()
    # runner.run(suite)
    
    discover = unittest.defaultTestLoader.discover('./', pattern='test_*.py')
    print (type(discover))
    runner.run(discover)
