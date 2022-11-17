import re

dates = input()
pattern = r"\b(\d{2})([./-])([A-Z][a-z]{2})(\2)(\d{4})\b"

matches = re.findall(pattern, dates)

for match in matches:
    day, month, year = match[0], match[2], match[4]

    print(f"Day: {day}, Month: {month}, Year: {year}")