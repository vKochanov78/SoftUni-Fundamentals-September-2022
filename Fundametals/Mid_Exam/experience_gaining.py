needed_experience = float(input())
count_of_battles = int(input())

count_of_moves_to_win = 0
total_experience = 0
is_unlocked = False

for current_battle in range(1, count_of_battles + 1):

    exp_for_current_battle = float(input())

    count_of_moves_to_win += 1

    if current_battle % 3 == 0:
        exp_for_current_battle *= 1.15

    if current_battle % 5 == 0:
        exp_for_current_battle *= 0.9

    if current_battle % 15 == 0:
        exp_for_current_battle *= 1.05

    total_experience += exp_for_current_battle

    if needed_experience <= total_experience:
        is_unlocked = True
        break

difference = abs(needed_experience - total_experience)

if is_unlocked:
    print(f"Player successfully collected his needed experience for {count_of_moves_to_win} battles.")
else:
    print(f"Player was not able to collect the needed experience, {difference:.2f} more needed.")