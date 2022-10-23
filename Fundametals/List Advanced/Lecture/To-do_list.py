to_do_notes = []

while True:
    command = input()

    if command == "End":
        break

    split_command = command.split("-")
    importance = int(split_command[0])
    current_task = split_command[1]

    to_do_notes.append([importance, current_task])

sorted_tasks = []
for task in sorted(to_do_notes):
    sorted_tasks.append(task[1])

print(sorted_tasks)