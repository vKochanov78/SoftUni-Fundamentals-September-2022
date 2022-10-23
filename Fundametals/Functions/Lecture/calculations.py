def solve(num1, num2, operation):
    if operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        result = int(num1 / num2)
    elif operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    return result

input_operation = input()
number_1 = int(input())
number_2 = int(input())
print(solve(number_1, number_2, input_operation))