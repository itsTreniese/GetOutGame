# Author: Treniese Ladson

#Dictionary of rooms
            #'room': {'North': '', 'East': '', 'West':'', 'South':'', 'room_message':''}
rooms = {
    'Kitchen': {'North': 'Grandpa_Walter_Bedroom', 'East': 'Hallway', 'item':'Teacup'},
    'Hallway': {'North': 'Rose_Bedroom', 'East': 'Memory_Vault', 'South': 'Georgina_Bedroom', 'West': 'Kitchen', 'item':'Gulf Club', 'room_message':' ... I got a feeling, you\'ll need this!'},
    'Rose_Bedroom': {'East': 'Rose_Closet', 'West': 'Grandpa_Walter_Bedroom', 'South': 'Hallway', 'item':'Car Keys', 'room_message':' Grab the keys!!! 🤫 ...Be QUIET!!!'},
    'Rose_Closet': {'West': 'Rose_Bedroom', 'item':'Earplugs', 'room_message':'  Quick put them in... '},
    'Grandpa_Walter_Bedroom': {'East': 'Rose_Bedroom', 'South': 'Kitchen','item':'Jesse Owens picture'},
    'Memory_Vault': {'North': 'Hypnotist_Lair', 'West': 'Hallway', 'item':'Your family portrait'},
    'Hypnotist_Lair': {'South': 'Memory_Vault', 'room_message':'The floor creaks...'},
    'Georgina_Bedroom': {'North': 'Hallway', 'East': 'Dean_Office', 'item':'Flashlight'},
    'Dean_Office': {'West': 'Georgina_Bedroom', 'item':'a TV', 'room_message':'The Coagula video procedure is playing. 😨 Will you make it out?! '}
}



#   Game Instructions
def player_instructions():
    #            ..::Welcome::.
    print("\n 🍵 .:Clink Clink:.\n")
    print("Uh... Oh!!!... Looks like you fell into the Sunken Place.")
    print("You're trapped in the Armitage house. \nFind a way out before Mrs. Armitage clinks that 🍵 again and you're stuck here FOREVER.")
    print(
        f'\nType: "Go North", "Go East", "Go West", or "Go South" to move. Type "exit" to quit.\nType: "Get item", to place the item in your inventory \n')
    print('Ok, let\'s see if you can get out of here!')


#   Game
def show_status(current_room, inventory):
    print(" \n ----------------------------- ")

    # Format the room name
    generic_rooms = ['Kitchen', 'Hallway', 'Memory_Vault', 'Hypnotist_Lair']
    personal_rooms = ['Rose_Bedroom', 'Rose_Closet', 'Grandpa_Walter_Bedroom', 'Georgina_Bedroom', 'Dean_Office']

    if current_room in generic_rooms:
        room_display = current_room.replace('_', ' ')
        print(f"You're in the {room_display}")
    else:
        room_display = current_room.replace('_', "'s ")
        print(f"You're in {room_display}")

    # Show item in the room (unless it's the villain)
    if 'item' in rooms[current_room] and rooms[current_room]['item'].lower() != 'villain':
        print(f"You see: {rooms[current_room]['item']}")

    # Show room message only if item hasn't been collected
    if 'room_message' in rooms[current_room] and 'item' in rooms[current_room]:
        print(rooms[current_room]['room_message'])

    # Show inventory
    if inventory:
        print("\n Inventory:", ', '.join(inventory))
    else:
        print("\n Your inventory is empty.")

    print(" \n ----------------------------- ")

def main():
    current_room = 'Kitchen'
    inventory = []
    player_instructions()

    while True:
        show_status(current_room, inventory)
        command = input("Enter your move: ").strip().lower()
        split_command = command.split()

        if command == 'exit':
            print("Oh, You want to stay in the sunken place!!!\n  .:Clink Clink 🍵:. Sink!!! \n  Game Over. ")
            break

        if len(split_command) < 2:
            print("❌ Invalid command format. Try something like 'go north' or 'get keys'.\n")
            continue

        direction = split_command[0]
        next_room = ' '.join(split_command[1:]).title()

        # Movement
        if direction == "go":
            if next_room in rooms[current_room]:
                current_room = rooms[current_room][next_room]
                print(f"You move {next_room} to the {current_room.replace('_', ' ')}.\n")

                # Villain logic (enhanced decision-based encounter)
                if current_room == 'Hypnotist_Lair':
                    print("\n👁️ Mrs. Armitage stirs her cup... You feel yourself slipping into the Sunken Place...")

                    response = input("Will you use something from your inventory to resist? (yes/no): ").strip().lower()

                    if response == 'yes':
                        if 'Earplugs' in inventory and 'Gulf Club' in inventory:
                            print("\n🧠 You plug your ears and swing the club—CRACK!!! You knocked the cup from her hand.")
                            print("💥 You broke the spell and escaped the Sunken Place! \n You’re free! 🏃🏾‍♀️💨")
                        elif 'Earplugs' in inventory or 'Gulf Club' in inventory:
                            print("\n😬 You tried... but it wasn’t enough. One item alone couldn’t stop her.")
                            print("🌀 The teacup spins. You’re frozen in time. 💀 GAME OVER.")
                        else:
                            print("\nYou reach into your pockets, but there’s nothing useful...")
                            print("The cup clinks again... and everything fades to black. 💀 GAME OVER.")
                    else:
                        print("\nYou hesitate... the clink echoes... and you fall deeper. 😢")
                        print("GAME OVER.")
                    break
            else:
                print(" 🚫 No... You can't go that way. Be quiet and try again...\n")

        # Get item
        elif direction == "get":
            item = rooms[current_room].get("item", "").lower()
            if item and next_room.lower() == item:
                inventory.append(rooms[current_room]['item'])
                print(f"{rooms[current_room]['item']} added to your inventory.")
                del rooms[current_room]['item']
            else:
                print("❌ That item isn’t here, or you typed it wrong. Try again.\n")

        else:
            print("🤔 Not a valid command. Use 'go [direction]' or 'get [item]'.\n")

        # Victory warning
        if len(inventory) == 6 and current_room != 'Hypnotist_Lair':
            print("\n✨ You have all 6 items! Find the Hypnotist Lair and face Mrs. Armitage!")


if __name__ == "__main__":
    main()
