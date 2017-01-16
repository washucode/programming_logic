def all_prime(n):
	for i in range(2,int(n**0.5)+1):
		if x < 2:
			return False
		elif x ==2:
			return True
		elif x%i ==0:
			return False
		else:
			return True


for x in range (0,n+1):
	if all_prime(n):
		print x


		


