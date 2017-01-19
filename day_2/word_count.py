#program used to take a string and find number of occurences of items in string

#caters for international characters
#!/usr/bin/env python
# -*- coding: utf-8 -*- 

def words(my_string):
	#return a list of all items in string
	my_string = my_string.split() 
	count_dict = {} 
	for word in my_string:
		
		#find item of type integer
		if word.isdigit():           
			# keeps track of  number occurences of numbers
			if int(word) in count_dict: 
				count_dict[int(word)] += 1
			else:
				count_dict[int(word)] = 1
		else:
			# keeps track of  number occurences of items
			if word in count_dict:  
				count_dict[word] += 1
			else:
				count_dict[word] = 1
	return count_dict
	  
		


 


