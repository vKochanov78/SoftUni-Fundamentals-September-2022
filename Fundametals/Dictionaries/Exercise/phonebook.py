phonebook = {}

while True:
    contact = input()
    if "-" not in contact:
        break
    name, phone_number = contact.split("-")

    phonebook[name] = phone_number

for check in range(1, int(contact) + 1):
    searched_name = input()

    if searched_name in phonebook.keys():
        print(f"{searched_name} -> {phonebook[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")
