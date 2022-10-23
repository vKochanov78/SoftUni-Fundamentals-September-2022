first_list = input().split(", ")
second_list = input().split(", ")

final_string = []

for first_word in first_list:
    for second_word in second_list:
        if first_word in second_word:
            final_string.append(first_word)
            break

print(final_string)