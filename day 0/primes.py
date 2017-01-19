#Takes a number,loops through the range (0 ,number+1)
#Returns an array of prime numbers including 2

def all_prime(n):
	for s in range (0,n+1):
		gen = True
		# insert formular used to calculate prime numbers
		#divides each number from range(0,n+1) by the square root of itself and 
		#all numbers less than that squarer root
		#if it is divisible by any of those number (square root and below)number is #not prime

		for i in range(2,int(n**0.5)+1):
			if s% i == 0:
				gen = False
			elif s==2:
				gen = True 
			elif s in range(0,2):
			  gen = Fals
			else:
				gen = True
		if gen ==True:
		  return s




		
	



		



