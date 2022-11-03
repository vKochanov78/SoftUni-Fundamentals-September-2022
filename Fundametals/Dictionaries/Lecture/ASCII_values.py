character_lst = input().split(", ")
ascii_values = {key: ord(key) for key in character_lst}
print(ascii_values)