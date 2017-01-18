#!/usr/bin/env python
# -*- coding: utf-8 -*- 



def words(my_string):
	my_string = my_string.split()
	count_dict = {}
	for word in my_string:
		if word.isdigit():
			if int(word) in count_dict:
				count_dict[int(word)] += 1
			else:
				count_dict[int(word)] = 1
		else:
			if word in count_dict:
				count_dict[word] += 1
			else:
				count_dict[word] = 1
	return count_dict
	  
		


 


