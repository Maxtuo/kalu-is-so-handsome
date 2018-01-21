class Sports(object):

	def __init__(self, name, country):
		self.name = name
		self.country = country
	
	def get_info(self):
		x = "i like to play " + self.name
		x += "i am from " + self.country
		return x
	
	def detail_info(self):
		y = " do you know " + self.name
		y += get_info()
max = Sports(name="football ", country="china")

print(max.get_info())