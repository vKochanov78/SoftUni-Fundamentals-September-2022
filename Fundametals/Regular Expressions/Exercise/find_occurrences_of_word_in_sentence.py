import re

sentence = input()
word = input() # searched word in the sentence
pattern = fr"\b{word}\b"

match = re.findall(pattern, sentence, re.IGNORECASE)

print(len(match))