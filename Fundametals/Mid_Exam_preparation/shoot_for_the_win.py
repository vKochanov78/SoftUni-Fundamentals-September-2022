def reduce_values(target, index):
    special_value = target[index]
    target[index] = -1
    for i in range(len(target)):
        if target[i] == -1:
            continue

        if special_value < target[i]:
            target[i] -= special_value
        else:
            target[i] += special_value

    return target


def shoot_for_the_win(target):
    count_of_shot_targets = 0

    while True:
        command = input()

        if command == "End":
            break

        current_index = int(command)
        if 0 <= current_index < len(sequence) and target[current_index] != -1:
            count_of_shot_targets += 1
            reduce_values(target, current_index)

    convert_target_values_to_string = [str(num) for num in target]
    print(f"Shot targets: {count_of_shot_targets} -> {' '.join(convert_target_values_to_string)}")


sequence = list(map(int, input().split(" ")))
shoot_for_the_win(sequence)