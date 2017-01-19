#Used to generate house type,house location 
#and house price
#house types include flats,mansionnetts,mansions
#and bungalows
class house(object):
	def __init__(self,house_type="",location=""):
		self.house_type =house_type
		self.location = self.location

	

	if self.house_type == "mansion":
		self.no_of_bedrooms = 6
	elif self.house_type == "mansionnettes":
		self.no_of_bedrooms = 4
	else:
		self.no_of_bedrooms = 3

	
	def has_backyard(self):
		if self.house_type == "flat":
			return "No backyard"
		else:
			return "Has a backyard"	

	def area_location(self,location):
		if self.location = "within the city":
			self.lowest_prize = 10000000
		else:
			self.lowest_prize = 7000000







