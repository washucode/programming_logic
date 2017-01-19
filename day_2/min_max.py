#this program 
#sorts array from the min value to the max value
#gets the min value
#gets the max value
#gets length of the array and appends to a new list and return it.


def find_max_min(my_array):
	my_array.sort()   
	new_list=[]
	
	my_min= my_array[0]

	my_max =my_array[-1]
	
	if my_min == my_max:
	   new_list.append(len(my_array)) 
	   return new_list
	else:   
	   new_list.append(my_min)
	   new_list.append(my_max)
	   return new_list 
