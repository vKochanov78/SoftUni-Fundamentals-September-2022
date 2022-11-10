text = input()
replaced_text = text.replace(" ", "")
dictionary = {}

for char in replaced_text:
    if char not in dictionary.keys():
        dictionary[char] = 0
    dictionary[char] += 1

for char, occurrences in dictionary.items():
    print(f"{char} -> {occurrences}")