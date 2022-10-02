list_of_numbers = input().split()
numbers_to_remove = int(input())
next_index = 1
removed_numbers_count = 0
list_of_numbers_as_digit = []
final_lst = []

for element in list_of_numbers:
    list_of_numbers_as_digit.append(int(element))

for _ in range(numbers_to_remove):
    list_of_numbers_as_digit.remove(min(list_of_numbers_as_digit))

for i in list_of_numbers_as_digit:
    final_lst.append(str(i))

print(", ".join(final_lst))