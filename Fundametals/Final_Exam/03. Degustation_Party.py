guests_collection = {}
dislike_meals_count = 0

while True:
    command = input().split("-")

    if command[0] == "Stop":
        break

    if command[0] == "Like":
        guest, meal = command[1], command[2]

        if guest not in guests_collection:
            guests_collection[guest] = [meal]
        elif guest in guests_collection and meal not in guests_collection[guest]:
            guests_collection[guest].append(meal)

    elif command[0] == "Dislike":
        guest, meal = command[1], command[2]

        if guest not in guests_collection:
            print(f"{guest} is not at the party.")

        elif meal not in guests_collection[guest]:
            print(f"{guest} doesn't have the {meal} in his/her collection.")

        else:
            dislike_meals_count += 1
            guests_collection[guest].remove(meal)
            print(f"{guest} doesn't like the {meal}.")

for guest, meals in guests_collection.items():
    print(f"{guest}: {', '.join(meals)}")

print(f"Unliked meals: {dislike_meals_count}")

