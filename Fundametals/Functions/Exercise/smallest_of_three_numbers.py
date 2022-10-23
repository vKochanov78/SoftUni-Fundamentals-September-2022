def smallest_number(number):
    return min(number)


first_number = int(input())
second_number = int(input())
third_number = int(input())

numbers_list = [first_number, second_number, third_number]
min_number = smallest_number(numbers_list)
print(min_number)