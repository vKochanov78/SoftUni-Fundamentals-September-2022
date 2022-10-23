card_list = input().split(", ")
number_of_commands = int(input())

for current_command in range(1, number_of_commands + 1):
    command = input().split(", ")

    if len(command) == 2:
        command, card = command[0], command[1]
    else:
        command, index, card, = command[0], int(command[1]), command[2]

    if command == "Add":
        if card not in card_list:
            card_list.append(card)
            print("Card successfully added")
        else:
            print("Card is already in the deck")

    elif command == "Remove":
        if card in card_list:
            card_list.remove(card)
            print("Card successfully removed")
        else:
            print("Card not found")

    elif command == "Remove At":
        index = int(card)
        if index <= len(card_list):
            card_list.pop(index)
            print("Card successfully removed")
        else:
            print("Index out of range")

    elif command == "Insert":
        if index <= len(card_list):
            if card not in card_list:
                card_list.insert(index, card)
                print("Card successfully added")
            else:
                print("Card is already added")
        else:
            print("Index out of range")

print(", ".join(card_list))