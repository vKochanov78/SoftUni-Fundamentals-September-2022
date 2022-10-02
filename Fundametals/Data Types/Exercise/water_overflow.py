number_of_lines = int(input())

tank_capacity = 255
total_water_poured = 0
for current_water_pour in range(number_of_lines):
    liters_of_water = int(input())
    if liters_of_water > tank_capacity:
        print("Insufficient capacity!")
        continue
    tank_capacity -= liters_of_water
    total_water_poured += liters_of_water
print(total_water_poured)