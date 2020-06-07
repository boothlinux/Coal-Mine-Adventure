class Enemy:
	def __init__(self):
		raise NotImplementedError("Do not create raw Enemy objects.")
	
	def __str__(self):
		return self.name

	def is_alive(self):
		return self.hp > 0

class MineRat(Enemy):
	def __init__(self):
		self.name = "Mine Rat"
		self.hp = 10
		self.damage = 2
		
class PitPony(Enemy):
	def __init__(self):
		self.name = "Pit Pony"
		self.hp = 30
		self.damage = 10

class ZombieMiner(Enemy):
	def __init__(self):
		self.name = "Zombie Miner"
		self.hp = 60
		self.damage = 15

class SingingZombie(Enemy):
	def __init__(self):
		self.name = "Singing Zombie Miner"
		self.hp = 100
		self.damage = 20
