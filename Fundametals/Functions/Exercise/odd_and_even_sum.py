def odd_and_even_sum(number):
    sum_of_even_digits = 0
    sum_of_odd_digits = 0
    for current_digit in number:
        if int(current_digit) % 2 == 0:
            sum_of_even_digits += int(current_digit)
        else:
            sum_of_odd_digits += int(current_digit)
    return sum_of_odd_digits, sum_of_even_digits


single_number = input()
sum_of_odd_digits, sum_of_even_digits = odd_and_even_sum(single_number)

print(f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}")