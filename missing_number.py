import unittest
"""
You are given an integer array which contains numbers from 1-100. but one number is missing.
What is the number.
"""



def missing(arr):
    sum = 0
    expected = 0

    for n in arr:
        sum = sum + n 
    for i in range(0,10):
        expected = expected + i  
    
    print("missing number is: {}".format(expected - sum))
    return expected - sum


class checkMissing(unittest.TestCase):

    def test_missing(self):
        array = [0,1,2,3,5,6,7,8,9]
        expected = 4
        actual = missing(array)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()



