import re

sentence = input()
pattern = r"\b_([a-zA-Z]+\b)"

matches = re.findall(pattern, sentence)

if matches:
    print(",".join(matches))