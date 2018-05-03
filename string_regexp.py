import re
import unittest

"""
Check if this string has digits only
"""

def find_num(somestr):
	match = re.match(r"(^\d+$)", somestr)
	if match:
		print(match.group(0))
		return True
	else:
		return False


class TestThisNow(unittest.TestCase):

	def test_match(self):
		res = find_num("12345")
		self.assertTrue(res)
		res = find_num("3abc344")
		self.assertFalse(res)



if __name__ == '__main__':
	unittest.main()

