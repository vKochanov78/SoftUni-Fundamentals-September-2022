def destinations_func(data):

    while True:
        command = input().split(":")

        if command[0] == "Travel":
            print(f"Ready for world tour! Planned stops: {data}")
            break

        elif command[0] == "Add Stop":
            index, stop = int(command[1]), command[2]

            if 0 <= index < len(data):
                data = data[:index] + stop + data[index:]

        elif command[0] == "Remove Stop":
            start_index, end_index = int(command[1]), int(command[2])

            if 0 <= start_index <= end_index < len(data):
                data = data[:start_index] + data[end_index + 1:]

        elif command[0] == "Switch":
            old_string, new_string = command[1], command[2]

            if old_string in data:
                data = data.replace(old_string, new_string)
        print(data)


destinations = input()
destinations_func(destinations)
