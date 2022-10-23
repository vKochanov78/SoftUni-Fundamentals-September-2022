from math import factorial

def factorial_division(number):
    result = factorial(number)
    return result

first_number = int(input())
second_number = int(input())

first_number_factorial = factorial_division(first_number)
second_number_factorial = factorial_division(second_number)

final_result = first_number_factorial / second_number_factorial
print(f"{final_result:.2f}")