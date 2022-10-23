def inventory_func(inventory):
    while True:
        command = input()

        if command == "Craft!":
            break

        command, product = command.split(" - ")

        if command == "Collect":
            if product not in inventory:
                inventory.append(product)

        elif command == "Drop":
            if product in inventory:
                inventory.remove(product)

        elif command == "Combine Items":
            first_value, second_value = product.split(":")
            if first_value in inventory:
                index = inventory.index(first_value)
                inventory.insert(index + 1, second_value)

        elif command == "Renew":
            if product in inventory:
                inventory.remove(product)
                inventory.append(product)

    print(", ".join(inventory))


data = input().split(", ")
inventory_func(data)