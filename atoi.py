
import unittest

"""
to run: python atoi.py
"""

def atoi(somestr):
	"""
	unicode 0=48,9=57
	"""
	table = [48,49,50,51,52,53,54,55,56,57]
	res = []
	num = []
	sign = 1
	answer = 0
	if somestr[0] == "-":
		sign = -1
	for s in somestr:
		d = ord(s)
		res.append(d)
		num.append(table.index(d))
	
	num.reverse()
	
	# need the units, tens, 100s position. reversed makes it easy to compte
	# 10 ** 0 ==> 1 squared position 0 = 1 ie units
	# 10 ** 1 ==> 10 squared position 1 ie 10's
	# 10 ** 2 ==> 100's and so on

	for i in range(0, len(num)):
		n = 10 ** i
		answer = answer + (num[i] * n)	
	return answer * sign


class TestThisNow(unittest.TestCase):

	
	def test_3(self):
		string = "546"
		answer = atoi(string)
		self.assertEqual(answer, 546)
		answer = atoi("9991")
		self.assertEqual(answer, 9991)


if __name__ == '__main__':
	unittest.main()