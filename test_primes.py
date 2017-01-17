import unittest
from primes import all_prime
class test_case_primes(unittest.TestCase):
	
	'''def test_two_prime(self):
		self.assertTrue(all_prime(2))'''
	
	def test_one_not_prime(self):
		self.assertFalse(all_prime(1))
		

if __name__== '__main__':
	unittest.main()
