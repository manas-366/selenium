import unittest
import HtmlTestRunner

class UnitTestClass(unittest.TestCase):

    def setUp(self):
        print('Manas')
    def test1(self):
        print('python')
    def test2(self):
        print('selenium')
    def tearDown(self):
        print('bye')

if __name__=='__main__':
    # Create a test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(UnitTestClass)
    
    # Run with HtmlTestRunner
    runner = HtmlTestRunner.HTMLTestRunner(output='reports', verbosity=2)
    runner.run(suite)