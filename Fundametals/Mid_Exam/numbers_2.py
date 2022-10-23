def number_func(sequence):
    while True:
        command = input().split()

        if command[0] == "Finish":
            return sequence

        if len(command) == 2:
            command, value = command[0], command[1]
        elif len(command) == 3:
            command, value1, value2 = command[0], command[1], command[2]

        if command == "Add":
            sequence.append(value)

        elif command == "Remove":
            if value in sequence:
                sequence.remove(value)

        elif command == "Replace":
            if value1 in sequence:
                index = sequence.index(value1)
                sequence[index] = value2

        elif command == "Collapse":
            for i in range(len(sequence) - 1, -1, -1):
                if int(sequence[i]) < int(value):
                    num_to_remove = sequence[i]
                    sequence.remove(num_to_remove)


data = input().split(" ")

print(*number_func(data))
