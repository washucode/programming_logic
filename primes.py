def all_prime(n):
	for x in range (0,n+1):
		
		for i in range(2,int(n**0.5)+1):
			if x % i == 0:
				return False
			elif x==2:
				return True
			elif  x in range (0,2):
				return False
			else:
				return True
		if True:
			print x

		
	



		


