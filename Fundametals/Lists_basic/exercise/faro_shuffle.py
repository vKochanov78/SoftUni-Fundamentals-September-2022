first_deck = input().split()
count_of_shuffles = int(input())

for shuffle in range(count_of_shuffles):
    final_deck = []
    middle_of_deck = len(first_deck) // 2
    left_part = first_deck[:middle_of_deck]
    right_part = first_deck[middle_of_deck:]
    for card_index in range(len(left_part)):
        final_deck.append(left_part[card_index])
        final_deck.append(right_part[card_index])
    first_deck = final_deck
print(first_deck)