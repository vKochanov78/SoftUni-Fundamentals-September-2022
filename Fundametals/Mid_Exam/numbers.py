def replace_func(value1, value2):
    index = sequence.index(value1)
    sequence.remove(value1)
    sequence.insert(index, value2)


def remove_func(value):
    sequence.remove(value)


def add_func(value):
    sequence.append(value)


def collapse_func(value):
    for num in sequence:
        if num < value:
            sequence.remove(num)


sequence = input().split()
while True:

    command = input().split()

    if len(command) == 1:
        print(" ".join(sequence))
        break

    if command[0] == "Add":
        add_func(command[1])

    elif command[0] == "Remove":
        remove_func(command[1])

    elif command[0] == "Replace":
        replace_func(command[1], command[2])

    elif command[0] == "Collapse":
        collapse_func(command[1])
