def characters_between(first_char, second_char):
    characters = []
    for current_char in range(ord(first_char) + 1, ord(second_char)):
        characters.append(chr(current_char))
    return characters


first_character = input()
second_character = input()

result = characters_between(first_character, second_character)
print(" ".join(result))