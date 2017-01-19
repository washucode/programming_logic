def find_max_min(my_array):
	my_array.sort()
	'''sorts array from the min value to the max value'''
	new_list=[]
	
	my_min= my_array[0]'''gets the min value'''

	my_max =my_array[-1]'''gets the max value'''
	
	if my_min == my_max:
	   new_list.append(len(my_array)) '''gets length of the array and appends to a new list and return the list'''
	   return new_list
	else:   
	   new_list.append(my_min)
	   new_list.append(my_max)
	   return new_list '''returns a list in the form [min value,max value]
