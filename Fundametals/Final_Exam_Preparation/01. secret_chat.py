message = input()

while True:
    line = input().split(":|:")

    command = line[0]

    if command == "Reveal":
        print(f"You have a new text message: {message}")
        break

    if command == "InsertSpace":
        index = int(line[1])
        message = message[:index] + " " + message[index:]
        print(message)

    elif command == "Reverse":
        substring = line[1]
        if substring not in message:
            print("error")
        else:
            message = message.replace(substring, "", 1)
            message += substring[::-1]
            print(message)

    elif command == "ChangeAll":
        old_string, new_string = line[1], line[2]

        message = message.replace(old_string, new_string)

        print(message)