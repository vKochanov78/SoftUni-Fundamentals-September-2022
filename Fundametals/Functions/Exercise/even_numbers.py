list_of_numbers = map(int, input().split())

even_numbers_list = list(filter(lambda x: x % 2 == 0, list_of_numbers))

print(even_numbers_list)