food_quantity_in_grams = float(input()) * 1000
hay_quantity_in_grams = float(input()) * 1000
cover_quantity_in_grams = float(input()) * 1000
pig_weight_in_grams = float(input()) * 1000

is_enough = True

for day in range(1, 31):
    food_quantity_in_grams -= 300

    if food_quantity_in_grams < 0 or \
            hay_quantity_in_grams < 0 or \
            cover_quantity_in_grams < 0:
        is_enough = False
        break

    if day % 2 == 0:
        hay_quantity_in_grams -= food_quantity_in_grams * 0.05
    if day % 3 == 0:
        cover_quantity_in_grams -= pig_weight_in_grams / 3

if is_enough:
    food_quantity_in_kg = food_quantity_in_grams / 1000
    hay_quantity_in_kg = hay_quantity_in_grams / 1000
    cover_quantity_in_kg = cover_quantity_in_grams / 1000
    print(f"Everything is fine! Puppy is happy! Food: {food_quantity_in_kg:.2f},"
          f" Hay: {hay_quantity_in_kg:.2f}, Cover: {cover_quantity_in_kg:.2f}.")
else:
    print("Merry must go to the pet store!")