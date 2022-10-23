text = input()
vowels = ['a', 'o', 'u', 'e', 'i']

new_lst = [ch for ch in text if ch.lower() not in vowels]
print("".join(new_lst))