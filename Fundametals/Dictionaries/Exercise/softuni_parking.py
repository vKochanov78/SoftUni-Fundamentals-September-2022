parking = {}
number_of_cars = int(input())

for car in range(number_of_cars):
    entry = input().split()
    command = entry[0]

    if command == "register":
        username = entry[1]
        license_plate = entry[2]

        if username in parking.keys():
            print(f"ERROR: already registered with plate number {parking[username]}")
        else:
            parking[username] = license_plate
            print(f"{username} registered {license_plate} successfully")

    elif command == "unregister":
        username = entry[1]

        if username not in parking.keys():
            print(f"ERROR: user {username} not found")
        else:
            del parking[username]
            print(f"{username} unregistered successfully")

for username, license_plate in parking.items():
    print(f"{username} => {license_plate}")

