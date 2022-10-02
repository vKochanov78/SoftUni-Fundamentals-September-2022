number = int(input())
for first_letter in range(number):
    for second_letter in range(number):
        for third_letter in range(number):
            print(f"{chr(first_letter + 97)}{chr(second_letter + 97)}{chr(third_letter + 97)}")