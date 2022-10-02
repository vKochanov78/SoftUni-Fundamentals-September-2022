# You will receive Peter's lost fights count
lost_fight_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

# Every second lost game, his helmet is broken.
helmets_broken = lost_fight_count // 2
# Every third lost game, his sword is broken.
swords_broken = lost_fight_count // 3
# When both his sword and helmet are broken in the same lost fight, his shield also breaks.
shields_broken = lost_fight_count // 6
# Every second time his shield brakes, his armor also needs to be repaired.
armors_broken = lost_fight_count // 12

total_expenses = helmet_price * helmets_broken +\
                 sword_price * swords_broken + \
                 shield_price * shields_broken + \
                 armor_price * armors_broken
print(f"Gladiator expenses: {total_expenses:.2f} aureus")