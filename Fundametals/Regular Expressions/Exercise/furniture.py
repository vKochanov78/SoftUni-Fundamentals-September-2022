import re

furniture_bought = []
total_money = 0

pattern = r">>([a-zA-Z]+)<<(\d+\.?\d*)!(\d+)"
item = input()

while item != "Purchase":
    matches = re.search(pattern, item)

    if matches:
        furniture, price, quantity = matches.groups()
        furniture_bought.append(furniture)
        total_money += float(price) * int(quantity)
    item = input()

print("Bought furniture:")
for furniture in furniture_bought:
    print(furniture)
print(f"Total money spend: {total_money:.2f}")