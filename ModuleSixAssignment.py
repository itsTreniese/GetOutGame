# Author: Treniese Ladson

#Dictionary of rooms
            #'room': {'North': '', 'East': '', 'West':'', 'South':''}
rooms = {
    'Kitchen': {'North': 'Grandpa_Walter_Bedroom', 'East': 'Hallway'},
    'Hallway': {'North': 'Rose_Bedroom', 'East': 'Memory_Vault', 'South': 'Georgina_Bedroom', 'West': 'Kitchen'},
    'Rose_Bedroom': {'East': 'Rose_Closet', 'West': 'Grandpa_Walter_Bedroom', 'South': 'Hallway'},
    'Rose_Closet': {'West': 'Rose_Bedroom'},
    'Grandpa_Walter_Bedroom': {'East': 'Rose_Bedroom', 'South': 'Kitchen'},
    'Memory_Vault': {'North': 'Hypnotist_Lair', 'West': 'Hallway'},
    'Hypnotist_Lair': {'South': 'Memory_Vault'},
    'Georgina_Bedroom': {'North': 'Hallway', 'East': 'Dean_Office'},
    'Dean_Office': {'West': 'Georgina_Bedroom'}
}
#start
current_room = 'Kitchen'

#            ..::Welcome::.
print("\n 🍵 .:Clink Clink:.\n")
print("Uh... Oh!!!... Looks like you fell into the Sunken Place.")
print("You're trapped in the Armitage house. \nFind a way out before Mrs. Armitage clinks that 🍵  again and you're stuck here FOREVER.")
print("\nType: 'Go North', 'Go East', 'Go West', or 'Go South' to move. Type 'exit' to quit.\n")

# Game
# Input handling enhanced based on instructor feedback:
# - Trims whitespace
# - Accepts flexible input like " go   north"
# - Validates direction and format
while current_room != 'exit':
    print("You're currently in the", current_room.replace('_', ' '))

    # Get player input
    command = input("Enter your next move: ").strip().lower()
    split_command = command.split()


    if command == 'exit':
        print("\n       You feel yourself waking up... maybe...")
        break

    if len(split_command) < 2:
        print("  ❌ Invalid command format. Try something like 'go north' or 'get car keys'.\n")
        continue

    direction = split_command[0]
    next_room = ' '.join(split_command[1:]).title()

    if direction == "go":
        if next_room in rooms[current_room]:
            current_room = rooms[current_room][next_room]
            print(f"You move {next_room} to the {current_room.replace('_', ' ')}.\n")
        else:
            print(" 🚫 No... You can't go that way. Be quiet and try again...\n")

    else:
        print("Invalid command!!! Try 'go North' or type 'exit'.\n")