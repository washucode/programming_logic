import unittest
from primes import all_prime
class test_case_primes(unittest.TestCase):
	
	'''def test_two_prime(self):
		self.assertTrue(all_prime(2))'''
	
	def test_one_not_prime(self):
		self.assertFalse(all_prime(1))

	def test_zero_not_prime(self):
		self.assertFalse(all_prime(0))

	def test_negativeone_notprime(self):
		self.assertFalse(all_prime(-1))

	def test_negativetwo_notprime(self):
		self.assertFalse(all_prime(-2))

	def test_negativethree_notprime(self):
		self.assertFalse(all_prime(-3))

	def test_negativefour_notprime(self):
		self.assertFalse(all_prime(-4))

	def test_negativefive_notprime(self):
		self.assertFalse(all_prime(-5))

	def test_negativesix_notprime(self):
		self.assertFalse(all_prime(-6))

	def test_negativeseven_notprime(self):
		self.assertFalse(all_prime(-7))

	def test_negativeEight_notprime(self):
		self.assertFalse(all_prime(-8))

	def test_negativenine_notprime(self):
		self.assertFalse(all_prime(-9))



	

if __name__== '__main__':
	unittest.main()
