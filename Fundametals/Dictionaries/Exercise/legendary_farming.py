items = {"shards": 0, "fragments": 0, "motes": 0}
obtained = False
materials = input().split()

while not obtained:
    for index in range(0, len(materials), 2):
        material = materials[index + 1].lower()
        quantity = int(materials[index])

        if material not in items.keys():
            items[material] = 0
        items[material] += quantity

        if items["shards"] >= 250:
            items["shards"] -= 250
            obtained = True
            print("Shadowmourne obtained!")

        elif items["fragments"] >= 250:
            items["fragments"] -= 250
            obtained = True
            print("Valanyr obtained!")

        elif items["motes"] >= 250:
            items["motes"] -= 250
            obtained = True
            print("Dragonwrath obtained!")
        if obtained:
            break
    if obtained:
        break
    materials = input().split()

for material, number_of_shards in items.items():
    print(f"{material}: {number_of_shards}")

