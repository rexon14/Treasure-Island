print("Welcome to Treasure Island")
print("Your mission is to find the treasure")

direction = str(input('''"You're at a cross road. Where do you want to go? Type "left" or "right".\n''')).lower()
if direction == "left":
    lake = str(input('''You came to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n''')).lower()
    if lake == "wait":
        doors = str(input('''You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n''')).lower()
        if doors == "blue":
            print("You enter a room of beasts. Game Over")
        elif doors == "red":
            print("The room is on fire. Game Over")
        elif doors == "yellow":
            print("You found the treasure. You Win!")
        else:
            print("Game Over")
    else:
        print("You attacked by trout. Game Over")
else:
    print("You fall into a hole. Game Over")
