#finds numbers in a not in b and in b not in a
#loop through item in list a
#loop through items in list b
#if there items in a that are not in b return those items
#if there are items(char) in b that are not in a return those item(char)

def missing_number(a,b):
	if len(a)==len (b):
		return list(0)
	else:
		maxlist = a
		if len (b) > len(a):
			maxlist = b
		else:
			minlist = a
		for num in maxlist:
			if num not in minlist:
				return num
