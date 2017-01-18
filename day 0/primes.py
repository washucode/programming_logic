def all_prime(n):
	for s in range (0,n+1):
		gen = True
		for i in range(2,int(n**0.5)+1):
			if s% i == 0:
				gen = False
			elif s %2 ==0:
				gen = False

			elif s ==2:
				gen = True
			elif s in range(0,2):
			  gen = False
			else:
				gen = True
		if gen ==True:
		  print s




		
	



		



