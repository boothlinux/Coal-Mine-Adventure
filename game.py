from player import Player
import world

def play():
	print("Escape from the Springhill Mine!\n")
	player = Player()
	while True:
		room = world.tile_at(player.x, player.y)
		print(room.intro_text())
		room.modify_player(player)
		action_input = get_player_command()
		if action_input in ['n', 'north']:
			player.move_north()
		elif action_input in ['s', 'south']:
			player.move_south()
		elif action_input in ['e', 'east']:
			player.move_east()
		elif action_input in ['w', 'west']:
			player.move_west()
		elif action_input in ['i', 'inventory']:
			player.print_inventory()
		elif action_input in ['a', 'attack']:
			player.attack()
		elif action_input in ['h', 'heal']:
			player.heal()
		else:
			print("I'm sorry, I don't know that command..")
		

def get_player_command():
	return input('Action:  ').lower()

	
play()
