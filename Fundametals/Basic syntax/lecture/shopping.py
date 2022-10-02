budget = int(input())

budget_left = budget
command = input()

while command != "End":
    price = int(command)
    budget_left -= price
    if budget_left < 0:
        print("You went in overdraft!")
        break
    command = input()
else:
    print("You bought everything needed.")