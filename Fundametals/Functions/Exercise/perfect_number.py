def perfect_number(some_number):
    sum_of_all_digits = 0
    for num in range(1, some_number):
        if some_number % num == 0:
            sum_of_all_digits += num
    if sum_of_all_digits == some_number:
        return "We have a perfect number!"
    return "It's not so perfect."


number = int(input())
print(perfect_number(number))