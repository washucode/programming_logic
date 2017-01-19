#define a BinarySearch class(child class)
#class super class constructor


class BinarySearch(List):
	def __init__(self,a,b):
		super(BinarySearch,self).__init__(range(0, (a*b)+1, b)[1:])
		self.length = a
	def search (self,value):
		#minimum value  of the number indices =0
		min_n=0            
		# minimum value of number indices = length of list -1 
		max_n = length - 1  
		l_list =[]
		# initialize found value = 0
		f_value = False    
		count =0
		index = 0
		#if value not found,max!=min,max<min
		while min_n<= max_n and f_value =False:  
			#find middle index
			mid = int((max_n+min_n)/2)  
			#add 1  to count to get number of iteration
			count += 1                  
			if l_list[mid]== value:
				index = mid
				f_value = True
			elif l_list[mid] < value:
				# set minimum index to sum of 1 and mid
				min_n = mid +1             
				f_value =False
			else: 
				max_n = mid -1
		return my_dict ={"count": count,"index":index} 





