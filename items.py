################################		
########MAIN CLASSES############
################################
class Weapon:
	def __init__(self):
		raise NotImplementedError("Do not create raw Weapon objects!")
	
	def __str__(self):
		return self.name

class Consumable:
	def __init__(self):
		raise NotImplementedError("Do not create raw consumable objects!")
		
	def __str__(self):
		return "{} (+{} HP)".format(self.name, self.healing_value)


################################		
###########WEAPONS##############
################################

class Rock(Weapon):
	def __init__(self):
		self.name = "Rock"
		self.description = "A fist sized rock, suitable for beating"
		self.damage = 5

class Dagger(Weapon):
	def __init__(self):
		self.name = "Dagger"
		self.description = "A small dagger with some rust. Somewhat more dangerous than a rock"
		self.damage = 10
			
class RustySword(Weapon):
	def __init__(self):
		self.name = "Rusty Sword"
		self.description = "A rusty sword. Still good for piercing skin, though"
		self.damage = 20

################################		
#########CONSUMABLES############
################################

class HealthyCigarettes(Consumable):
	def __init__(self):
		self.name = "Healthy Cigarettes"
		self.healing_value = 10
