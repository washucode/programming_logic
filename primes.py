def all_prime(n):

	for i in range(2,int(n**0.5)+1):
		if x in range(0,2):
			return False
		elif x%i ==0:
			return False
		else:
			return True
print 2
	
def gen_prime(n):
	for x in range (0,n+1):
		if all_prime(n):
			print x


		


