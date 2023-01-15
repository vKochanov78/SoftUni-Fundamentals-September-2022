import re


number_of_inputs = int(input())

pattern = r"^(\%|\$)([A-Z][a-z]{2,})\1: \[(\d+)\]\|\[(\d+)\]\|\[(\d+)\]\|$"

for _ in range(number_of_inputs):
    current_input = input()

    result = re.search(pattern, current_input)

    if result:
        result = result.groups()
        request = result[1]
        first_letter = chr(int(result[2]))
        second_letter = chr(int(result[3]))
        third_letter = chr(int(result[4]))

        print(f"{request}: {first_letter}{second_letter}{third_letter}")
    else:
        print("Valid message not found!")