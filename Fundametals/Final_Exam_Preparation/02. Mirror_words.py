import re

text = input()

pattern = r"(@|#)([a-zA-Z]{3,})(\1{2})([a-zA-Z]{3,})\1"
mirror_words = []

result = re.findall(pattern, text)

for pair in result:
    if pair[1] == pair[3][::-1]:
        mirror_words.append(f"{pair[1]} <=> {pair[3]}")

if not result:
    print("No word pairs found!")
else:
    print(f"{len(result)} word pairs found!")

if not mirror_words:
    print("No mirror words!")
else:
    print("The mirror words are:")
    print(", ".join(mirror_words))