text = input()

while True:
    command = input().split()

    if command[0] == "Done":
        break

    if command[0] == "Change":
        current_char, new_char = command[1], command[2]

        text = text.replace(current_char, new_char)
        print(text)

    if command[0] == "Includes":
        substring = command[1]

        if substring in text:
            print("True")
        else:
            print("False")

    if command[0] == "End":
        substring = command[1]

        print(text.endswith(substring))

    if command[0] == "Uppercase":
        print(text.upper())

    if command[0] == "FindIndex":
        char = command[1]

        index = text.find(char)
        print(index)

    if command[0] == "Cut":
        start_index, count = int(command[1]), int(command[2])
        text = text[start_index:start_index + count]

        print(text)

