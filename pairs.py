import unittest

"""
How to find all pairs on integer array whose sum is equal to a given number
example [1,3,6,9] and 9
The answer is 3,6
"""

def find_pair(arr, target):
    """ Complexity is O(N^2"""
    x = 0
    y = 0

    for n in arr:
        for j in arr:
            if n + j == target:
                x = n 
                y = j
                break
    return (x,y)


class TestPair(unittest.TestCase):

    def test_pair_find(self):
        arr = [2,7,4,1,15]
        target = 5
        res = find_pair(arr, target)
        print(res)
        self.assertEqual((1,4), res)

        arr = [1,3,6,7]
        target = 9
        res = find_pair(arr, target)
        print(res)
        self.assertEqual((6,3), res)


if __name__ == '__main__':
    unittest.main()