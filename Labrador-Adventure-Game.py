def main_menu():
    # instructions and intro
    print('\n--------------------------------------------------------------------')
    print('\n*     *  * * * *  *     *        *  * *  * * * *  **   **  * * * *')
    print('* *   *  *        *     *        *       *     *  * * * *  *      ')
    print('*  *  *  * * *    *  *  *        *   **  * * * *  *  *  *  * * *  ')
    print('*   * *  *        * * * *        *    *  *     *  *     *  *      ')
    print('*     *  * * * *  **   **        *  * *  *     *  *     *  * * * *\n')
    print('--------------------------------------------------------------------\n')
    print("Welcome to the Labrador game, reach the Kitchen after collecting all 6 items to win.")
    print("To move, type: up, down, left, or right. You can also type quit at any time to quit.")


# each room and how they connect to each other
rooms = {
    'Foyer': {'down': 'Living Room', 'left': 'Backyard', 'up': 'Bedroom', 'right': 'Dining Room'},
    'Living Room': {'up': 'Foyer', 'right': 'Basement', 'item': 'Frisbee'},
    'Basement': {'left': 'Living Room', 'item': 'Squeaky toy'},
    'Backyard': {'right': 'Foyer', 'item': 'Stick'},
    'Bedroom': {'down': 'Foyer', 'right': 'Bathroom', 'item': 'Ball'},
    'Bathroom': {'left': 'Bedroom', 'item': 'Rope'},
    'Dining Room': {'left': 'Foyer', 'up': 'Kitchen', 'item': 'Bone'},
    'Kitchen': {'down': 'Dining Room'},
}
# define the directions
directions = ['up', 'down', 'right', 'left']
def move_between_rooms(current_room, move, rooms):
    current_room = rooms[current_room][move]

# adding and removing items from the player's inventory
# also remove the item from the associated room
def get_item(current_room, move, rooms, inventory):
    inventory.append(rooms[current_room]['item'])
    del rooms[current_room]['item']

# list for storing player inventory
inventory = []
# starting room
current_room = "Foyer"
# show the player the main menu
main_menu()



# main game loop
while True:
    # when the player encounters the cat
    if current_room == 'Kitchen':
        # if they won
        if len(inventory) == 6:
            print("\nThe villainous cat is impressed by the collection of toys, he allows you to keep them.")
            print("\nYOU WIN!")
        # if they lost
        else:
            print("\nYou did not collect all of the items!")
            print("The villainous cat does not respect you because you don’t have enough toys.")
            print("YOU LOSE!")
        # ask player if they'd like to play the game again
        play_again = input("\nWould you like to play again? Type ""yes"" or ""no"" :")
        if play_again == 'yes':
            inventory = []
            current_room = "Foyer"
            main_menu()
            continue
        elif play_again == 'no':
            print('\nThanks for playing the Labrador Game!')
            print("Fun fact: This game was inspired by my toy loving lab, Mara <3")
            print("Have a good day!")
            break
        else:
            print("Invalid input, ending game.")
            print('\nThanks for playing the Labrador Game!')
            print("Fun fact: This game was inspired by my toy loving lab, Mara <3")
            print("Have a good day!")
            break
    # tell the user their current room and prompt for a move
    print('You are currently in the ' + current_room)
    # tell the user if there is an item in the room
    if current_room != 'item' in rooms[current_room].keys():
        print('You see the {} and add it to your inventory'.format(rooms[current_room]['item']))
        if (rooms[current_room]['item']) not in list(inventory):
            inventory.append(rooms[current_room]['item'])
    # tell user their inventory
    print('Your inventory now consists of:')
    print(inventory)
    print('\n--------------------------------------------------------------------\n')

    # prompt user for direction to move between rooms
    command = input('\nEnter your move :')
    if command in directions:
        command = command.replace("go", "")
        if command in rooms[current_room].keys():
            current_room = rooms[current_room][command]
        else:
            # if the player inputs a direction where there's not a room
            print('You cant go that way!')
    # checks to see if the player quits the game
    elif command == 'quit':
        print('\nThanks for playing!')
        break
    # invalid command
    else:
        print('\nInvalid input, please type up, down, left, or right\n')
        continue