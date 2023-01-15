def playing_game(heroes):

    while True:
        command = input().split(" - ")

        if command[0] == "End":
            break

        current_command = command[0]

        if current_command == "CastSpell":
            hero_name, mp_needed, spell_name = command[1], int(command[2]), command[3]

            if mp_needed <= heroes[hero_name][1]:
                heroes[hero_name][1] -= mp_needed
                mana_left = heroes[hero_name][1]
                print(f"{hero_name} has successfully cast {spell_name} and now has {mana_left} MP!")
            else:
                print(f"{hero_name} does not have enough MP to cast {spell_name}!")

        elif current_command == "TakeDamage":
            hero_name, damage, attacker = command[1], int(command[2]), command[3]

            available_hp = heroes[hero_name][0]

            if available_hp - damage > 0:
                heroes[hero_name][0] -= damage
                hp_left = heroes[hero_name][0]
                print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {hp_left} HP left!")
            else:
                del heroes[hero_name]
                print(f"{hero_name} has been killed by {attacker}!")

        elif current_command == "Recharge":
            hero_name, amount = command[1], int(command[2])

            available_mp = heroes[hero_name][1]

            if heroes[hero_name][1] + amount > 200:
                amount = 200 - available_mp
                heroes[hero_name][1] += amount
            else:
                heroes[hero_name][1] += amount

            print(f"{hero_name} recharged for {amount} MP!")

        elif current_command == "Heal":
            hero_name, amount = command[1], int(command[2])

            available_hp = heroes[hero_name][0]

            if available_hp + amount > 100:
                amount = 100 - available_hp
                heroes[hero_name][0] += amount
            else:
                heroes[hero_name][0] += amount

            print(f"{hero_name} healed for {amount} HP!")


def print_function(heroes):
    print_result = ""

    for hero in heroes:
        print_result += f'{hero}\n  HP: {heroes[hero][0]}\n  MP: {heroes[hero][1]}\n'

    return print_result


def heroes_of_code(number):
    heroes = {}

    for current_hero in range(number):
        name, hit_points, mana_points = input().split()
        heroes[name] = [int(hit_points), int(mana_points)]

    playing_game(heroes)

    print(print_function(heroes))


number_of_heroes = int(input())
heroes_of_code(number_of_heroes)
