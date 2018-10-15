"""
			Simple RPG
	Simple RPG is a text based RPG game where the player
	can move between rooms, pick up items, fight monsters 
	for the ultimate goal of escaping the mansion.
@author Michael Quinn
@version 0.2
@date October 14, 2018
"""
from rooms import rooms
import sys

def showInstructions() : #Make this all one string, no + signs 
						# include more detailed instruction on how to play and win.
	print("================" + 
	
		"\nCommands:" +
		"\n\'go\' [direction]" +
		"\n\'get' [item]" +
		"\n================")

def showStatus():
	print("-------STATUS-------" +
		"\nCurrent room: " + currentRoom +
		"\nInventory: " + str(inventory))
	if 'item' in rooms[currentRoom] :
		print("You see a " + rooms[currentRoom]['item'])
	print("--------------------")

inventory = [] #initialize an empty inventory
currentRoom = 'hall' #starting room

print("Welcome to Simple RPG!")
showInstructions()

while True:
	showStatus() 
	move = ''
	while move == '':
		move = input(">")
	move = move.lower().split() #split the move command into a list
		
	if move[0] == 'go': #if the move command begins with 'go'
		if move[1] in rooms[currentRoom]:
			currentRoom = rooms[currentRoom][move[1]]
		else:
			print("You can\'t go that way!")

	if move[0] == 'get': #if the move command begins with 'get'
		if 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']: #if the room contains an item and if its the item specified
			inventory += [move[1]] #add the item to the inventory
			del rooms[currentRoom]['item']
			print("got " + move[1])
		else : 
			print("can\'t get " + move[1])
	if currentRoom == 'foyer' and 'key' in inventory:
		print("You unlucked the door...")
		inventory.remove('key')
	if currentRoom == 'garden':
		print("You escaped the mansion... YOU WIN!")
		break
