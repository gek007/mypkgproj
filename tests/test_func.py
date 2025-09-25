import unittest 
from mypkg import add, sub 

'''
This class checks functions - unit test 
'''

class TestFunc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(5, add(2,3))

    def test_sub(self):
        self.assertEqual(2, sub(5,3))   



if __name__ == "__main__":
    unittest.main()


