start_index = int(input())
final_index = int(input())

for current_character in range(start_index, final_index + 1):
    current_character = chr(current_character)
    print(current_character, end=" ")