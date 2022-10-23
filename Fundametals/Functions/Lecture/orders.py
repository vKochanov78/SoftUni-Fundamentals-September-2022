def order_calculator(prod, quan):
    total_price = 0
    if prod == "coffee":
        total_price = quan * 1.5
    elif prod == "coke":
        total_price = quan * 1.4
    elif prod == "water":
        total_price = quan * 1
    elif prod == "snacks":
        total_price = quan * 2
    return f"{total_price:.2f}"



product = input()
quantity_of_product = int(input())

print(order_calculator(product, quantity_of_product))