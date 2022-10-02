from math import floor

number_of_companions = int(input())
days = int(input())

coins = 0
for current_day in range(1, days + 1):
    # Every 10th (tenth) day at the start of the day, 2 (two) of your companions leave.
    if current_day % 10 == 0:
        number_of_companions -= 2
    # But every 15th (fifteenth) day 5 (five) new companions are joined at the beginning of the day.
    if current_day % 15 == 0:
        number_of_companions += 5
    # Every 3rd (third) day, you organize a motivational party, spending 3 coins per companion for drinking water.
    if current_day % 3 == 0:
        coins -= number_of_companions * 3
    # Every 5th (fifth) day, you slay a boss monster and gain 20 coins per companion.
    # But if you have a motivational party the same day, you spend additional 2 coins per companion.
    if current_day % 5 == 0:
        coins += number_of_companions * 20
        if current_day % 3 == 0:
            coins -= number_of_companions * 2
    # Every day, you earn 50 coins, but you also spend 2 coins per companion for food.
    coins += 50
    coins -= number_of_companions * 2
coins_per_companion = floor(coins / number_of_companions)
print(f"{number_of_companions} companions received {coins_per_companion} coins each.")