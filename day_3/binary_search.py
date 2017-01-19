class BinarySearch(List):
	def __init__(self,a,b):
		super(BinarySearch,self).__init__(range(0, (a*b)+1, b)[1:])
		self.length = a
	def search (self,value):
		max_n=0
		max_n = length
		l_list =[]
		f_value = False
		count =0
		while min_n<= max_n and f_value =False:
			mid = int((max_n+min_n)/2)
			count += 1
			if l_list[mid]== value:
				index = mid
				f_value = True
			elif l_list[mid] < value:
				min_n = mid +1
				f_value =False
			else: 
				max_n = mid -1
		return my_dict ={"count": count,"index":index} 





