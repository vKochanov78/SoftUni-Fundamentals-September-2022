number_of_snowballs = int(input())
max_value = 0
for current_snowball in range(1, number_of_snowballs + 1):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    value = (snowball_weight / snowball_time) ** snowball_quality
    if value > max_value:
        max_value = value
        max_weight = snowball_weight
        max_time = snowball_time
        max_quality = snowball_quality
print(f"{max_weight} : {max_time} = {int(max_value)} ({max_quality})")