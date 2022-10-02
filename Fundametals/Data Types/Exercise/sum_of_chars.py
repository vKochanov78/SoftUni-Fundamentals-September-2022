number_of_lines = int(input())
sum_of_characters = 0
for current_index in range(number_of_lines):
    current_character = input()
    sum_of_characters += ord(current_character)
print(f"The sum equals: {sum_of_characters}")