import random
import enemies

class MapTile:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def intro_text(self):
		raise NotImplementedError("Create a subclass instead!")

	def modify_player(self, player):
		pass



class StartTile(MapTile):
	def intro_text(self):
		return """
		You awake to find yourself in a mine.
		
		At least you think its a mine
		 
		The taste of coal dust is in your mouth.
		
		Looking around, you can see four dark paths.
		"""

class EnemyTile(MapTile):
	def __init__(self, x, y):
		r = random.random()
		if r < 0.30:
			self.enemy = enemies.MineRat()
			self.alive_text = "A Mine Rat scurries in front of you barring it teeth"
			self.dead_text = "The corpse of a dead rat is on the ground"
		elif r < 0.75:
			self.enemy = enemies.PitPony()
			self.alive_text = "A Pit Pony bucks and snorts"
			self.dead_text = "A dead Pit Pony look sup at you with lifeless eyes.\nLooks like this pony won't be carrying any more coal.."
		elif r < 0.90:
			self.enemy = enemies.ZombieMiner()
			self.alive_text = "A zombie dressed in a mining outfit swings his pickaxe wildly in your direction"
			self.dead_text = "The dead zombie reminds you of your triumph"
		else:
			self.enemy = enemies.SingingZombie()
			self.alive_text = "A zombie sits on the ground, strumming his guitar and singing. \n His songs drain your HP"
			self.dead_text = "Black-ass nigga singing zombie mofo is dead!"
			
		super().__init__(x, y)
	
	def modify_player(self, player):
		if self.enemy.is_alive():
			player.hp = player.hp - self.enemy.damage
			print("{} does {} damage! You have {} health remaining.".format(self.enemy, self.enemy.damage, player.hp))
	
	def intro_text(self):
		text = self.alive_text if self.enemy.is_alive() else self.dead_text
		return text




class VictoryTile(MapTile):
	def intro_text(self):
		return """
		You see a bright light in the distance. 
		Could it be?
		
		Yes! It's the exit!
		You're free at last.. But the memories of what happened here
		will haunt you forever...
		"""



def tile_at(x, y):
	if x < 0 or y < 0:
		return None
	try:
		return world_map[y][x]
	except IndexError:
		return None

world_map = [
	[None,VictoryTile(1,0),None],
	[None,EnemyTile(1,1),None],
	[EnemyTile(0,2),StartTile(1,2),EnemyTile(2,2)],
	[None,EnemyTile(1,3),None]
]
