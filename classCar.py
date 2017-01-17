class Car(object_type):
	self.object_type = object_type

	def __init__(self,name= "General",model="GM",onject_type=""):
		self.object_type= object_type
		self.model =model
		self.name = name

	def car_prop(self,name,model):
		self.name = name
		self.model = model

	def car_doors(self,num_of_doors):
		self.num_of_doors = num_of_doors
		if self.model == Porshe:
			return num_of_doors == 2

		elif self.model == Koenugsegg:
			return num_of_doors == 2

		else:
			return num_of_doors == 4

	def car_wheels(self,num_of_wheels):
		self.num_of_wheels ==num_of_wheels
		if self.object_type == 'trailer':
			return num_of_wheels == 8

		else:
			return num_of_wheels == 4

	def car_type(self,object_type):
		self.object_type == object_type
		if object_type == 'salon':
			return 'trailer'

	def car_speed(self,packing_speed,moving_speed):
		self.parking_speed = parking_speed
		self.moving_speed = moving_speed
		if 'trailer':
			return packing_speed ==0

		else:
			return moving_speed == 77

	
	def car_speed2(self,parking_speed,moving_speed):
		self.parking_speed = parking_speed
		self.moving_speed = moving_speed
		if 'Mercedes':
			return parking_speed == 0:
		else:
			return moving_speed == 1000:


	def drive_car(self,moving_man)







