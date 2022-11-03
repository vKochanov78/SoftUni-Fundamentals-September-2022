elements = input().split()
stock = {}
products_to_search = input().split()

for index in range(0, len(elements), 2):
    product = elements[index]
    quantity = elements[index + 1]
    stock[product] = int(quantity)

for product in products_to_search:
    if product in stock.keys():
        quantity = stock[product]
        print(f"We have {quantity} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")