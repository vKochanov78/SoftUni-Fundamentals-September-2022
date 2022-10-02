number_of_lines = int(input())
lst = []


# Commands
COMMAND_EVEN = "even"
COMMAND_ODD = "odd"
COMMAND_POSITIVE = "positive"
COMMAND_NEGATIVE = "negative"

for _ in range(number_of_lines):
    current_number = int(input())
    lst.append(current_number)

filtered_lst = []
command = input()

for num in lst:
    passed = (
        (command == COMMAND_EVEN and num % 2 == 0) or
        (command == COMMAND_ODD and num % 2 != 0) or
        (command == COMMAND_POSITIVE and num >= 0) or
        (command == COMMAND_NEGATIVE and num < 0)
    )
    if passed:
        filtered_lst.append(num)
print(filtered_lst)