"""
			Simple RPG
	Simple RPG is a text based RPG game where the player
	can move between rooms, pick up items, fight monsters 
	for the ultimate goal of escaping the mansion.
	
	This version adds in a second dictionary for the holding
	item and monster information for better print statements.
@author Michael Quinn
@version 0.3
@date October 14, 2018
"""
from rooms import *
import sys

def showInstructions() :
	print("""================
The objective of the game is simple: Escape the mansion.
You can move from room to room collecting items to help you in
this task, but watch out for the monster!
Commands:
\'go\' [direction]
\'get' [item]
\'quit'
================""")

def showStatus():
	print("-------STATUS-------" +
		"\nCurrent room: " + currentRoom +
		"\nAvailable directions: " + str(list(rooms[currentRoom].keys())) +
		"\nInventory: " + str(inventory))
	if 'item' in items[currentRoom] :
		print("You see a " + items[currentRoom]['item'])
	print("--------------------")

inventory = [] #initialize an empty inventory
currentRoom = 'hall' #starting room

print("Welcome to Simple RPG!")
showInstructions()

while True:
	try:
		showStatus() 
		move = ''
		while move == '':
			move = input(">")
		move = move.lower().split() #split the move command into a list
			
		if move[0] == 'quit':
			print("Thanks for playing!")
			break
		if move[0] == 'go': #if the move command begins with 'go'
			assert len(move) == 2 , "'go' command requires 2 entries!"
			
			if move[1] in rooms[currentRoom]:
				currentRoom = rooms[currentRoom][move[1]]
			else:
				print("You can't go that way!")
			

		if move[0] == 'get': #if the move command begins with 'get'
			assert len(move) == 2 , "'get' command requires 2 entries!"
			if 'item' in items[currentRoom] and move[1] in items[currentRoom]['item']: #if the room contains an item and if its the item specified
				inventory += [move[1]] #add the item to the inventory
				del items[currentRoom]['item']
				print("got " + move[1])
			else : 
				print("can\'t get " + move[1])
		if currentRoom == 'foyer' and 'key' in inventory:
			print("You unlucked the door...")
			inventory.remove('key')
			rooms['foyer'].update({'east' : 'garden'})
		if currentRoom == 'garden':
			print("You escaped the mansion... YOU WIN!")
			break
		if 'monster' in items[currentRoom]:
			print("Ah! there's a " + items[currentRoom]['monster'] + "!")
			print("GAME OVER!")
			break
	except AssertionError:
		print("Oh no! \nSomething went wrong!")
		raise
	except:
		print("Game breaking crash, please send reports to Quinnovations.Feedback@gmail.com!")
