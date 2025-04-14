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
while current_room != 'exit':
    print("You're currently in the", current_room.replace('_', ' '))
    command = input("Enter your next move: ").strip().lower()

    if command == 'exit':
        print("\n       You feel yourself waking up... maybe...")
        current_room = 'exit'

    elif command.startswith("go "):
        direction = command[3:].capitalize()

        if direction in rooms[current_room]:
            next_room = rooms[current_room][direction]
            print(f"You move {direction} to the {next_room.replace('_', ' ')}.\n")
            current_room = next_room
        else:
            print("No... You can't go that way. Be quiet and try again...\n")

    else:
        print("NO! You can't go that way!!! Try 'go North' or type 'exit'.\n")