import unittest
from  twosome import two_sum

class twoSomeTestCase(unittest.TestCase):

	def test_list_range_4(self):
		res = two_sum([2,5,1,7],8)
		self.assertEqual(res,[2,3])

	def test_list_range_5(self):
		res = two_sum([2,5,1,7,1],8)
		self.assertEqual(res,[2,3])

	def test_list_range_6(self):
		res = two_sum([2,5,1,7,6,4],10)
		self.assertEqual(res,[4,5])

	def test_list_range_7(self):
		res = two_sum([2,5,1,7,3,58,12],14)
		self.assertEqual(res,[0,6])

	def test_list_range_9(self):
		res = two_sum([2,9,1,7,56,88,12,123,45],10)
		self.assertEqual(res,[1,2])

	def test_list_range_10(self):
		res = two_sum([2,5,1,7,78,54,56,32,55,10],65)
		self.assertEqual(res,[8,9])

	def test_list_range_11(self):
		res = two_sum([2,5,1,7,78,54,56,32,55,10,23],65)
		self.assertEqual(res,[8,9])

	def test_list_range_12(self):
		res = two_sum([2,5,1,7,78,54,56,32,55,10,200,100],300)
		self.assertEqual(res,[10,11])

	def test_list_range_13(self):
		res = two_sum([2,5,1,7,78,54,56,32,55,10,1,5,6],7)
		self.assertEqual(res,[0,1])

	def test_list_range_14(self):
		res = two_sum([2,5,1,7,78,54,56,32,55,10,1,2,3,4],5)
		self.assertEqual(res,[11,12])











if __name__ == "__main__":
	unittest.main()