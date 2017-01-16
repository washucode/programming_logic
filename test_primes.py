import unittest
from primes import all_prime
class test_case_primes(unittests.Testcase):
	def test_two_prime(self):
		self.assertTrue(all_prime(2))
