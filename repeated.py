import unittest

"""
There is an aray with every element repeated twice except one. Find that element
"""
arr = [1,1,2,2,3,4,4,5,5]

def repeated_unique(arr):
    scanned = []
    sum_scanned = 0
    sum_dups = 0

    for n in arr:
        if n not in scanned:
            sum_scanned = sum_scanned + n 
            scanned.append(n)
        else:
            sum_dups = sum_dups + n 
    return sum_scanned - sum_dups


res = repeated_unique(arr)
print("Number not Repeated number is: {}".format(res))

class TestThis(unittest.TestCase):

    def test_number(self):
        arr = [90,90,95,95, 101,200,200]
        res = repeated_unique(arr)
        self.assertEqual(res, 101)
        print("Number is {}".format(res))

if __name__ == '__main__':
    unittest.main()