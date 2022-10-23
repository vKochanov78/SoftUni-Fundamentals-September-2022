def positive_numbers(num):
        return [number for number in num if int(number) >= 0]


def negative_numbers(num):
    return [number for number in num if int(number) < 0]


def even_numbers(num):
    return [number for number in num if int(number) % 2 == 0]


def odd_numbers(num):
    return [number for number in num if int(number) % 2 != 0]


numbers = input().split(", ")
print(f"Positive: {', '.join(positive_numbers(numbers))}")
print(f"Negative: {', '.join(negative_numbers(numbers))}")
print(f"Even: {', '.join(even_numbers(numbers))}")
print(f"Odd: {', '.join(odd_numbers(numbers))}")