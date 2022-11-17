text = input()
ciphered_text = ""

for letter in text:
    ciphered_text += letter.replace(letter, chr(ord(letter) + 3))

print(ciphered_text)