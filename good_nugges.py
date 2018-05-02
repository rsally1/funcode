from functools import reduce
import unittest


def compute(arr):
    print(arr)
    sum = reduce((lambda x, y: x + y), arr )
    return sum


class CheckSum(unittest.TestCase):

    def test_sum(self):
        
        arr = [0,1,2,3,4,5,6,7,9]
        exp = [x for x in range(0,10)]
        actual = compute(arr)
        expected = compute(exp)
        self.assertEqual(expected-actual, 8)



if __name__ == '__main__':
    unittest.main()