number = int(input())
train = [0] * number

while True:
    command = input()
    split_command = command.split()
    action = split_command[0]
    if command == "End":
        break

    if action == "add":
        people_to_add = int(split_command[1])
        train[-1] += people_to_add
    elif action == "insert":
        index = int(split_command[1])
        people_to_add = int(split_command[2])
        train[index] += people_to_add

    elif action == "leave":
        index = int(split_command[1])
        people_to_leave = int(split_command[2])
        train[index] -= people_to_leave

print(train)