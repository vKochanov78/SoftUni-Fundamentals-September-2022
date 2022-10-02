orders_number = int(input())

total_price = 0
for i in range(orders_number):
    price_per_capsule = float(input())
    days = int(input())
    capsules_needed = int(input())
    price = 0
    if 0.01 <= price_per_capsule <= 100:
        if 1 <= days <= 31:
            if 1 <= capsules_needed <= 2000:
                price = days * (price_per_capsule * capsules_needed)
                total_price += price
                print(f"The price for the coffee is: ${price:.2f}")

print(f"Total: ${total_price:.2f}")