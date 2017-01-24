 

def words(my_string):
	#return a list of all items in string
	my_string = my_string.split() 
	count_dict = {} 
	for word in my_string:
		
		#find item of type integer
		if word.isdigit():           
			word = int (word) 
		if word in count_dict:
			count_dict[word] += 1
			
	return count_dict
	  
		


 


