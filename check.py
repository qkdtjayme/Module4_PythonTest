import unittest

def check(n):

    return n >= 100


class MyTest(unittest.TestCase):

    def test(self):
        self.assertTrue(check(50))
        
if __name__== '__main__':

    unittest.main()