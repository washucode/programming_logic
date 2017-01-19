#finds numbers in a not in b and in b not in a
#loop through item in list a
#loop through items in list b
#if there items in a that are not in b return those items
#if there are items(char) in b that are not in a return those item(char)

def missing_number(a,b):
	if len(a)==len (b):
		return list(0)
	else:
		for item in a:
			for char in b:
				if item not in b:
					return list(set(a)-set(b))
				elif char not in a:
					return list(set(b)-set(a))
				else:
					pass

