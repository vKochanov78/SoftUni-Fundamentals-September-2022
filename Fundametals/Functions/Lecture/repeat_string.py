input_line = input()
number_of_repeats = int(input())

repeat_string = lambda first_string, repeats: first_string * repeats
result = repeat_string(input_line, number_of_repeats)
print(result)